# Trade Finance KYC Platform - Architecture Decisions

**Version:** 1.0  
**Date:** July 2026

---

## 1. Purpose

This document records the major architecture and governance decisions for the platform. It should be updated whenever a material technical decision affects:
- security
- tenancy
- storage
- deployment
- user identity
- workflow behavior

Each decision should ideally also map to a Jira issue.

---

## 2. Decision Log Format

Use this template for future entries:

```text
Decision ID:
Title:
Date:
Status: Proposed | Accepted | Superseded
Jira:
Context:
Decision:
Consequences:
Alternatives Considered:
```

---

## 3. Current Accepted Decisions

### ADR-001 - Use Multi-Tenant Shared Infrastructure for MVP

**Status:** Accepted  
**Context:** The product must support multiple trade finance companies without delaying the first release.

**Decision:** Use a shared application and shared database with strict tenant-aware isolation in the application layer and tenant-aware storage prefixes.

**Consequences:**
- faster time to market
- lower hosting cost
- stronger need for disciplined tenant scoping
- easy upgrade path to dedicated tenant isolation later

---

### ADR-002 - Store Documents in Object Storage, Not the Application Database

**Status:** Accepted  
**Context:** The platform will handle large and sensitive files such as KYC packets, LCs, and invoices.

**Decision:** Store document binaries in S3-compatible object storage and only store metadata in the relational database.

**Consequences:**
- better scale for file handling
- easier signed upload and download flows
- simpler retention and lifecycle policy control

---

### ADR-003 - Use Verified Magic Links for External Submitters

**Status:** Accepted  
**Context:** External counterparties need low-friction access without broad account management overhead.

**Decision:** External submitters will use verified magic links or signed time-bound access flows tied to a single request.

**Consequences:**
- simpler external user experience
- lower operational burden than permanent accounts
- requires strong token expiry, revocation, and audit controls

---

### ADR-004 - Prefer Managed Authentication Provider

**Status:** Accepted  
**Context:** Building secure auth from scratch slows delivery and increases security risk.

**Decision:** Use a managed authentication provider such as Auth0 or Cognito for internal and merchant users.

**Consequences:**
- faster secure rollout
- easier MFA adoption
- some vendor dependency

---

### ADR-005 - Keep Review Workflow Manual in MVP

**Status:** Accepted  
**Context:** The first release should optimize for delivery speed and clarity before advanced approval logic is introduced.

**Decision:** Support manual review, approval, rejection, and resubmission only in MVP.

**Consequences:**
- simpler initial implementation
- better operational learning before automation
- advanced maker-checker and routing remain phase-two items

---

## 4. Governance Rules

The following rules should govern technical changes:

- any decision affecting tenancy or security must be recorded here
- any decision with operational impact should link to Jira
- any superseded decision should remain in history rather than being deleted
- no implementation should silently diverge from accepted architecture without an updated ADR

---

## 5. Review Cadence

Review architecture decisions:
- at the start of each major implementation phase
- before production launch
- when a compliance or enterprise customer requirement changes the model

---

## 6. Decisions Likely Needed Next

These are likely future ADR candidates:
- whether to use row-level security in PostgreSQL
- whether premium tenants get dedicated buckets or databases
- whether to implement maker-checker separation before production
- whether OCR should be synchronous or asynchronous
- whether tenant branding is stored in app config or a dedicated branding service
