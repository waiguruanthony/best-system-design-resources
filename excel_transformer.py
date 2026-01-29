#!/usr/bin/env python3
"""
Excel Time Log Transformer
Reads data from EXPORT_DECTOJAN2026.xlsx and populates Template_Jira_DPO.xlsx.
"""

import os
import sys
from datetime import datetime
from typing import Iterable, Optional

import pandas as pd

def examine_excel_structure(file_path: str) -> None:
    """Examine the structure of an Excel file to understand its sheets and columns."""
    print(f"\n=== Examining {os.path.basename(file_path)} ===")

    try:
        excel_file = pd.ExcelFile(file_path)
        print(f"Sheet names: {excel_file.sheet_names}")

        for sheet_name in excel_file.sheet_names:
            print(f"\n--- Sheet: {sheet_name} ---")
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            print(f"Shape: {df.shape} (rows x columns)")
            print(f"Columns: {list(df.columns)}")
            print("First few rows:")
            print(df.head())
            print("Data types:")
            print(df.dtypes)
            break
    except Exception as e:
        print(f"Error examining {file_path}: {e}")


def _normalize(value: str) -> str:
    return "".join(ch for ch in str(value).strip().lower() if ch.isalnum())


def _pick_column(
    columns: Iterable[str],
    candidates: Iterable[str],
    fallback_index: Optional[int] = None,
) -> Optional[str]:
    columns_list = list(columns)
    normalized = {_normalize(col): col for col in columns_list}
    for candidate in candidates:
        key = _normalize(candidate)
        if key in normalized:
            return normalized[key]
    if fallback_index is not None and 0 <= fallback_index < len(columns_list):
        return columns_list[fallback_index]
    return None


def _format_month_label(label) -> str:
    if isinstance(label, datetime):
        return label.strftime("%b %Y")
    if isinstance(label, pd.Timestamp):
        return label.strftime("%b %Y")
    return str(label).strip()

def transform_data(
    input_file: str,
    template_file: str,
    output_file: str,
    input_sheet: Optional[str] = None,
    template_sheet: Optional[str] = None,
) -> Optional[pd.DataFrame]:
    """Transform input time log data to populate the template."""
    print("\n=== Transforming Data ===")

    try:
        input_df = pd.read_excel(input_file, sheet_name=input_sheet or 0)
        print(f"Loaded {len(input_df)} rows from input file")

        template_xl = pd.ExcelFile(template_file)
        template_sheet_name = template_sheet or template_xl.sheet_names[0]
        template_df = pd.read_excel(template_file, sheet_name=template_sheet_name)
        template_columns = list(template_df.columns)
        print(f"Template has {len(template_columns)} columns")

        input_columns = list(input_df.columns)

        worked_user_col = _pick_column(input_columns, ["Worked User"])
        summary_col = _pick_column(input_columns, ["Summary"])
        parent_col = _pick_column(input_columns, ["Parent"])
        key_col = _pick_column(input_columns, ["Key"])

        if not all([worked_user_col, summary_col, parent_col, key_col]):
            missing = [
                name
                for name, col in {
                    "Worked User": worked_user_col,
                    "Summary": summary_col,
                    "Parent": parent_col,
                    "Key": key_col,
                }.items()
                if col is None
            ]
            raise ValueError(f"Missing required input columns: {', '.join(missing)}")

        if len(input_columns) < 9:
            raise ValueError(
                "Input does not have columns H and I (8th and 9th columns)."
            )

        month_columns = [input_columns[7], input_columns[8]]

        month_col = _pick_column(template_columns, ["Month", "A - Month"], 0)
        name_col = _pick_column(template_columns, ["Name"])
        desc_col = _pick_column(template_columns, ["Desc", "Q - Desc", "Description"])
        parent_task_col = _pick_column(
            template_columns, ["Parent Task", "Z - Parent Task"], 25
        )
        project_id_col = _pick_column(
            template_columns, ["Project ID", "Project Id", "N - Project ID"], 13
        )
        hours_col = _pick_column(
            template_columns,
            ["Billable Effort", "Hours", "Time Spent", "Time Spent (h)"],
        )

        for name, col in {
            "Month": month_col,
            "Name": name_col,
            "Desc": desc_col,
            "Parent Task": parent_task_col,
            "Project ID": project_id_col,
        }.items():
            if col is None:
                raise ValueError(f"Missing required template column: {name}")

        transformed_rows = []
        for _, row in input_df.iterrows():
            for month_column in month_columns:
                hours_value = row.get(month_column)
                if pd.isna(hours_value) or hours_value == 0:
                    continue

                month_label = _format_month_label(month_column)
                new_row = {col: "" for col in template_columns}
                new_row[month_col] = month_label
                new_row[name_col] = row[worked_user_col]
                new_row[desc_col] = row[summary_col]
                new_row[parent_task_col] = row[parent_col]
                new_row[project_id_col] = row[key_col]
                if hours_col:
                    new_row[hours_col] = hours_value

                transformed_rows.append(new_row)

        result_df = pd.DataFrame(transformed_rows, columns=template_columns)
        print(f"Created {len(result_df)} rows of transformed data")

        with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
            result_df.to_excel(writer, sheet_name=template_sheet_name, index=False)

        print(f"Successfully saved transformed data to: {output_file}")
        print("\nSample of transformed data:")
        print(result_df.head())
        return result_df

    except Exception as e:
        print(f"Error during transformation: {e}")
        return None

def main() -> None:
    base_dir = "/Users/anthonywaiguru/Documents/TimeLogAutomation/Jira Automation"
    input_file = os.path.join(base_dir, "EXPORT_DECTOJAN2026.xlsx")
    template_file = os.path.join(base_dir, "Template_Jira_DPO.xlsx")
    output_file = os.path.join(
        base_dir, "Template_Jira_DPO_Populated.xlsx"
    )

    if len(sys.argv) >= 3:
        input_file = sys.argv[1]
        template_file = sys.argv[2]
    if len(sys.argv) >= 4:
        output_file = sys.argv[3]

    if not os.path.exists(input_file):
        print(f"Error: Input file not found: {input_file}")
        return

    if not os.path.exists(template_file):
        print(f"Error: Template file not found: {template_file}")
        return

    print("Excel Time Log Transformer")
    print("=" * 50)

    examine_excel_structure(input_file)
    examine_excel_structure(template_file)

    result = transform_data(input_file, template_file, output_file)

    if result is not None:
        print("\n✅ Transformation completed successfully!")
        print(f"Output file: {output_file}")
    else:
        print("\n❌ Transformation failed!")

if __name__ == "__main__":
    main()
