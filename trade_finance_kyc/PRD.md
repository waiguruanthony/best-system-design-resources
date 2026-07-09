# Trade Finance KYC Platform - Product Requirements Document

**Version:** 1.0  
**Date:** July 2026

---

## 1. Product Vision

Build a secure, multi-tenant platform that helps trade finance companies collect KYC and transaction-supporting documents faster, review them reliably, and track progress from request to approval.

The product should replace fragmented email-driven document collection with a controlled workflow that is auditable, scalable, and suitable for multiple finance-company tenants.

---

## 2. Problem Statement

Today, many trade finance document journeys are slow because:
- documents are requested over email or WhatsApp
- submitters do not know exactly what is required
- reviewers lack a central queue and status view
- sensitive documents are spread across inboxes and drives
- there is weak traceability from submission to approval

This creates longer turnaround times, operational risk, and poor client experience.

---

## 3. Product Goals

The MVP should:
- reduce turnaround time for KYC and trade-document submission
- give merchants and invited submitters a clear upload checklist
- store files securely in cloud object storage
- let internal teams review, approve, reject, or request resubmission
- create clear audit trails and notifications
- support more than one trade finance company through multi-tenancy

---

## 4. Non-Goals for MVP

The MVP will not initially include:
- native mobile apps
- AI document validation
- OCR extraction pipelines
- configurable workflow builders
- complex separation-of-duties logic
- dedicated infrastructure per tenant

---

## 5. Primary Users

| User | Need |
|------|------|
| Tenant Admin | Set up merchants, create requests, monitor pipeline, manage reviewers |
| Reviewer | Review submissions quickly and record decisions |
| Merchant Admin | Track requirements, coordinate internal submission, manage merchant users |
| Merchant User | Upload required documents and monitor status |
| External Submitter | Complete a limited secure request without full platform access |

---

## 6. Core Use Cases

### 6.1 Merchant Onboarding

As a tenant admin, I want to onboard a merchant and invite its primary user so that the merchant can begin submitting documents through the platform.

### 6.2 Request Creation

As a tenant admin or authorized merchant admin, I want to create a submission request with required documents so that the right party knows exactly what to provide.

### 6.3 Secure Submission

As a merchant user or external submitter, I want to upload required documents securely and submit them for review so that financing can progress.

### 6.4 Review Decision

As a reviewer, I want to inspect uploaded documents and approve, reject, or request resubmission so that only valid packages proceed.

### 6.5 Status Visibility

As a merchant user, I want to see whether my submission is pending, approved, rejected, or needs resubmission so that I know what action is required.

---

## 7. Functional Requirements

### 7.1 Tenant and Access

- The system must support multiple trade finance companies as separate tenants.
- The system must isolate tenant data in application logic and persistent storage.
- The system must support role-based access for tenant admins, reviewers, merchant admins, merchant users, and external submitters.

### 7.2 Merchant Management

- A tenant admin must be able to create a merchant organization.
- A tenant admin must be able to invite a merchant admin.
- Merchant admins must be able to manage additional merchant users, if enabled by tenant policy.

### 7.3 Submission Requests

- Authorized users must be able to create a submission request.
- Each request must support one or more required document items.
- A request must have a lifecycle state.
- A request must allow assignment of merchant users and optionally an external submitter.

### 7.4 Document Upload

- Users must be able to upload documents directly to secure object storage.
- The system must validate file type and file size.
- The system must store document metadata in the application database.
- Uploaded files must remain private and accessible only through authorized flows.

### 7.5 Review Workflow

- Reviewers must see a queue of pending submissions.
- Reviewers must be able to view uploaded documents once they pass security checks.
- Reviewers must be able to approve, reject, or request resubmission.
- Reviewer comments must be attached to the request or document where applicable.

### 7.6 Notifications

- The system must send email notifications for invites and major workflow transitions.
- The system must provide in-app notifications for authenticated users.
- The system must confirm successful submission to the relevant participants.

### 7.7 Audit

- The system must record audit events for sensitive actions.
- Audit logs must capture actor, time, action, and target resource.
- Audit logs must be tenant-scoped and append-only.

---

## 8. Non-Functional Requirements

### 8.1 Security

- All traffic must use TLS.
- Files at rest must be encrypted in object storage.
- Access to files must use short-lived signed URLs.
- External submitters must use time-bound verified access links.

### 8.2 Performance

- The system should support direct-to-storage uploads to reduce backend bottlenecks.
- Reviewer queues should load efficiently for high document volumes.
- Upload status and request status should update reliably.

### 8.3 Scalability

- The architecture should scale horizontally for stateless web and API services.
- The data model should support multiple tenants and future workflow expansion.

### 8.4 Reliability

- Notifications and scan jobs should run asynchronously with retry handling.
- Submission state transitions should be durable and auditable.

---

## 9. MVP Features

### Included

- tenant setup
- merchant onboarding
- secure document request creation
- upload of KYC and trade documents
- status tracking
- reviewer queue
- approval, rejection, and resubmission actions
- email and in-app notifications
- audit logging

### Excluded

- mobile app
- OCR and AI classification
- workflow builders
- dedicated per-tenant infrastructure
- advanced approval chains

---

## 10. Acceptance Criteria

### 10.1 Merchant Onboarding

- [ ] A tenant admin can create a merchant organization.
- [ ] A tenant admin can send an invitation to a merchant admin email.
- [ ] A merchant admin can accept the invite and access the merchant portal.

### 10.2 Request Creation

- [ ] A tenant admin can create a request with a checklist of required documents.
- [ ] A request can be assigned to a merchant and optionally an external submitter.
- [ ] The request status starts in `draft` and changes correctly as work progresses.

### 10.3 Secure Upload

- [ ] A permitted submitter can upload supported document files.
- [ ] Files are stored in private object storage and not publicly accessible.
- [ ] The system stores metadata and links each upload to the request and checklist item.

### 10.4 Submission and Review

- [ ] A submitter can complete and submit the request package.
- [ ] A reviewer can see the package in a pending review queue.
- [ ] A reviewer can approve, reject, or request resubmission.
- [ ] The request state reflects the reviewer decision.

### 10.5 Notifications

- [ ] Invite emails are sent successfully.
- [ ] Submission completion triggers notification to the tenant review team.
- [ ] Review outcomes notify relevant merchant or submitter participants.

### 10.6 Auditability

- [ ] Login, invite, upload, review, and state-change events are captured in audit logs.
- [ ] Audit events can be filtered by tenant and request.

---

## 11. Success Metrics

The MVP should be evaluated using:
- average time from request creation to completed submission
- reviewer turnaround time
- percentage of requests completed without support intervention
- number of resubmission loops per request
- upload failure rate

---

## 12. Open Product Decisions

These items may be finalized during implementation refinement:
- whether merchants can always create requests or only tenant staff can
- whether counterparties must verify via magic link only or create lightweight accounts
- whether the first release requires multiple internal review teams
- whether maker-checker approval is needed before production launch
