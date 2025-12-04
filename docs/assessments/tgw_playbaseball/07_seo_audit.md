# SEO Audit

## Summary
**tgw.com** outperforms **playbaseball.com** in technical SEO (92 vs 77). Modern sites missing image alt text and XML sitemap. Meta tags and canonicals are valid.

## Comparative Analysis

### 1. Lighthouse SEO Scores
*Out of 100*

| Page Type | tgw.com (Legacy) | playbaseball.com (Modern) | playsoftball... (Modern) |
| :-------- | :--------------- | :------------------------ | :----------------------- |
| **Home**  | 🟢 **92**         | 🟠 77                      | 🟠 77                     |
| **PLP**   | 🟢 **92**         | 🟠 77                      | 🟠 77                     |
| **PDP**   | 🟢 **92**         | *Failed*                  | 🟠 77                     |

### 2. Technical Checks

| Feature         | tgw.com                    | playbaseball.com     | Status                      |
| :-------------- | :------------------------- | :------------------- | :-------------------------- |
| **Robots.txt**  | ✅ Valid (Standard)         | ✅ Valid (Cloudflare) | Both functional.            |
| **XML Sitemap** | ✅ Present (`/sitemap.xml`) | ⚠️ **Non-Standard**   | Found at custom path.       |
| **Meta Title**  | ✅ Optimized                | ✅ Optimized          | Both Good.                  |
| **Meta Desc**   | ✅ Present                  | ✅ Present            | Both Good.                  |
| **Canonical**   | ✅ Correct                  | ✅ Correct            | Both Good.                  |
| **Image Alt**   | ✅ Present                  | ❌ **Missing**        | 🔴 **SEO & Access. Penalty** |

## Key Findings

### Critical Issues (Modern Platform)
1.  Sitemaps exist but not linked in robots.txt (`/content/BBS_google_sitemap_indexV2.xml`, `/content/SBS_google_sitemap_indexV2.xml`)
2.  Missing alt text on informational graphics (trust signals, UI elements) and no aria-label fallback
3.  Robots.txt blocks faceted search but lacks discoverable sitemap

### Legacy Site Strengths
*   Mature SEO setup: proper sitemap, alt text, consistent meta data

## Recommendations
1.  Generate XML sitemap and link in robots.txt
2.  Automate alt text from product names
3.  Monitor GSC for indexing issues
