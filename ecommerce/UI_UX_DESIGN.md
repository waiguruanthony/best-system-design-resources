# Malqia Brand — UI/UX Design Guidelines

**Version:** 1.0  
**Date:** February 2025  
**Reference:** Ikojn-inspired, top-tier beauty/fashion benchmarks, mobile-first

---

## 1. Design Philosophy

**Inspired by Ikojn, but uniquely Malqia:**
- Clean, product-focused layouts (Ikojn strength)
- Enhanced mobile experience (71% of beauty shoppers use mobile for research)
- Distinct brand identity: typography, palette, and layout that feel premium without copying
- Keyword: **trust, accessibility, fast**

---

## 2. Ikojn vs Top-Tier Beauty Sites: Comparison & Improvements

### 2.1 What Ikojn Does Well (Keep)

| Element | Ikojn | Keep |
|--------|-------|------|
| Sectioned homepage | Featured collections, themed carousels | ✓ |
| Product cards | Image, name, price, badges (New, Sale, Sold Out) | ✓ |
| Quick buy / Add to Cart | Clear CTAs | ✓ |
| Category navigation | Mega-menu style, Dresses/Tops/Bottoms | ✓ |
| Social proof | "600+ 5 star reviews" | ✓ |
| Newsletter signup | Simple, benefit-driven | ✓ |
| Footer structure | Contact, Company, Customer Care | ✓ |

### 2.2 Where Ikojn Falls Short & How to Improve

| Area | Ikojn Gap | Malqia Improvement |
|------|-----------|--------------------|
| **Mobile hamburger** | Standard only | Sticky, full-height overlay with smooth animations |
| **Product imagery** | Single primary image | Multiple images, quick-view on hover/tap, zoom on product page |
| **Touch targets** | Some small buttons | Minimum 44×44px for taps (Apple HIG) |
| **Loading states** | Often minimal | Skeletons, spinners, progressive image loading |
| **Trust badges** | Limited | M-Pesa, secure checkout, delivery, returns |
| **Search** | Basic | Predictive search, recent searches, category filters |
| **Sticky elements** | Minimal | Sticky "Add to Cart" on product page when scrolled |
| **WhatsApp/Chat** | None | Floating WhatsApp button (Malqia differentiator) |

### 2.3 Top-Tier Benchmarks (Sephora, Glossier, Fenty)

| Practice | Application for Malqia |
|----------|-------------------------|
| **Large hero imagery** | Full-width hero with overlay text, clear CTA |
| **Product-first** | Product imagery dominates; minimal clutter |
| **Accessible contrast** | WCAG AA minimum (4.5:1 text) |
| **Fast perceived load** | Above-the-fold content first; lazy-load below |
| **Trust above fold** | Free shipping, M-Pesa, returns visible early |
| **Sticky add-to-cart** | On product page when user scrolls past fold |
| **Quick-view modal** | See product details without leaving list |
| **Breadcrumbs** | Home > Category > Product |
| **Size/colour selectors** | Large, tappable on mobile |

---

## 3. Responsive Breakpoints & Mobile-First

### 3.1 Breakpoints

| Breakpoint | Width | Layout Notes |
|------------|-------|---------------|
| **Mobile** | &lt; 640px | Single column, stacked nav, full-width images |
| **Tablet** | 640px – 1024px | 2-col product grid, collapsed mega-menu |
| **Desktop** | &gt; 1024px | 3–4 col grid, full mega-menu |

### 3.2 Mobile-First Principles

1. **Design for 375px first** (iPhone SE), scale up.
2. **Touch-friendly**: 44×44px minimum tap targets.
3. **Thumb zone**: Primary CTAs in lower half on mobile.
4. **No hover-dependent UX** on mobile; use tap.
5. **Bottom nav or sticky CTA** for "Add to Cart" on long product pages.
6. **Reduce form fields** on checkout (auto-detect country, etc.).

### 3.3 Key Mobile UX Patterns

| Page | Mobile Pattern |
|------|----------------|
| **Home** | Hero → Featured (horizontal scroll) → Collections grid |
| **Product list** | 2-column grid, swipeable filters |
| **Product detail** | Image gallery (swipe), sticky "Add to Cart" bar |
| **Cart** | Full-width cards, clear quantity controls |
| **Checkout** | Single column, collapsible sections, payment icons visible |

