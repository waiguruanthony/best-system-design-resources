# Ecommerce Platform — Modules and Task Breakdown

**Version:** 1.0  
**Date:** February 2025  
**Reference:** [ARCHITECTURE.md](./ARCHITECTURE.md)

---

## Module Overview

| # | Module | Description | Priority |
|---|--------|--------------|----------|
| 1 | **Foundation** | Laravel setup, config, base layout | P0 |
| 2 | **Database & Models** | Migrations, Eloquent models | P0 |
| 3 | **Product Catalog** | Products, categories, images, sold-out | P0 |
| 4 | **Content Management** | Editable pages, homepage sections | P0 |
| 5 | **Admin Panel** | Filament setup, CRUD for products & pages | P0 |
| 6 | **Cart** | Session/DB cart, add/remove/update | P0 |
| 7 | **Checkout** | Checkout flow, payment method selection | P0 |
| 8 | **M-Pesa Integration** | Daraja STK Push, Paybill, callbacks | P0 |
| 9 | **Stripe Integration** | Checkout redirect, webhooks | P0 |
| 10 | **Orders** | Order creation, status, thank-you | P0 |
| 11 | **Frontend Polish** | Ikojn-inspired UI, responsive, sold-out badges | P1 |
| 12 | **Deployment** | GoDaddy setup, env, callbacks | P1 |

---

## Module 1: Foundation

**Goal:** Project scaffold, base configuration, layout structure.

| Task ID | Task | Deliverable | Depends On |
|---------|------|-------------|------------|
| 1.1 | Create Laravel project | `composer create-project laravel/laravel` | — |
| 1.2 | Install Tailwind CSS | `tailwind.config.js`, build pipeline | 1.1 |
| 1.3 | Install Alpine.js | Via CDN or npm | 1.1 |
| 1.4 | Create base layout (header, footer, nav) | `resources/views/layouts/app.blade.php` | 1.2 |
| 1.5 | Configure `.env.example` placeholders | Daraja, Stripe, Till, MPESA_STK_TIMEOUT_SECONDS, WhatsApp | 1.1 |
| 1.6 | Set app locale/timezone (Africa/Nairobi) | `config/app.php` | 1.1 |
| 1.7 | Create home route and view | `/` → homepage placeholder | 1.4 |

---

## Module 2: Database & Models

**Goal:** Schema and Eloquent models for products, orders, pages, payments.

| Task ID | Task | Deliverable | Depends On |
|---------|------|-------------|------------|
| 2.1 | Migration: `categories` | id, name, slug, parent_id, timestamps | 1.1 |
| 2.2 | Migration: `products` | id, name, slug, description, price, compare_at_price, sku, stock_quantity, is_sold_out, is_active, category_id, timestamps | 1.1 |
| 2.3 | Migration: `product_images` | id, product_id, path, is_primary, sort_order, timestamps | 2.2 |
| 2.4 | Migration: `carts` (optional, if DB cart) | id, session_id, timestamps | 1.1 |
| 2.5 | Migration: `cart_items` | id, cart_id, product_id, quantity, timestamps | 2.4 |
| 2.6 | Migration: `orders` | id, order_number, customer_email, customer_phone, subtotal, shipping, total, payment_method, payment_status, stripe_session_id, mpesa_checkout_id, mpesa_customer_receipt, status, timestamps | 1.1 |
| 2.7 | Migration: `order_items` | id, order_id, product_id, quantity, unit_price, total_price, timestamps | 2.6 |
| 2.8 | Migration: `pages` | id, title, slug, content, meta_title, meta_description, is_published, timestamps | 1.1 |
| 2.9 | Migration: `mpesa_transactions` | id, order_id, mpesa_request_id, receipt_number, amount, phone, status, raw_response, timestamps | 2.6 |
| 2.10 | Migration: `settings` (key-value) | id, key, value, timestamps | 1.1 |
| 2.11 | Create Eloquent models with relationships | Category, Product, Order, OrderItem, Page, MpesaTransaction | 2.1–2.10 |
| 2.12 | Add `order_number` generation (e.g., ORD-YYYYMMDD-XXX) | Order model / observer | 2.11 |

---

## Module 3: Product Catalog

**Goal:** Product listing, detail view, categories, sold-out logic.

