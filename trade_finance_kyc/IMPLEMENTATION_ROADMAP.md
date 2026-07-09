# Trade Finance KYC Platform - Implementation Roadmap

**Version:** 1.0  
**Date:** July 2026

---

## 1. Product Delivery Strategy

The recommended path is to deliver a secure MVP for one or more trade finance tenants on shared infrastructure, while preserving clean paths toward:
- richer approval workflows
- stronger compliance controls
- premium tenant isolation
- automation such as OCR and document intelligence

The MVP should optimize for:
- fast merchant onboarding
- secure document collection
- reliable reviewer notification
- clear approval and resubmission flows

---

## 2. Recommended Technology Stack

### 2.1 Primary Recommendation

| Layer | Choice | Notes |
|------|--------|-------|
| Frontend | `Next.js` | Good for authenticated portals, server actions, and flexible routing |
| Backend API | `NestJS` | Clean modular architecture, guards, queues, DTOs, and enterprise-friendly patterns |
| Database | `PostgreSQL` | Strong relational support and future row-level security options |
| Object Storage | `AWS S3` | Signed URL support, lifecycle rules, KMS integration |
| Queue and Jobs | `SQS` plus worker service | Good fit for notifications, scans, and asynchronous processing |
| Auth | `Auth0` or `AWS Cognito` | Faster secure setup than custom auth |
| Email | `SES`, `Postmark`, or `SendGrid` | Transactional notifications |
| Malware Scanning | Worker-based ClamAV or managed equivalent | Keeps files safe before review |
| Infrastructure | Docker plus Terraform or similar IaC | Promotes consistency across environments |

### 2.2 Why This Stack

This stack is a strong fit because it supports:
- modular service boundaries
- scalable file-heavy workflows
- secure auth for both internal and merchant users
- low-friction integration with cloud storage and queues
- future movement toward event-driven and service-based growth

### 2.3 Acceptable Alternatives

If the team prefers Python:
- `FastAPI` can replace `NestJS`
- the rest of the architecture can remain the same

If the team wants tighter AWS alignment:
- `Cognito`, `S3`, `SQS`, `Lambda` workers, and `RDS PostgreSQL` form a cohesive cloud-native variant

---

## 3. MVP Scope

### 3.1 Must Include

- tenant setup and tenant-aware configuration
- merchant onboarding and account invitation
- internal staff login and merchant login
- secure submission request creation
- request-specific secure links for external submitters
- upload of KYC and trade-related documents to object storage
- submission checklist and progress tracking
- reviewer queue with manual approve, reject, and resubmission decisions
- email and in-app notifications
- append-only audit logging
- malware scan workflow before reviewer download

### 3.2 Should Exclude for MVP

- mobile app
- OCR extraction
- AI document validation
- configurable workflow builder
- dedicated infrastructure per tenant
- complicated multi-step approval chains
- sanctions screening and compliance data integrations

### 3.3 UX Surfaces in MVP

The MVP should expose three focused experiences:
- tenant operations portal
- merchant portal
- external submitter portal

Each experience should have a narrow purpose and minimal unnecessary navigation.

---

## 4. Phased Rollout Plan

### Phase 1 - Foundation

Build the platform baseline:
- tenant model and tenant-aware auth
- organization and user management
- request and document data model
- private object storage integration
- secure upload and download path

### Phase 2 - Workflow MVP

Build the business workflow:
- merchant invite and onboarding
- request creation and document checklist
- external submitter invitation flow
- submission states and reviewer queue
- approve, reject, and resubmission actions

### Phase 3 - Hardening and Launch Readiness

Operationalize the MVP:
- malware scanning
- audit screens
- email delivery and retry handling
- dashboard metrics for pending work
- staging and production infrastructure
- seed data and operator playbooks

### Phase 4 - Scale Extensions

Expand after validation:
- expiry reminders
- configurable document templates
- maker-checker review
- tenant branding
- premium isolation
- OCR and analytics

---

## 5. Suggested Feature Backlog

### 5.1 Foundation Workstreams

| Workstream | Deliverables |
|-----------|--------------|
| Identity | Auth provider integration, role model, invitations, password or SSO flows |
| Tenancy | Tenant-aware middleware, scoping, seed bootstrap |
| Storage | Signed upload URLs, object metadata writeback, lifecycle tagging |
| Audit | Event emitter, append-only store, query screens |

### 5.2 Workflow Workstreams

| Workstream | Deliverables |
|-----------|--------------|
| Merchant Onboarding | Merchant organization creation, user invitation, profile completion |
| Submission Requests | Request creation, checklist, participant assignment |
| Document Handling | Upload UI, validations, malware scanning, version replacement |
| Review | Pending queue, document previews, decision capture, comments |
| Notifications | Email templates, in-app feed, retry strategy |

---

## 6. API Surface Recommendation

Suggested API domains:
- `/auth`
- `/tenants`
- `/organizations`
- `/users`
- `/submission-requests`
- `/required-documents`
- `/document-assets`
- `/reviews`
- `/notifications`
- `/audit-events`

Keep file transfer separate from metadata writes:
- backend issues signed upload URLs
- frontend uploads directly to object storage
- backend receives completion callback or client confirmation and updates metadata

---

## 7. Deployment Recommendation

### 7.1 Environment Layout

Use at minimum:
- `local`
- `staging`
- `production`

Each environment should have:
- separate database
- separate object storage bucket or clear environment prefixes
- separate auth application configuration
- separate email and queue configuration

### 7.2 Infrastructure Notes

- keep APIs stateless
- run workers separately from API nodes
- centralize secrets management
- use IaC for bucket policies, queues, databases, and IAM
- enable object storage lifecycle and versioning policies where appropriate

---

## 8. Success Metrics

The first launch should be measured using:
- average time from request creation to completed submission
- percentage of submissions completed without support intervention
- reviewer turnaround time
- number of resubmission cycles per request
- failed upload rate
- audit completeness for sensitive operations

These metrics will help decide whether to invest next in UX improvements, review automation, or compliance tooling.

---

## 9. Launch Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Weak tenant scoping | Severe | Enforce tenant-aware data access in every repository and endpoint |
| Complex external user experience | High | Use verified magic links and simplified request-only flows |
| Unsafe file uploads | High | Malware scanning and signed object storage access only |
| Operational confusion during review | Medium | Clear queue states and request-level comments |
| Scope bloat | High | Hold AI, OCR, and custom workflow features until post-MVP |

---

## 10. Immediate Next Artifacts

The next practical deliverables after this roadmap should be:
1. wireframes for tenant admin, merchant, and external submitter flows
2. a product requirements document with acceptance criteria
3. a technical backlog organized by frontend, backend, infrastructure, and security
4. an initial database schema and API contract draft
