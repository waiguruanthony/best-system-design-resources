# Ecommerce Platform — Architecture Document

**Version:** 1.0  
**Date:** February 2025  
**Scope:** Kenya-focused ecommerce store with M-Pesa (Daraja) + Card (Stripe) payments

---

## 1. Executive Summary

A self-contained Laravel ecommerce platform with:
- **Direct M-Pesa integration** via Safaricom Daraja API (STK Push, Paybill) — no third-party gateway commission
- **Card payments** via Stripe (redirect to Stripe Checkout)
- **Content management** for pages and product catalog with easy modification
- **Sold-out support** for inventory visibility on the frontend
- **MVC architecture** with clear separation of concerns
- **Kenya-first** (KES, M-Pesa, mobile-responsive)

---

## 2. Technology Stack

| Layer | Technology |
|-------|------------|
| **Framework** | Laravel (PHP 8.2+) |
| **Frontend** | Blade, Tailwind CSS, Alpine.js |
| **Database** | MySQL 8.0+ |
| **M-Pesa** | Safaricom Daraja API (`savannabits/daraja`) |
| **Cards** | Stripe (Checkout redirect) |
| **Admin** | Filament (content & product management) |
| **Hosting** | GoDaddy (PHP + MySQL) or compatible |
| **File Storage** | Local / S3 for product images |

---

## 3. High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              CLIENT (Browser)                                    │
│  • Public storefront  • Checkout  • Payment selection (M-Pesa / Card)          │
└─────────────────────────────────────────────────────────────────────────────────┘
                                         │
                                         ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                         LARAVEL APPLICATION                                       │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │   Routes    │  │ Controllers │  │  Services   │  │   Models    │              │
│  │  (web/api)  │  │  (Logic)   │  │  (Business) │  │  (Eloquent) │              │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘              │
│         │                │                │                │                     │
│         └────────────────┴────────────────┴────────────────┘                     │
│                                  │                                                │
│  ┌─────────────────────────────────────────────────────────────────────────┐   │
│  │  Filament Admin Panel (Authenticated)                                    │   │
│  │  • Products  • Pages  • Orders  • Inventory (sold out)  • Settings         │   │
│  └─────────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────────┘
                                         │
                    ┌────────────────────┼────────────────────┐
                    ▼                    ▼                    ▼
            ┌───────────────┐   ┌───────────────┐   ┌───────────────┐
            │    MySQL      │   │  Daraja API    │   │  Stripe API   │
            │   (Primary)    │   │  (Safaricom)   │   │  (Cards)      │
            └───────────────┘   └───────────────┘   └───────────────┘
```

---

## 4. MVC Structure

### 4.1 Directory Layout

```
app/
├── Http/
│   ├── Controllers/
│   │   ├── CheckoutController.php      # Checkout flow, payment routing
│   │   ├── PaymentController.php      # M-Pesa callbacks, Stripe webhooks
│   │   ├── ProductController.php      # Catalog, product detail
│   │   ├── CartController.php         # Cart CRUD
│   │   ├── PageController.php         # CMS pages (About, etc.)
│   │   └── HomeController.php
│   └── Middleware/
├── Services/
│   ├── MpesaService.php               # Daraja STK Push, callback parsing
│   ├── StripeService.php              # Checkout Session, webhook handling
│   ├── CartService.php
│   └── OrderService.php
├── Models/
│   ├── Product.php
│   ├── Order.php
│   ├── OrderItem.php
│   ├── Cart.php / CartItem.php
│   ├── Page.php                        # CMS pages
│   ├── MpesaTransaction.php
│   └── ...
└── ...

resources/
├── views/
│   ├── layouts/
│   ├── pages/                         # CMS-backed pages
│   ├── products/
│   ├── cart/
│   ├── checkout/
│   └── ...
└── ...

database/migrations/
```

### 4.2 Layer Responsibilities

| Layer | Responsibility | Examples |
|-------|----------------|----------|
| **View** | Presentation only; no business logic | Blade templates, partials |
| **Controller** | Request handling, validation, orchestration | CheckoutController, PaymentController |
| **Service** | Business logic, external API calls | MpesaService, StripeService |
| **Model** | Data access, relationships, attributes | Product, Order, Page |

---

## 5. Data Model

### 5.1 Core Entities

```
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│    products     │       │  product_images │       │    categories   │
├─────────────────┤       ├─────────────────┤       ├─────────────────┤
│ id              │──┐    │ id              │       │ id              │
│ name             │  │    │ product_id (FK) │       │ name            │
│ slug             │  └───►│ path            │       │ slug            │
│ description      │       │ is_primary      │       │ parent_id (FK)  │
│ price            │       └─────────────────┘       └─────────────────┘
│ compare_at_price │              ▲                          ▲
│ sku              │              │                          │
│ stock_quantity   │              │                          │
│ is_sold_out ◄────┼── Sold-out flag (derived or explicit)    │
│ is_active        │                                       │
│ category_id (FK) │───────────────────────────────────────┘
│ created_at       │
│ updated_at       │
└─────────────────┘

