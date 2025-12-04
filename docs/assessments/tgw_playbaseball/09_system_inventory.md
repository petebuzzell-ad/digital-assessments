# System Inventory & Architecture Map

## Overview
Complete ecosystem mapping for modern (**playbaseball.com**) and legacy (**tgw.com**) platforms.

## 1. Modern Platform (**playbaseball.com**)
**Architecture Type**: Composable / MACH (Microservices, API-first, Cloud-native, Headless)

| Category               | System / Provider      | Role & Notes                                                                             |
| :--------------------- | :--------------------- | :--------------------------------------------------------------------------------------- |
| **Commerce Core**      | **CommerceTools**      | The central "brain" for Product Catalog, Cart, Orders, and Customers. Headless backend.  |
| **Frontend (Head)**    | **ASP.NET MVC**        | Custom application (`TsgMvc`) serving as the frontend head. Consumes CommerceTools APIs. |
| **Frontend Framework** | **AngularJS 1.8.2**    | Legacy JavaScript framework running on the client-side.                                  |
| **Search & Merch**     | **Algolia**            | **Algolia** references (`algoliaClick`, `algoliaclickevent`) found in `global.js`.       |
| **Reviews**            | **Bazaarvoice**        | Customer ratings and reviews integration.                                                |
| **Tax**                | **Avalara**            | Real-time tax calculation at checkout.                                                   |
| **Payments**           | **Adyen**              | Modern payment gateway and processor.                                                    |
| **CDN / Security**     | **Cloudflare**         | Edge caching, WAF, and bot protection.                                                   |
| **Hosting**            | **Azure** (Implied)    | Hosting environment for the ASP.NET MVC application.                                     |
| **Analytics**          | **Google Analytics 4** | Web analytics and tracking.                                                              |
| **Marketing**          | **Meta Pixel**         | Social advertising tracking.                                                             |

## 2. Legacy Platform (**tgw.com**)
**Architecture Type**: Monolithic

| Category          | System / Provider          | Role & Notes                                                  |
| :---------------- | :------------------------- | :------------------------------------------------------------ |
| **Commerce Core** | **IBM WebSphere Commerce** | All-in-one legacy monolith (Catalog, Cart, Orders, Frontend). |
| **Frontend**      | **Dojo Toolkit**           | Legacy JavaScript library bundled with WebSphere themes.      |
| **Search**        | **Endeca**                 | Legacy Oracle search engine (known for high maintenance).     |
| **Reviews**       | **PowerReviews**           | Legacy review platform (different from the modern site).      |
| **Payments**      | **Cybersource**            | Legacy payment gateway.                                       |
| **CDN**           | **Akamai**                 | Legacy CDN provider.                                          |

## 3. Key Integration Differences

| Feature      | Legacy       | Modern      | Shift                       |
| :----------- | :----------- | :---------- | :-------------------------- |
| **Search**   | Endeca       | Algolia     | SaaS-based search           |
| **Reviews**  | PowerReviews | Bazaarvoice | Market leader consolidation |
| **Payments** | Cybersource  | Adyen       | Modern APIs                 |
| **CDN**      | Akamai       | Cloudflare  | Modern edge network         |

## 4. Data Flow
*   **BFF Pattern**: ASP.NET MVC proxies between AngularJS and CommerceTools, securing API keys
*   **Shared Services**: **playbaseball.com** and `playsoftball.playbaseball.com` share CommerceTools project, enabling shared cart