---

## 4. Malqia Brand Visual Identity (Suggested)

### 4.1 Typography

| Use | Font | Fallback |
|-----|------|----------|
| Headings | Playfair Display, Cormorant, or DM Serif Display | serif |
| Body | Inter, Outfit, or Nunito Sans | sans-serif |
| Accent / CTAs | Same as body, semibold | — |

*Avoid generic fonts (e.g. generic sans) to differentiate from Ikojn.*

### 4.2 Color Palette (Example — Customize for Malqia)

| Role | Hex | Use |
|------|-----|-----|
| Primary | #1a1a2e (dark) or brand color | Nav, footer, buttons |
| Secondary | #e8d5b7 (warm neutral) | Accents, badges |
| Background | #faf9f7 | Page background |
| Text | #2d2d2d | Body text |
| Text Muted | #6b6b6b | Secondary text |
| Success | #2d6a4f | Confirmations, in stock |
| Sold Out | #9d0208 | Sold-out badge |
| Sale | #d00000 | Discount badges |

### 4.3 Spacing & Layout

- **Container max-width:** 1280px (content), 1440px (full-bleed sections).
- **Grid:** 12 columns, 24px gutter.
- **Section padding:** 48px mobile, 64px tablet, 80px desktop (vertical).

---

## 5. Component Specifications

### 5.1 Product Card

| Element | Spec |
|---------|------|
| Image | 1:1 or 3:4 aspect ratio, rounded corners (8px) |
| Badges | Sale (red), New (dark), Sold Out (grey overlay) |
| Title | 2 lines max, truncate with ellipsis |
| Price | Current price bold; compare-at strikethrough |
| CTA | "Add to Cart" or "Quick View" full-width on hover/tap |
| Hover | Subtle scale (1.02) or shadow |

### 5.2 Header

| Element | Desktop | Mobile |
|---------|---------|--------|
| Logo | Left | Centered or left |
| Nav | Horizontal, mega-menu | Hamburger, full-screen overlay |
| Search | Icon, expands on click | In overlay or top bar |
| Cart | Icon + count | Icon + count |
| Height | 64–80px | 56–64px |

### 5.3 Footer

- 4 columns desktop; stacked mobile.
- Links: About, Contact, Shipping, Returns, Size Guide.
- Social icons.
- Newsletter (inline or stacked).
- Copyright, policy links.

---

## 6. WhatsApp Floating Button — Specification

### 6.1 Purpose

- **Quick assistance** — Customer can contact Malqia Brand for support or questions.
- **Pre-filled greeting** — Opens chat with a standard welcome and prompt.

### 6.2 Placement

| Position | Spec |
|----------|------|
| **Location** | Bottom-right corner |
| **Offset** | 24px from bottom, 24px from right |
| **Desktop** | Fixed, always visible |
| **Mobile** | Fixed, above fold; consider 16px offset on smaller screens |
| **Z-index** | High (e.g. 9999) so it floats above all content |

### 6.3 Design

| Property | Value |
|----------|-------|
| **Size** | 56×56px (mobile), 60×60px (desktop) |
| **Icon** | WhatsApp logo (official green) |
| **Background** | #25D366 (WhatsApp green) |
| **Shadow** | `0 4px 12px rgba(37, 211, 102, 0.4)` |
| **Shape** | Circle |
| **Hover** | Slight scale (1.05), brighter shadow |

### 6.4 Pre-filled Message

**Default text (configurable in Settings/Filament):**

```
Thank you for contacting Malqia Brand! How can we help you today?
```

**Alternative (generic):**

```
Hi! I'd like to know more about Malqia Brand products.
```

**With context (optional — from product page):**

```
Hi! I'm interested in [Product Name]. Could you help me with sizing or availability?
```

### 6.5 URL Format

```
https://wa.me/254XXXXXXXXX?text=Thank%20you%20for%20contacting%20Malqia%20Brand!%20How%20can%20we%20help%20you%20today?
```