┌─────────────────┐       ┌─────────────────┐
│     orders      │       │   order_items   │
├─────────────────┤       ├─────────────────┤
│ id              │──┐    │ id              │
│ order_number    │  │    │ order_id (FK)   │
│ customer_email  │  └───►│ product_id (FK) │
│ customer_phone  │       │ quantity        │
│ total_amount    │       │ unit_price      │
│ payment_method  │       │ total_price     │
│ payment_status  │       └─────────────────┘
│ stripe_session_id│
│ mpesa_checkout_id│
│ mpesa_customer_receipt │  ◄── User-submitted receipt (Till fallback)
│ payment_status  │
│ status          │
│ created_at      │
└─────────────────┘

┌─────────────────┐       ┌─────────────────┐
│     pages       │       │ mpesa_transactions│
├─────────────────┤       ├─────────────────┤
│ id              │       │ id              │
│ title           │       │ order_id (FK)   │
│ slug            │       │ mpesa_request_id│
│ content (HTML)  │       │ mpesa_receipt   │
│ meta_title      │       │ amount          │
│ meta_description│       │ phone           │
│ is_published    │       │ status          │
│ created_at      │       │ raw_callback    │
│ updated_at      │       │ created_at      │
└─────────────────┘       └─────────────────┘
```

### 5.2 Sold-Out Handling

Two approaches (choose one or combine):

| Approach | Implementation | Pros | Cons |
|----------|----------------|------|------|
| **A: Explicit flag** | `products.is_sold_out` (boolean) | Simple; manual control | Must update manually |
| **B: Stock-based** | `products.stock_quantity`; sold out when = 0 | Automatic | Requires inventory tracking |
| **C: Hybrid** | Stock decrements on order; `is_sold_out` can override | Flexible | Slightly more logic |

**Recommendation:** Use **stock-based** with optional `is_sold_out` override for edge cases (e.g., reserve without selling).

- **Frontend:** Product card shows "Sold Out" badge when `stock_quantity = 0` or `is_sold_out = true`; "Add to Cart" disabled.

### 5.3 Content Pages (CMS)

| Field | Purpose |
|-------|---------|
| `title` | Page title |
| `slug` | URL (e.g., `/about`, `/shipping`) |
| `content` | Rich HTML (WYSIWYG in Filament) |
| `meta_title`, `meta_description` | SEO |
| `is_published` | Visibility toggle |

---

## 6. Payment Flows

### 6.1 M-Pesa (Two Options: STK or Till)

When the customer selects M-Pesa, they choose one of two options upfront:

| Option | Description | Best for |
|-------|-------------|----------|
| **STK Push** | Instant prompt on phone; enter PIN to pay | Fast payment when customer is ready to respond quickly |
| **Till Number** | Pay manually via M-Pesa → Till; paste receipt to verify | Customers who prefer no time pressure, or who've had STK timeout before |

**Why offer both:** STK often fails because customers must enter their PIN within the timeout window. Offering Till upfront lets users who know they're slow, or who've experienced STK timeout before, skip STK and pay via Till instead—no time limit, more reliable.

#### 6.1.1 Upfront Choice: STK vs Till

```
Customer selects M-Pesa
        │
        ▼
┌───────────────────────────────────────────────────┐
│  Choose how to pay:                               │
│  ○ STK Push – Instant prompt on your phone        │
│    (Enter PIN when prompted; may timeout if slow) │
│                                                   │
│  ○ Till Number – Pay manually, paste receipt       │
│    (No time limit; more reliable)                 │
└───────────────────────────────────────────────────┘
        │
        ├── Chose STK ──► Enter phone ──► Trigger STK Push
        │
        └── Chose Till ──► Go directly to Till instructions (skip STK)
```

#### 6.1.2 STK Flow (with Till Fallback on Failure)

STK often fails when customers don’t enter their PIN before timeout. If STK fails or cannot be confirmed, the user is offered the Till flow.

```
Customer chose STK
        │
        ▼
Enter phone (254XXXXXXXXX)
        │
        ▼
[Pay with M-Pesa]  ──►  MpesaService::stkPush()
        │                         │
        │                         ▼
        │                  Daraja API (STK Push)
        │                         │
        │                         ▼
        │                  Safaricom sends prompt to phone
        │                  (Customer must enter PIN before timeout)
        │                         │
        │                         ├── SUCCESS ──► Callback ──► Order paid ──► Thank-you page
        │                         │
        │                         └── FAILURE ──► Offer Till flow
        │                               (timeout, cancel, no callback, API error)
```

**STK failure reasons (common):**
- Customer doesn’t enter PIN in time (timeout)
- Customer cancels or ignores the prompt
- Network/API error

#### 6.1.3 Till Flow (Chosen Upfront or After STK Failure)

Same Till flow in both cases:

```
Till chosen upfront OR STK failed (timeout / cancel / error)
        │
        ▼
