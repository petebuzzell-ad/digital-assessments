# Digital Assessment: TGW & PlayBaseball

## Executive Summary
**playbaseball.com** successfully replatformed to CommerceTools (headless backend), eliminating legacy WebSphere constraints. Frontend execution limits ROI: search discovery, SEO fundamentals, and competitive speed lag.

**Verdict**: Replatforming complete. Shift focus from engineering to experience optimization.

## Context
*   Sales down 40-60% YoY
*   ROAS floor reached - traffic growth yields diminishing returns
*   **2% Cart-to-Checkout conversion drop** (June/July 2025)
*   Policy: No optimization on legacy (**tgw.com**)

---

## TGW.com (Legacy)
**Role**: Benchmark / Cash Cow | **Status**: Maintenance Mode

Technically obsolete but functionally rich. Performance floor, feature maturity ceiling.

### Key Insights
*   **3x slower** than market leader (3.4s vs 1.2s LCP)
*   SEO maturity: proper sitemap, alt text, baseline organic visibility
*   Functional search/navigation (functional parity target)

---

## PlayBaseball.com (Modern)
**Role**: Growth Engine | **Status**: Active Development

Modern architecture, underperforming due to execution gaps.

### Assets
*   Unified architecture: multi-site shared GA4 property and cart
*   Real-world stability: CLS 0.00 (CrUX data)
*   Accessibility: 89/100 foundation

### Critical Execution Gaps
*   **Speed**: 2.1s LCP slower than all competitors (Better Baseball ~1.8s)
*   **Search**: Basic Algolia text-only vs. competitors' rich autosuggest (visuals + categories)
*   **SEO**: Missing alt text on trust signals, non-standard sitemap (invisible to crawlers)
*   **Mobile**: Desktop-first UX, small touch targets, sluggish navigation

---

## Investment Priorities

### 1. TGW.com: Revenue Protection (Policy Exception)
*   **Guest Checkout hotfix**: Address 2% conversion drop (June/July)
    *   Resolve color conflict (Free Shipping messages vs. checkout buttons)
    *   Elevate Guest Checkout path visibility
    *   High-ROI repair, not feature optimization

### 2. PlayBaseball.com: Growth
*   **SEO basics (immediate)**: Generate XML sitemap, automate alt text
*   **Search upgrade (months)**: Rich autosuggest UI for Algolia
*   **Mobile polish (months)**: Match Dick's app-like navigation

### 3. Risk Mitigation (Quarters)
*   **Frontend modernization**: Migrate from AngularJS 1.8.2 (EOL, security risk) to modern framework

## Assessment Scope
Full e-commerce funnel across 11 documents:

| Document                                                                       | Focus                                        |
| :----------------------------------------------------------------------------- | :------------------------------------------- |
| [01_platform_architecture.md](01_platform_architecture.md)                     | CommerceTools backend + ASP.NET MVC frontend |
| [02_ux_audit.md](02_ux_audit.md)                                               | Browsing, search, checkout flows             |
| [03_analytics_audit.md](03_analytics_audit.md)                                 | GA4, GTM, DataLayer                          |
| [04_security_audit.md](04_security_audit.md)                                   | AngularJS 1.8.2 EOL risk                     |
| [05_capabilities_inventory.md](05_capabilities_inventory.md)                   | Feature parity check                         |
| [06_performance_accessibility_audit.md](06_performance_accessibility_audit.md) | Lab vs. field performance, accessibility     |
| [07_seo_audit.md](07_seo_audit.md)                                             | Search visibility                            |
| [08_geo_audit.md](08_geo_audit.md)                                             | Generative Engine Optimization               |
| [09_system_inventory.md](09_system_inventory.md)                               | Stack map (Algolia confirmed)                |
| [10_mobile_audit.md](10_mobile_audit.md)                                       | Mobile UX review                             |
| [11_competitor_benchmark.md](11_competitor_benchmark.md)                       | vs. Dick's, Golf Galaxy, others              |