| Task ID | Task | Deliverable | Depends On |
|---------|------|-------------|------------|
| 3.1 | ProductController: index (catalog) | List products by category, pagination | 2.11 |
| 3.2 | ProductController: show (product detail) | Single product by slug | 2.11 |
| 3.3 | Sold-out logic: derive from `stock_quantity` or `is_sold_out` | Helper / accessor on Product | 2.11 |
| 3.4 | Product card partial (image, name, price, sold-out badge) | `_product-card.blade.php` | 1.4, 3.3 |
| 3.5 | Disable "Add to Cart" when sold out | Frontend conditional | 3.4 |
| 3.6 | Category filtering / category page | Route, controller, view | 2.1, 3.1 |
| 3.7 | Product image display (primary + gallery) | Blade partial | 2.3 |

---

## Module 4: Content Management (Pages)

**Goal:** Editable pages (About, Shipping, etc.), content upload, quick modification.

| Task ID | Task | Deliverable | Depends On |
|---------|------|-------------|------------|
| 4.1 | Page model + migration (already in 2.8) | — | — |
| 4.2 | PageController: show by slug | Dynamic page route | 2.11 |
| 4.3 | Route: `/{slug}` for CMS pages | Match slugs from `pages` table | 4.2 |
| 4.4 | Page view template (title, content, meta) | `pages/show.blade.php` | 4.2 |
| 4.5 | Homepage as special page or sections | Config or `pages` with slug `home` | 4.2 |
| 4.6 | Support for image upload in page content | Filament RichEditor + media or base64 | Module 5 |
| 4.7 | Caching: cache pages by slug; clear on update | Cache facade | 4.2 |

---

## Module 5: Admin Panel (Filament)

**Goal:** Admin UI for products, pages, orders; easy content modification.

| Task ID | Task | Deliverable | Depends On |
|---------|------|-------------|------------|
| 5.1 | Install Filament | `composer require filament/filament` | 1.1 |
| 5.2 | Create Filament admin user | `php artisan make:filament-user` | 5.1 |
| 5.3 | Product resource (CRUD) | Filament ProductResource | 2.11 |
| 5.4 | Product form: name, slug, description, price, stock, images, category | Form schema | 5.3 |
| 5.5 | Product: sold-out toggle or stock-based badge in table | `is_sold_out` or `stock_quantity` display | 5.3 |
| 5.6 | Page resource (CRUD) | Filament PageResource | 2.11 |
| 5.7 | Page form: title, slug, content (RichEditor), meta, is_published | Form schema | 5.6 |
| 5.8 | Order resource (read-only or manage status) | Filament OrderResource | 2.11 |
| 5.9 | Category resource | Filament CategoryResource | 2.1 |
| 5.10 | Image upload for products | Spatie Media or Filament FileUpload | 5.4 |
| 5.11 | Settings page (optional) | Site name, contact, etc. | 2.10 |

---

## Module 6: Cart

**Goal:** Add to cart, update quantity, remove, persist (session or DB).

| Task ID | Task | Deliverable | Depends On |
|---------|------|-------------|------------|
| 6.1 | CartService: add, remove, update, getItems | Service class | 2.11 |
| 6.2 | CartController: add, remove, update | HTTP handlers | 6.1 |
| 6.3 | Cart storage: session-based | `session('cart')` or DB with session_id | 6.1 |
| 6.4 | Cart view (cart page) | List items, quantities, totals | 6.2 |
| 6.5 | Cart icon with count in header | Partial, Alpine.js or Livewire | 1.4, 6.1 |
| 6.6 | Prevent adding sold-out items to cart | Validation in CartService | 3.3 |

---

## Module 7: Checkout

**Goal:** Checkout flow, collect details, route to M-Pesa (STK or Till) or Stripe.

| Task ID | Task | Deliverable | Depends On |
|---------|------|-------------|------------|
| 7.1 | CheckoutController: show checkout form | Email, phone, address (if needed) | 6.1 |
| 7.2 | Checkout view: payment method selector (M-Pesa / Card) | Radio or tabs | 7.1 |
| 7.3 | Checkout view: M-Pesa sub-options (STK vs Till) | When M-Pesa selected, show two choices with brief descriptions | 7.2 |
| 7.4 | Checkout view: STK flow — phone input (shown when STK selected) | Conditional form; only for STK | 7.3 |
| 7.5 | Order creation: create Order + OrderItems from cart | OrderService | 2.11, 6.1 |
| 7.6 | Payment routing: M-Pesa STK → trigger STK; M-Pesa Till → redirect to Till page; Card → Stripe | CheckoutController | 7.5, Modules 8–9 |
| 7.7 | "Waiting for payment" view (M-Pesa STK only) | Poll order status; show timer; on timeout → offer Till flow | Module 8 |
| 7.7a | Waiting page: "STK didn't complete? Pay via Till instead" link | Fallback when STK fails (timeout, cancel, etc.) | Module 8 |
| 7.8 | Till payment page (for Till chosen upfront OR STK fallback) | Route: checkout/mpesa-till/{order}; Till details + receipt form | Module 8 |
| 7.9 | Success URL for Stripe redirect | Route, thank-you page | Module 9 |
| 7.10 | Clear cart after successful payment | CartService | 7.5 |