Show Till payment UI
        │
        ├── Display: Till Number, Account/Reference (= order_number), Amount
        │
        ├── Instructions: "Pay via M-Pesa → Paybill/Till → Enter Account number above"
        │
        ▼
User pays manually via M-Pesa app
        │
        ▼
User pastes M-Pesa receipt number (e.g. ABC12XY34Z)
        │
        ▼
[Verify Payment]  ──►  Two verification paths:
        │
        ├── Path A (automatic): C2B callback from Safaricom
        │   • Customer pays to Till with Account = order_number
        │   • Safaricom sends callback to /api/mpesa/c2b-callback
        │   • Match by BillRefNumber (order_number) + amount
        │   • Mark order paid
        │
        └── Path B (user-submitted receipt):
            • Store receipt in order / mpesa_transactions
            • If callback already received for this order → match and mark paid
            • If callback not yet received → "Verification pending" (poll or wait for callback)
            • Admin can manually verify via M-Pesa statement if callback never arrives
        │
        ▼
Order marked paid (when verified)
        │
        ▼
Thank-you page
```

#### 6.1.4 Till — Data to Display

| Field | Source | Example |
|-------|--------|---------|
| **Till Number** | `settings.till_number` or `.env` | `123456` |
| **Account / Reference** | `order.order_number` | `ORD-20250214-001` |
| **Amount (KES)** | `order.total` | `4,999.00` |

#### 6.1.5 Verification Logic

| Step | Action |
|------|--------|
| 1 | Register C2B validation/confirmation URLs with Daraja for Till |
| 2 | On Till payment, Safaricom sends callback with `BillRefNumber`, `TransAmount`, `TransID` |
| 3 | Match `BillRefNumber` to `order_number`; verify `TransAmount` |
| 4 | Mark order paid, store `MpesaTransaction` |
| 5 | If user submits receipt before callback, store it and mark `pending_till_verification` |
| 6 | When callback arrives, match and mark paid; optionally link to stored receipt |
| 7 | If callback never arrives (rare), admin uses stored receipt for manual verification |

#### 6.1.6 Configurable Timeout & Till

```
MPESA_STK_TIMEOUT_SECONDS=120   # e.g. 90–120 seconds (customer must enter PIN before this)
MPESA_TILL_NUMBER=123456        # Your Till/Paybill for Till flow
```

- For STK: start timer when STK Push is initiated
- If no callback within timeout, offer Till flow ("STK didn’t complete? Pay via Till instead")
- Customers who chose Till upfront skip STK entirely; no timeout applies

### 6.2 Card (Stripe Redirect)

```
Customer selects Card
        │
        ▼
[Pay with Card]  ──►  StripeService::createCheckoutSession()
        │                         │
        │                         ▼
        │                  Stripe API (Session)
        │                         │
        │                         ▼
        │                  Redirect to checkout.stripe.com
        │                         │
        │                         ▼
        │                  Customer completes payment
        │                         │
        │                         ▼
        │                  Redirect to success_url (your site)
        │                  + Stripe webhook  ──►  /api/stripe/webhook
        │                         │
        │                         ▼
        │                  Order marked paid
        │
        ▼
Thank-you page
```

---

## 7. Content Management

### 7.1 Editable Content Types

| Type | Storage | Editable Via |
|------|---------|--------------|
| **Products** | `products`, `product_images` | Filament Product resource |
| **Static pages** | `pages` | Filament Page resource |
| **Homepage sections** | `pages` (home) or `settings` | Filament |
| **Site settings** | `settings` (key-value) | Filament Settings page |

### 7.2 Quick Modification Strategy

1. **Filament Admin** — Single place for products, pages, orders, sold-out.
2. **WYSIWYG Editor** — Filament’s RichEditor for page content.
3. **Image Upload** — Spatie Media Library or Filament’s native upload.
4. **Caching** — Cache product catalog and pages; bust on update.

---

## 8. Security Considerations

| Concern | Mitigation |
|---------|------------|
| Card data | Never touches app; Stripe Checkout hosted |
| Webhook forgery | Verify Stripe signature, validate Daraja callbacks |
| CSRF | Laravel CSRF tokens |
| XSS | Blade escaping, sanitize HTML in pages |
| Auth | Filament for admin; no customer accounts initially |
| HTTPS | Required for Daraja callbacks, Stripe, production |

---

## 9. Deployment (GoDaddy)

- PHP 8.2+, MySQL 8.0+
- `.env` for secrets (Daraja, Stripe)
- Callback URLs: public HTTPS (Daraja, Stripe webhooks)
- Queue worker for async jobs (optional)

---

## 10. Document References

- [MODULES_AND_TASKS.md](./MODULES_AND_TASKS.md) — Module breakdown and tasks
- [Safaricom Daraja](https://developer.safaricom.co.ke/)
- [Stripe Checkout](https://stripe.com/docs/payments/checkout)
- [Filament](https://filamentphp.com/)
