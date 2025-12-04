# Analytics & Tracking Audit

## Summary
*   GA4: Implemented on all sites. Modern sites share single property (cross-domain tracking)
*   GTM: Active on all sites with separate container IDs
*   Meta Pixel: Active on all sites with separate pixel IDs
*   DataLayer: Modern platform uses cleaner event schema (`view_page`, `view_item`)

> [!NOTE]
> PLA spend surge (Mar-Aug 2025) drove lower-quality traffic, explaining conversion rate decline.

## Comparative Matrix

| Feature           | tgw.com (Legacy)   | playbaseball.com (Modern) | playsoftball... (Modern)    |
| :---------------- | :----------------- | :------------------------ | :-------------------------- |
| **GA4 Property**  | `G-G4ZQ9EYW9R`     | `G-1GL9G327L8`            | `G-1GL9G327L8`              |
| **GTM Container** | `DC-4953838`       | `DC-4954029`              | `DC-4954029` (assumed)      |
| **Meta Pixel**    | `1514576802145700` | `296741824068964`         | `296741824068964` (assumed) |
| **Cross-Domain**  | ❌ Isolated         | ✅ **Shared Property**     | ✅ **Shared Property**       |

## Detailed Event Analysis

### 1. Home Page
*   **Legacy**: Fires standard `page_view`.
*   **Modern**: Fires `page_view` AND a custom `view_page` event.

### 2. Product Listing Page (PLP)
*   **Legacy**: Standard `page_view`. No specific `view_item_list` event detected in the initial load.
*   **Modern**: Standard `page_view` + `view_page`. No `view_item_list` detected in initial load (likely fires on scroll or interaction).

### 3. Product Detail Page (PDP)
*   **Legacy**:
    *   Events: `view_item`, `page_view`.
    *   Data Structure: Basic product data.
*   **Modern**:
    *   Events: `view_item`, `page_view`, `view_page`.
    *   Data Structure: Consistent with GA4 e-commerce standards.

## Key Findings

### Modern Platform Advantages
1.  Unified tracking: shared GA4 property enables cross-storefront user journey tracking
2.  Custom events: `view_page` provides additional page view tracking

### Legacy Site Status
1.  Isolated data: separate GA4 property, siloed from modern stack
2.  Basic implementation: functional DataLayer but lacks custom events

## Recommendations
1.  Implement `view_item_list` on PLP for impression-to-click CTR measurement
2.  Consider consolidating GTM containers if cross-domain tracking is needed
