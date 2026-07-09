# Trade Finance KYC Platform - Modules and Tasks

**Version:** 1.0  
**Date:** July 2026  
**Reference:** [ARCHITECTURE.md](./ARCHITECTURE.md), [DATA_MODEL.md](./DATA_MODEL.md), [SECURITY.md](./SECURITY.md)

---

## 1. Module Overview

| # | Module | Description | Priority |
|---|--------|-------------|----------|
| 1 | Foundation and Tenancy | Project setup, auth base, tenant scoping, environment setup | P0 |
| 2 | Organizations and Users | Tenant, merchant, counterparty, and user management | P0 |
| 3 | Submission Requests | Request creation, checklists, participant assignment | P0 |
| 4 | Document Storage and Upload | Signed uploads, metadata persistence, malware scanning | P0 |
| 5 | Review Workflow | Reviewer queue, comments, approval, rejection, resubmission | P0 |
| 6 | Notifications and Audit | Email and in-app notifications, append-only audit trail | P0 |
| 7 | Merchant and External Portals | Merchant dashboard and secure external submitter journey | P0 |
| 8 | Security Hardening | MFA, retention, advanced controls, compliance posture | P1 |
| 9 | Reporting and Extensions | Dashboards, reminders, configurable templates, analytics | P1 |

---

## 2. Module 1 - Foundation and Tenancy

**Goal:** Establish the application skeleton, auth foundation, and strict tenant-aware access.

| Task ID | Task | Deliverable |
|---------|------|-------------|
| 1.1 | Create frontend and backend project skeletons | Base app structure |
| 1.2 | Integrate managed authentication provider | Login, logout, invitation support |
| 1.3 | Define core roles | `tenant_admin`, `reviewer`, `merchant_admin`, `merchant_user`, `external_submitter` |
| 1.4 | Add tenant-aware middleware or guards | Every request scoped by `tenant_id` |
| 1.5 | Configure environment separation | Local, staging, production settings |
| 1.6 | Set up shared design system and layout shells | Tenant portal, merchant portal, submitter portal base |

---

## 3. Module 2 - Organizations and Users

**Goal:** Support tenant-owned organizations and their users.

| Task ID | Task | Deliverable |
|---------|------|-------------|
| 2.1 | Create `tenants` model and migration | Tenant table and bootstrap flow |
| 2.2 | Create `organizations` model and migration | Merchant and counterparty organizations |
| 2.3 | Create `users` and organization membership mapping | User and organization relationships |
| 2.4 | Build merchant invitation flow | Merchant admin invitation and acceptance |
| 2.5 | Build merchant profile completion flow | Basic merchant KYC profile fields |
| 2.6 | Build internal reviewer management | Reviewer invitation and role assignment |

---

## 4. Module 3 - Submission Requests

**Goal:** Define and manage KYC and trade-document requests.

| Task ID | Task | Deliverable |
|---------|------|-------------|
| 3.1 | Create `submission_requests` model and migration | Top-level workflow record |
| 3.2 | Create `document_types` and `required_documents` | Reusable document catalog and request checklist |
| 3.3 | Build request creation flow | Tenant or merchant can create request based on policy |
| 3.4 | Add participant assignment | Merchant users and external submitters tied to request |
| 3.5 | Implement submission state machine | `draft` through `archived` |
| 3.6 | Build request details page | Checklist, history, participants, status |

---

## 5. Module 4 - Document Storage and Upload

**Goal:** Securely upload, store, and validate files.

| Task ID | Task | Deliverable |
|---------|------|-------------|
| 4.1 | Create `document_assets` model and migration | File metadata records |
| 4.2 | Implement signed upload URL generation | Direct-to-storage upload flow |
| 4.3 | Add upload validation | MIME, extension, and file-size enforcement |
| 4.4 | Persist upload completion metadata | File record linked to checklist item |
| 4.5 | Add malware scan worker | Scan state transitions |
| 4.6 | Implement signed download flow | Authorized reviewer and merchant downloads |
| 4.7 | Support document replacement | New versions without destructive overwrite |

