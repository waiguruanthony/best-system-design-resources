# Trade Finance KYC Platform - Security

**Version:** 1.0  
**Date:** July 2026

---

## 1. Security Objectives

The platform handles sensitive corporate and financial documents, so the MVP should be designed around:
- confidentiality of uploaded documents
- strong tenant separation
- controlled reviewer access
- auditable user and system activity
- secure external submission journeys
- safe handling of files from untrusted sources

---

## 2. Threat Model Summary

The main risks are:
- cross-tenant data leakage
- unauthorized access through weak invitation links
- compromised or malicious file uploads
- excessive access by internal reviewers
- insecure document downloads or overlong signed URLs
- audit gaps that make compliance investigations difficult

The MVP should aim to reduce these risks without overcomplicating the initial rollout.

---

## 3. Authentication Strategy

### 3.1 Internal and Merchant Users

Use full authenticated accounts for:
- `tenant_admin`
- `reviewer`
- `merchant_admin`
- `merchant_user`

Recommended controls:
- email plus password or enterprise SSO through a managed auth provider
- short-lived sessions with secure refresh handling
- brute-force protection and login throttling
- enforced password policy if passwords are used
- MFA support built into the provider, enabled for tenant admins in MVP if feasible

### 3.2 External Submitters

Use a secure request-specific access pattern:
- send a time-bound magic link or signed invitation URL
- require email verification before allowing upload
- bind the invitation to one submission request
- expire the link after a configurable period, such as 72 hours
- support regeneration and revocation by tenant staff

Recommended MVP choice:
- verified magic-link authentication for `external_submitter`
- no permanent external account unless product requirements expand later

This keeps the experience low-friction while still avoiding anonymous uploads.

---

## 4. Authorization Model

### 4.1 Role-Based Access

| Role | Permissions |
|------|-------------|
| `tenant_admin` | Manage tenant settings, merchants, requests, reviewers, and all submissions within tenant |
| `reviewer` | View and decide on submissions assigned within tenant |
| `merchant_admin` | Manage merchant users, track requests, upload merchant documents |
| `merchant_user` | Upload and view merchant-scoped requests only |
| `external_submitter` | Upload only to the specific request tied to an active invitation |

### 4.2 Tenant Enforcement

Every request path should verify:
- authenticated actor identity
- actor role
- actor tenant membership
- actor organization scope where applicable
- actor access to the specific request or document

Authorization should not rely on frontend filtering alone.

---

## 5. Encryption Strategy

### 5.1 Data in Transit

Protect all traffic with TLS:
- HTTPS for all browser traffic
- TLS for API calls and object storage operations
- TLS for mail provider and job service integrations

Security headers should include:
- HSTS
- secure cookie settings
- content security policy tuned to the frontend stack

### 5.2 Data at Rest

Recommended MVP baseline:
- encrypt database storage at the cloud provider level
- encrypt object storage with cloud-managed KMS-backed keys
- keep secrets in a managed secret store rather than environment files on hosts where possible

Recommended object storage posture:
- private bucket only
- no public ACLs
- access via short-lived signed URLs
- tenant-aware storage prefixes

### 5.3 Tenant-Aware Keying

Preferred progression:
1. MVP: one managed KMS policy for the platform with tenant-aware storage prefixes
2. Growth: tenant-specific encryption context and tighter IAM boundaries
3. Premium compliance tier: dedicated tenant keys or dedicated buckets

---

## 6. End-to-End Encryption Position

True end-to-end encryption is not the right MVP choice for this product because tenant reviewers must be able to read and evaluate documents.

Recommended position:
- use strong transport encryption
- use strong at-rest encryption
- optionally apply field-level encryption to highly sensitive structured data
- keep decryption inside trusted backend services for authorized reviewers only

This balances confidentiality with operational practicality.

---

## 7. Secure File Handling

### 7.1 Upload Controls

All uploaded files should pass through these controls:
- extension allowlist
- MIME type validation
- file size limits by document category
- malware scanning before reviewer download
- upload integrity verification using checksum or ETag comparison

### 7.2 Download Controls

Reviewer and merchant downloads should use:
- short-lived signed URLs
- explicit access checks before link generation
- audit event creation for every download
- optional watermarking in future phases for highly sensitive documents

### 7.3 Storage and Retention Rules

Files should:
- remain private in object storage
- be logically linked to their owning request and tenant
- support version replacement instead of destructive overwrite
- follow retention policy rules defined per tenant

---

## 8. Audit and Monitoring

### 8.1 Audit Event Requirements

Record at minimum:
- login success and failure
- invitation created, resent, revoked, and redeemed
- document uploaded, replaced, downloaded, and deleted if deletion is allowed
- request submitted
- reviewer decision issued
- status transitions
- admin role or permission changes

### 8.2 Audit Log Design

Audit logs should be:
- append-only
- timestamped with timezone
- tenant-scoped
- actor-aware
- queryable by request, user, and date range

Audit metadata should avoid storing document content itself.

### 8.3 Operational Monitoring

The platform should emit alerts for:
- repeated failed logins
- suspicious invitation redemption patterns
- malware scan failures
- repeated authorization failures
- cross-tenant access denials

---

## 9. Data Retention and Privacy

Recommended MVP policy direction:
- allow tenant-level configuration of default retention periods
- archive rather than hard-delete workflow records by default
- hard-delete documents only through controlled administrative processes
- support legal hold flags in later phases

For privacy and minimization:
- collect only metadata needed for workflow, compliance, and support
- avoid exposing full sensitive identifiers in list screens
- mask nonessential values in logs and notifications

---

## 10. Secure Notification Patterns

Email and in-app notifications should:
- avoid attaching sensitive files directly to email
- avoid exposing full document names if that increases risk
- direct users back to the authenticated portal
- use request references instead of sensitive payloads in email bodies

---

## 11. Secure Development Guardrails

The implementation team should enforce:
- tenant-aware middleware and repository patterns
- secure defaults in object storage configuration
- signed URL expiry limits
- structured audit event emission from all sensitive operations
- mandatory server-side authorization checks for every file operation
- dependency scanning and secret scanning in CI

---

## 12. MVP Security Checklist

- private object storage bucket
- KMS-backed encryption at rest
- HTTPS-only delivery
- signed upload and download URLs
- managed authentication provider
- verified magic links for external submitters
- append-only audit events
- malware scanning worker
- tenant-scoped authorization on every request
- notification flows that never include sensitive file contents

---

## 13. Phase-Two Hardening Options

After MVP, consider:
- mandatory MFA for all internal users
- reviewer assignment and separation-of-duties workflows
- IP allowlisting for internal tenant users
- tenant-specific KMS keys
- dedicated storage buckets for premium tenants
- data classification tags and retention automation
- DLP checks and OCR pipelines
