# Trade Finance KYC Platform - Jira, Git, and Deployment Traceability

**Version:** 1.0  
**Date:** July 2026

---

## 1. Purpose

This document defines how the project should be tracked in Jira so work can be traced from:
- idea
- requirement
- Jira epic or story
- branch
- commit
- pull request
- deployment
- release note

The goal is to make delivery auditable and operationally clear from the first sprint.

---

## 2. Recommended Jira Project Model

Create one Jira Software project for the product, for example:

- Project Name: `Trade Finance KYC Platform`
- Project Key: `TFKYC`

Recommended issue hierarchy:

| Level | Use |
|------|-----|
| Epic | Major business capability such as Merchant Onboarding or Document Review |
| Story | User-facing or business-deliverable slice of work |
| Task | Engineering, infrastructure, security, or documentation work |
| Sub-task | Small execution items under a story or task |
| Bug | Defect against expected behavior |

---

## 3. Recommended Epic Structure

Suggested initial epics:

| Epic Key Example | Epic Name |
|------------------|-----------|
| `TFKYC-EP1` | Tenant Foundation and Identity |
| `TFKYC-EP2` | Merchant Onboarding |
| `TFKYC-EP3` | Submission Request Workflow |
| `TFKYC-EP4` | Secure Document Upload and Storage |
| `TFKYC-EP5` | Review Queue and Approval Workflow |
| `TFKYC-EP6` | Notifications and Audit Logging |
| `TFKYC-EP7` | Security and Compliance Controls |
| `TFKYC-EP8` | Reporting, Dashboards, and Extensions |

---

## 4. Workflow Recommendation

Recommended Jira workflow states:

| Status | Meaning |
|--------|---------|
| `Backlog` | Scoped but not yet prioritized |
| `Selected for Refinement` | Under analysis or design |
| `Ready for Development` | Acceptance criteria complete |
| `In Progress` | Engineering work has started |
| `In Review` | PR open or awaiting review |
| `Ready for QA` | Merged and deployed to test environment |
| `Done` | Accepted and released |
| `Blocked` | Waiting on dependency or decision |

Use required fields before moving to `Ready for Development`:
- description
- acceptance criteria
- linked epic
- owner
- security or compliance impact flag

---

## 5. Git Branch Naming Convention

Every branch should include the Jira key.

Recommended format:

```text
feature/TFKYC-123-merchant-invite-flow
fix/TFKYC-212-signed-url-expiry-bug
chore/TFKYC-305-add-audit-indexes
docs/TFKYC-099-prd-and-wireframes
```

This gives automatic linkage in Jira when the Jira key appears in:
- branch names
- commit messages
- pull request titles

---

## 6. Commit and PR Conventions

### 6.1 Commit Format

Recommended commit message pattern:

```text
TFKYC-123 add merchant invitation workflow
```

### 6.2 Pull Request Format

Recommended PR title:

```text
TFKYC-123 Add merchant invitation workflow
```

Recommended PR body sections:
- Summary
- Jira Link
- Test Plan
- Security Impact
- Deployment Notes

Example Jira link:

```text
Jira: https://your-domain.atlassian.net/browse/TFKYC-123
```

---

## 7. Deployment Traceability

To tie Jira to deployments, each environment release should reference included Jira keys.

### 7.1 Recommended Environments

- `dev`
- `staging`
- `production`

### 7.2 Deployment Metadata

Each deployment should capture:
- deployment timestamp
- git SHA
- branch or tag
- included Jira issues
- deployed environment
- operator or pipeline identity

### 7.3 Release Tag Pattern

Recommended tags:

```text
release/2026-07-09.1
release/2026-07-16.2
```

Release notes should list:
- included Jira tickets
- notable security changes
- schema or infrastructure changes
- rollback notes

---

## 8. CI/CD Integration Recommendations

To make Jira, Git, and deployments work together cleanly:

1. Connect the GitHub repository to Jira.
2. Ensure branches and PRs always include the Jira issue key.
3. Use PR checks for tests, linting, and security scans.
4. Configure deployment automation to post deployment status back to Jira.
5. Use release notes or changelogs grouped by Jira issue key.

If using GitHub Actions, the pipeline should:
- validate PRs
- deploy to staging after merge
- optionally require approval before production
- annotate deployments with commit SHA and Jira issues

---

## 9. Ticket Templates

### 9.1 Story Template

```text
Title:
As a <user type>, I want <goal>, so that <business value>.

Description:
<Problem, context, and proposed behavior>

Acceptance Criteria:
- [ ] ...
- [ ] ...

Security / Compliance Notes:
<Any special requirements>

Dependencies:
<Linked issues or blockers>
```

### 9.2 Task Template

```text
Title:
<Technical or documentation task>

Goal:
<Expected outcome>

Definition of Done:
- [ ] Code or document completed
- [ ] Linked PR opened
- [ ] Tests or verification completed
- [ ] Deployment notes added if needed
```

---

## 10. Recommended Labels and Fields

Suggested labels:
- `security`
- `compliance`
- `multi-tenant`
- `merchant-portal`
- `review-workflow`
- `documents`
- `infra`
- `mvp`

Suggested custom fields:
- `Security Impact`
- `Compliance Impact`
- `Tenant Facing`
- `Deployment Notes Required`

---

## 11. Suggested First Backlog Slice

Start Jira with these epics and sample stories:

### Epic: Tenant Foundation and Identity
- `TFKYC-1` Create tenant-aware auth model
- `TFKYC-2` Define roles and access guard rules
- `TFKYC-3` Integrate managed auth provider

### Epic: Merchant Onboarding
- `TFKYC-10` Create merchant organization flow
- `TFKYC-11` Send merchant admin invite
- `TFKYC-12` Merchant accepts invite and completes profile

### Epic: Secure Document Upload and Storage
- `TFKYC-20` Generate signed upload URLs
- `TFKYC-21` Persist document metadata
- `TFKYC-22` Add malware scanning worker

### Epic: Review Queue and Approval Workflow
- `TFKYC-30` Create reviewer dashboard
- `TFKYC-31` Add approve, reject, and resubmission actions
- `TFKYC-32` Emit audit events for review actions

---

## 12. Definition of Done

No Jira issue should move to `Done` unless:
- implementation or documentation is complete
- Jira issue key is linked in branch or PR history
- review is complete
- test or verification notes are present
- deployment status is recorded if applicable
- release impact is understood

---

## 13. Practical Recommendation

For this project, Jira should be the system of record for:
- scope
- delivery status
- acceptance criteria
- security-sensitive decisions
- deployment traceability

GitHub should be the system of execution, and deployments should feed status back into Jira for complete end-to-end visibility.
