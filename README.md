# Jira Automation

Automates population of the `Template_Jira_DPO.xlsx` from Jira time log exports.

## Files
- `excel_transformer.py` — Main script
- `requirements.txt` — Python dependencies

## Input/Output
- Input: `~/Documents/TimeLogAutomation/Jira Automation/EXPORT_DECTOJAN2026.xlsx`
- Template: `~/Documents/TimeLogAutomation/Jira Automation/Template_Jira_DPO.xlsx`
- Output: `~/Documents/TimeLogAutomation/Jira Automation/Template_Jira_DPO_Populated.xlsx`

## Mapping Rules
- Month: from columns H/I (uses those column headers as month labels)
- Name: `Worked User`
- Project ID (Column N): `Key`
- Desc (Column Q): `Summary`
- Parent Task (Column Z): `Parent`
- Hours (if present): from columns H/I values
- All other columns: left empty as not present in input

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run
```bash
python excel_transformer.py
```

## Notes
- Script expects the input and template files to exist at the paths above.
- Update paths in `excel_transformer.py` if your filenames or locations change.