---

## Module 8: M-Pesa Integration (Daraja)

**Goal:** Two M-Pesa options (STK and Till); STK with Till fallback on failure; C2B callbacks; receipt verification.

| Task ID | Task | Deliverable | Depends On |
|---------|------|-------------|------------|
| 8.1 | Install `savannabits/daraja` | Composer package | 1.1 |
| 8.2 | MpesaService: config from .env, token generation | Service class | 8.1 |
| 8.3 | MpesaService: stkPush(orderId, amount, phone) | STK Push request | 8.2 |
| 8.4 | STK Push: try/catch + configurable timeout (MPESA_STK_TIMEOUT_SECONDS) | Handle timeout, API errors, user cancel (STK relies on PIN entry before timeout) | 8.3 |
| 8.5 | On STK failure: redirect to Till page | Same Till page for STK fallback or Till chosen upfront | 8.4 |
| 8.6 | Till payment view: display Till number, Account (order_number), Amount, instructions | Blade view (used for Till upfront + STK fallback) | 8.5 |
| 8.7 | Till view: receipt input form + Verify Payment action | Form to submit M-Pesa receipt number | 8.6 |
| 8.8 | Store user-submitted receipt in orders.mpesa_customer_receipt | PaymentController::verifyTillPayment | 8.7 |
| 8.9 | Register C2B validation/confirmation URLs with Daraja for Till | Artisan command or setup | 8.2 |
| 8.10 | Route: POST /api/mpesa/stk-callback (STK Push callback) | Callback endpoint | 8.1 |
| 8.11 | Route: POST /api/mpesa/c2b-callback (Till/Paybill callback) | C2B callback endpoint | 8.9 |
| 8.12 | STK callback handler: parse response, find order, mark paid | PaymentController | 8.10 |
| 8.13 | C2B callback handler: match BillRefNumber to order_number, verify amount, mark paid | PaymentController | 8.11 |
| 8.14 | Verification logic: when user submits receipt, check if C2B already received; else pending | Match callback to stored receipt | 8.8, 8.13 |
| 8.15 | Callbacks: return proper JSON ack to Safaricom | Response format | 8.12, 8.13 |
| 8.16 | Settings: Till number (settings or .env) | Configurable Till for Till flow | 8.6 |
| 8.17 | Sandbox testing (STK, Till, STK→Till fallback) | Test credentials, simulate | 8.4, 8.13 |

---

### M-Pesa Flow Summary

| User Choice | Flow |
|-------------|------|
| **STK** | Phone → STK Push → Success or failure |
| **STK fails** (timeout, cancel, error) | Offer Till flow (same Till page) |
| **Till (upfront)** | Skip STK; go directly to Till page with order details |

---

## Module 9: Stripe Integration

**Goal:** Redirect to Stripe Checkout, webhook, mark order paid.

| Task ID | Task | Deliverable | Depends On |
|---------|------|-------------|------------|
| 9.1 | Install `stripe/stripe-php` | Composer package | 1.1 |
| 9.2 | StripeService: createCheckoutSession(order, successUrl, cancelUrl) | Service method | 9.1 |
| 9.3 | Session metadata: order_id for webhook | Pass order_id in metadata | 9.2 |
| 9.4 | Route: POST /api/stripe/webhook (public, no CSRF) | Webhook endpoint | 9.1 |
| 9.5 | Webhook handler: verify signature, handle `checkout.session.completed` | PaymentController | 9.4 |
| 9.6 | Webhook: find order by metadata, mark paid | Order update | 9.5 |
| 9.7 | Success redirect: /checkout/success?session_id=xxx | Route, view | 7.7 |
| 9.8 | Idempotency: avoid duplicate payment processing | Check existing payment status | 9.6 |

---

## Module 10: Orders

**Goal:** Order confirmation, thank-you page, order details.