---

## 6. Module 5 - Review Workflow

**Goal:** Give internal tenant teams a controlled review process.

| Task ID | Task | Deliverable |
|---------|------|-------------|
| 5.1 | Create reviewer dashboard | Pending, approved, rejected, resubmission views |
| 5.2 | Build request review screen | Checklist, file previews, comments, history |
| 5.3 | Create `review_decisions` model | Approval and rejection outcomes |
| 5.4 | Add request-level and file-level comments | Reviewer feedback capture |
| 5.5 | Implement approve action | Finalize review and notify participants |
| 5.6 | Implement reject action | Close request with reason |
| 5.7 | Implement resubmission action | Reopen required items only |

---

## 7. Module 6 - Notifications and Audit

**Goal:** Track and communicate every important workflow event.

| Task ID | Task | Deliverable |
|---------|------|-------------|
| 6.1 | Create `notifications` model | Delivery tracking |
| 6.2 | Create `audit_events` model | Append-only security and workflow audit |
| 6.3 | Build event emission layer | Structured events from sensitive actions |
| 6.4 | Create email templates | Invite, submission receipt, review outcome, resubmission |
| 6.5 | Add in-app notification feed | Portal notification center |
| 6.6 | Build audit log screen | Filter by actor, resource, date, request |

---

## 8. Module 7 - Merchant and External Portals

**Goal:** Deliver focused submission experiences for non-reviewer actors.

| Task ID | Task | Deliverable |
|---------|------|-------------|
| 7.1 | Build merchant dashboard | Request status, pending actions, uploads |
| 7.2 | Build merchant request view | Checklist and upload actions |
| 7.3 | Create secure external invitation flow | Verified magic link access |
| 7.4 | Build external submitter upload page | Minimal request-scoped experience |
| 7.5 | Add submission confirmation and receipt | Final state after successful submission |
| 7.6 | Add save-and-return support | Resume unfinished submission |

---

## 9. Module 8 - Security Hardening

**Goal:** Strengthen the MVP into a more compliance-ready platform.

| Task ID | Task | Deliverable |
|---------|------|-------------|
| 8.1 | Enable MFA for internal users | Stronger access control |
| 8.2 | Add configurable retention policies | Tenant-controlled lifecycle rules |
| 8.3 | Add separation-of-duties controls | Maker-checker option |
| 8.4 | Add tenant-specific key management options | Premium security tier |
| 8.5 | Add anomaly monitoring and alerts | Suspicious activity detection |

---

## 10. Module 9 - Reporting and Extensions

**Goal:** Extend the platform after the workflow MVP is stable.

| Task ID | Task | Deliverable |
|---------|------|-------------|
| 9.1 | Dashboard metrics | Submission times, reviewer turnaround, completion rate |
| 9.2 | Configurable document templates | Per-tenant request presets |
| 9.3 | Expiry reminders | Renewal and refresh workflows |
| 9.4 | OCR and extraction | Metadata extraction from uploaded documents |
| 9.5 | Compliance integrations | Sanctions, registry, or verification providers |

---

## 11. Recommended MVP Build Order

### Phase 1
1. Module 1 - Foundation and Tenancy  
2. Module 2 - Organizations and Users  
3. Module 3 - Submission Requests  

### Phase 2
4. Module 4 - Document Storage and Upload  
5. Module 7 - Merchant and External Portals  

### Phase 3
6. Module 5 - Review Workflow  
7. Module 6 - Notifications and Audit  

### Phase 4
8. Module 8 - Security Hardening  
9. Module 9 - Reporting and Extensions  

---

## 12. MVP Acceptance Outcomes

The MVP is ready when a tenant can:
- create a merchant
- invite a merchant user
- create a request with a document checklist
- send a secure submission link
- receive uploaded files in private object storage
- review the package and request resubmission or approve it
- trace the full lifecycle through notifications and audit logs