- **Phone:** International format, no + or spaces (e.g. `254712345678`).
- **Text:** URL-encoded (spaces → `%20`).

### 6.6 Implementation (Blade Component)

```html
{{-- WhatsApp Floating Button - Partial: resources/views/components/whatsapp-float.blade.php --}}
<a href="https://wa.me/{{ config('services.whatsapp.number') }}?text={{ urlencode(config('services.whatsapp.message')) }}"
   target="_blank"
   rel="noopener noreferrer"
   class="fixed bottom-6 right-6 z-[9999] flex h-14 w-14 items-center justify-center rounded-full bg-[#25D366] text-white shadow-lg transition hover:scale-105 hover:shadow-xl md:h-16 md:w-16"
   aria-label="Chat with Malqia Brand on WhatsApp">
    <svg class="h-8 w-8 md:h-9 md:w-9" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
        <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
    </svg>
</a>
```

### 6.7 Configuration

**`.env`:**
```
WHATSAPP_NUMBER=254712345678
WHATSAPP_MESSAGE="Thank you for contacting Malqia Brand! How can we help you today?"
```

**`config/services.php` (add to array):**
```php
'whatsapp' => [
    'number' => env('WHATSAPP_NUMBER', ''),
    'message' => env('WHATSAPP_MESSAGE', 'Thank you for contacting Malqia Brand! How can we help you today?'),
],
```

**Blade:** Use `config('services.whatsapp.number')` and `config('services.whatsapp.message')`.

### 6.8 Optional Enhancements

| Enhancement | Description |
|------------|-------------|
| **Tooltip** | "Chat with us" on hover (desktop) |
| **Pulse animation** | Subtle pulse to draw attention (first visit) |
| **Hide on checkout** | Avoid distraction during payment |
| **Context-aware message** | On product page, include product name in pre-fill |
| **Hours badge** | "We reply within 2 hours" under button (optional) |

---

## 7. Page-Level UX Checklist

### 7.1 Homepage

- [ ] Full-width hero with CTA
- [ ] Featured products (horizontal scroll on mobile)
- [ ] Trust badges (M-Pesa, Free delivery, Returns)
- [ ] Collections grid
- [ ] Newsletter signup
- [ ] Social proof (reviews count)
- [ ] WhatsApp button visible

### 7.2 Product Listing

- [ ] Filters (category, price) — slide-out on mobile
- [ ] Sort (newest, price)
- [ ] Product grid (2 col mobile, 3–4 col desktop)
- [ ] Sold-out badge
- [ ] Clear "View" / "Add to Cart"

### 7.3 Product Detail

- [ ] Image gallery (swipe on mobile)
- [ ] Sticky "Add to Cart" when scrolled
- [ ] Size guide link
- [ ] Breadcrumbs
- [ ] Share / WhatsApp (optional)
- [ ] Related products
- [ ] WhatsApp button for "Questions? Chat with us"

### 7.4 Cart & Checkout

- [ ] Clear item list, quantity controls
- [ ] Order summary (sticky on desktop)
- [ ] Payment icons (M-Pesa, Card)
- [ ] Progress indicator (Cart → Info → Payment)
- [ ] WhatsApp button (or hide during payment step)

---

## 8. Accessibility

- **Contrast:** WCAG AA (4.5:1 text, 3:1 large text).
- **Focus states:** Visible keyboard focus (outline, ring).
- **Alt text:** All product images.
- **Labels:** All form inputs.
- **Skip link:** "Skip to main content" for keyboard users.

---

## 9. Performance

- **Images:** WebP, lazy-load, responsive `srcset`.
- **Above-fold:** Critical CSS inline or loaded first.
- **Fonts:** `font-display: swap` to avoid FOIT.
- **Tap delay:** Remove 300ms delay on mobile (touch-action).

---

## 10. Document References

- [ARCHITECTURE.md](./ARCHITECTURE.md)
- [MODULES_AND_TASKS.md](./MODULES_AND_TASKS.md)
- [WhatsApp Click-to-Chat](https://faq.whatsapp.com/general/chats/how-to-use-click-to-chat)
- [Baymard Ecommerce UX](https://baymard.com/research/health-and-beauty)
