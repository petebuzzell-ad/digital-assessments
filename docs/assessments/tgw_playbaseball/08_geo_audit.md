# GEO (Generative Engine Optimization) Audit

## Summary
**playbaseball.com** provides clear hierarchical content and accessible Schema markup. **tgw.com** has limited AI crawler visibility due to CSR and missing heading structures.

## Comparative Analysis

### 1. LLM Readability
LLMs require clear heading hierarchies (H1 -> H2 -> H3) and high text density.

| Metric             | tgw.com (Legacy)        | playbaseball.com (Modern) | Advantage |
| :----------------- | :---------------------- | :------------------------ | :-------- |
| **Home Structure** | ❌ 0 H1s / 0 H2s (Empty) | ✅ **1 H1 / 15 H2s**       | Modern    |
| **PLP Structure**  | ❌ 0 H1s / 0 H2s         | ✅ **1 H1 / 6 H2s**        | Modern    |
| **PDP Structure**  | ❌ 0 H1s / 0 H2s         | ✅ **1 H1 / 7 H2s**        | Modern    |
| **Text Density**   | ⚠️ Low (~0.8%)           | ✅ **High (2.4% - 4.7%)**  | Modern    |

> [!IMPORTANT]
> `tgw.com` appears empty to AI crawlers due to heavy JavaScript rendering. **playbaseball.com** serves structured HTML immediately.

### 2. Schema.org Markup
Structured data helps LLMs understand entities (products, prices, reviews).

| Feature            | tgw.com (Legacy)     | playbaseball.com (Modern)    | Advantage   |
| :----------------- | :------------------- | :--------------------------- | :---------- |
| **Product Schema** | ⚠️ Present (CSR Only) | ✅ **Present (SSR Friendly)** | Modern      |
| **Breadcrumbs**    | ✅ Present            | ❌ Missing/Not Detected       | Legacy      |
| **Organization**   | ❌ Missing            | ❌ Missing                    | ❌ Both Fail |

> [!NOTE]
> Product Schema on **playbaseball.com** is SSR/embedded, ensuring AI agents can read product data without JS.

### 3. Brand Authority Signals
Signals that help LLMs associate the domain with a trusted entity.

*   **tgw.com**: Strong legacy footprint. "About Us" and "Contact" pages are easily found, but lack `Organization` schema.
*   **playbaseball.com**: Weaker signals. No `Organization` schema. Social links are present but the brand entity is less defined in the Knowledge Graph.

## Key Findings

### Modern Platform Wins
1.  Universal readability: clear H1/H2 structure across all page types
2.  Accessible Schema: Product Schema visible without JS

### Legacy Site Failures
1.  Requires full browser engine to render structure
2.  Empty or image-based H1s provide no semantic value

## Recommendations
1.  Add Organization schema to homepage
2.  Fix PLP H1s to reflect category (e.g., "Baseball Bats")
3.  Maintain SSR Product Schema implementation
