# Performance & Accessibility Audit

## Summary
Lab tests show slow legacy load times (>30s), but CrUX data shows real users experience ~2.4s. **playbaseball.com** outperforms legacy in both lab (PLP 5x faster) and field metrics (85% vs 78% Good LCP). Accessibility consistently better on modern platform.


## Comparative Analysis

### 1. Performance (Lab Data)
*Out of 100*

| Metric                  | Page | tgw.com (Legacy) | playbaseball.com (Modern) | Delta            |
| :---------------------- | :--- | :--------------- | :------------------------ | :--------------- |
| **Overall Score**       | Home | **27**           | **25**                    | 🔻 -2             |
|                         | PLP  | **26**           | **36**                    | ✅ +10            |
|                         | PDP  | **27**           | **29**                    | ✅ +2             |
| **LCP (Load)**          | Home | 35.7s            | 18.5s                     | ✅ 2x Faster      |
|                         | PLP  | 31.0s            | 5.9s                      | ✅ **5x Faster**  |
|                         | PDP  | 34.5s            | 20.8s                     | ✅ 40% Faster     |
| **TBT (Interactivity)** | Home | 5,260ms          | 3,910ms                   | ✅ 25% Better     |
|                         | PLP  | 5,210ms          | 1,200ms                   | ✅ **77% Better** |
|                         | PDP  | 3,020ms          | 1,640ms                   | ✅ 45% Better     |

> [!NOTE]
> LCP measures loading (target: <2.5s). TBT measures responsiveness (lower is better).

### 2. Field Data (CrUX)
*Phone, Nov 2025*

| Metric                  | tgw.com (Legacy) | playbaseball.com (Modern) | Winner                     |
| :---------------------- | :--------------- | :------------------------ | :------------------------- |
| **LCP (Load)**          | 2.4s (78% Good)  | **2.1s (85% Good)**       | ✅ Modern (Slight Edge)     |
| **INP (Interactivity)** | 175ms (88% Good) | **171ms (89% Good)**      | ✅ Modern (Tie/Slight Edge) |
| **CLS (Stability)**     | 0.00 (95% Good)  | **0.00 (96% Good)**       | 🤝 Tie (Excellent)          |

> [!IMPORTANT]
> Lab vs Field discrepancy: Lab shows ~30s LCP, field shows ~2s. Lab simulates slow 4G and waits for network idle. Real users see content in 2.1-2.4s, but resource-heavy code drains battery/data.

### 3. Competitive Landscape (CrUX)
*Mobile, Last 28 Days*

**Golf Vertical (PLP Speed)**
| Site                      | LCP (Load) | INP (Interactivity) | Status      |
| :------------------------ | :--------- | :------------------ | :---------- |
| **Dick's Sporting Goods** | **1.2s** 🚀 | 152ms               | 🟢 Excellent |
| **Golf Galaxy**           | 1.7s       | 195ms               | 🟢 Good      |
| **Rock Bottom Golf**      | 2.3s       | 145ms               | 🟡 Fair      |
| **Worldwide Golf Shops**  | 2.8s       | 120ms               | 🟡 Fair      |
| **tgw.com (Legacy)**      | **3.4s**   | 202ms               | 🔴 Lagging   |

**Baseball Vertical (PLP Speed)**
| Site                 | LCP (Load) | INP (Interactivity) | Status |
| :------------------- | :--------- | :------------------ | :----- |
| **Better Baseball**  | **2.0s** 🟢 | 149ms               | 🟢 Good |
| **playbaseball.com** | 2.2s       | **105ms** 🚀         | 🟡 Fair |
| **Baseball Monkey**  | 3.1s       | 145ms               | 🔴 Poor |

#### Analysis
*   TGW is 3x slower than market leader (3.4s vs 1.2s)
*   **playbaseball.com** is competitive (2.2s) with best-in-class interactivity (105ms INP)

### 4. Accessibility
*Out of 100*

| Page     | tgw.com Score | playbaseball.com Score | Notes                                      |
| :------- | :------------ | :--------------------- | :----------------------------------------- |
| **Home** | 82            | **89**                 | Modern site has better semantic structure. |
| **PLP**  | 78            | **87**                 | Significant improvement in listing pages.  |
| **PDP**  | 81            | **85**                 | Consistent improvement across the funnel.  |

## Key Findings

### Critical Issues
1.  Legacy site: LCP >30s in lab tests (render-blocking resources)
2.  Modern site: Fails Core Web Vitals (LCP 18.5s on Home), likely unoptimized images/large JS bundles

### Improvements
1.  PLP performance: 5x faster (5.9s vs 31.0s LCP), 77% better interactivity
2.  Accessibility: Consistently higher scores (better semantic HTML5)

## Recommendations
1.  Optimize images: size and lazy-load hero images/banners
2.  Code splitting: review AngularJS bundle, defer non-critical scripts
3.  Monitor CrUX: lab data can be pessimistic