| Task ID | Task | Deliverable | Depends On |
|---------|------|-------------|------------|
| 10.1 | Order creation from cart (already in 7.4) | — | — |
| 10.2 | Thank-you / success page | Order summary, order number | 7.7, 7.9 |
| 10.3 | Decrement product stock on order paid | Observer or service | 2.11, 8.6, 9.6 |
| 10.4 | Handle insufficient stock edge case | Validation before checkout | 7.4 |
| 10.5 | Order email (optional) | Mail notification | P2 |

---

## Module 11: Frontend Polish

**Goal:** Ikojn-inspired design, responsive, sold-out badges.

| Task ID | Task | Deliverable | Depends On |
|---------|------|-------------|------------|
| 11.1 | Homepage layout: hero, featured products, collections | Ikojn-style sections | 1.4, 3.1 |
| 11.2 | Product grid: cards with image, name, price, sold-out badge | Styling | 3.4 |
| 11.3 | Sold-out badge component | Visible when sold out | 3.5 |
| 11.4 | Mobile-responsive navigation | Hamburger, dropdowns | 1.4 |
| 11.5 | Category nav / mega-menu style | Ikojn-inspired | 2.1 |
| 11.6 | Footer: links, contact, newsletter placeholder | Footer partial | 1.4 |
| 11.7 | Loading states, error handling | UX polish | Various |
| 11.8 | WhatsApp floating button (bottom-right, fixed) | Link to wa.me with pre-filled message | 1.4 |
| 11.9 | WhatsApp config: number + message in settings/.env | "Thank you for contacting Malqia Brand! How can we help you today?" | 11.8 |

---

## Module 12: Deployment

**Goal:** GoDaddy-compatible deployment, env, callbacks.

| Task ID | Task | Deliverable | Depends On |
|---------|------|-------------|------------|
| 12.1 | Ensure callback URLs are public HTTPS | Daraja, Stripe webhook config | 8.4, 9.4 |
| 12.2 | `.env` production: Daraja live credentials | Config | 8.2 |
| 12.3 | `.env` production: Stripe live keys | Config | 9.2 |
| 12.4 | GoDaddy: PHP 8.2+, MySQL | Hosting setup | — |
| 12.5 | Document deployment steps | README or DEPLOYMENT.md | 12.4 |
| 12.6 | Queue worker for async (optional) | Supervisor or cron | P2 |

---

## Dependency Graph (Simplified)

```
Module 1 (Foundation) ─┬─► Module 2 (DB/Models)
                       ├─► Module 4 (Content) ─► Module 5 (Admin)
                       ├─► Module 3 (Products) ─► Module 6 (Cart)
                       │                          │
                       │                          └─► Module 7 (Checkout) ─┬─► Module 8 (M-Pesa)
                       │                                                    └─► Module 9 (Stripe)
                       │                                                    │
                       │                                                    └─► Module 10 (Orders)
                       └─► Module 11 (Frontend)
```

---

## Suggested Implementation Order

### Phase 1: Core (P0)
1. Foundation (1.1–1.7)  
2. Database & Models (2.1–2.12)  
3. Admin Panel – Products & Pages (5.1–5.11)  
4. Product Catalog (3.1–3.7)  
5. Content Management (4.1–4.7)  
6. Cart (6.1–6.6)  
7. Checkout skeleton (7.1–7.4)  
8. M-Pesa Integration (8.1–8.9)  
9. Stripe Integration (9.1–9.8)  
10. Orders (10.1–10.4)  
11. Checkout completion (7.6–7.10)  

### Phase 2: Polish (P1)
12. Frontend Polish (11.1–11.7)  
13. Deployment (12.1–12.5)  

---

## Content Modification Quick Reference

| Content Type | Where to Edit | How |
|--------------|---------------|-----|
| Products | Filament Admin → Products | Add/edit name, price, images, stock, sold-out |
| Categories | Filament Admin → Categories | Add/edit categories |
| Static pages | Filament Admin → Pages | Rich text editor, meta, publish toggle |
| Homepage | Filament Admin → Pages (slug: home) or Settings | Edit sections / content |
| Sold-out | Product edit: set `stock_quantity = 0` or `is_sold_out = true` | One click |

---

## Sold-Out Flow Summary

1. **Admin:** Set `stock_quantity = 0` or toggle `is_sold_out` in Filament.  
2. **Model:** Product accessor or scope: `isAvailable()` = `!is_sold_out && stock_quantity > 0`.  
3. **Catalog:** Product card shows "Sold Out" badge when `!isAvailable()`.  
4. **Add to Cart:** Disabled or hidden for sold-out products.  
5. **Cart/Checkout:** Revalidate stock before payment; reject if sold out.
