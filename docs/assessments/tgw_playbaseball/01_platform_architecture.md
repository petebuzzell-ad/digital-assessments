# Platform Architecture Comparison

| Feature                 | tgw.com (Legacy Reference)                                                           | playbaseball.com (Replatformed)                                                          |
| :---------------------- | :----------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------- |
| **Platform Indicators** | **IBM WebSphere Commerce**<br>(`WC_SESSION_ESTABLISHED`, `WC_ACTIVEPOINTER` cookies) | **CommerceTools (Headless)**<br>(Confirmed via architecture diagram. No legacy cookies.) |
| **Frontend Framework**  | **Dojo** + **jQuery 2.1.1**                                                          | **AngularJS 1.8.2** + **jQuery 3.5.1**                                                   |
| **Visual Design**       | Identical Layout & Structure                                                         | Identical Layout & Structure                                                             |
| **Architecture**        | Monolithic (WebSphere)                                                               | **Composable / MACH**<br>(CommerceTools Backend + Custom .NET Head)                      |
| **Session Cookies**     | `WC_...` (WebSphere)                                                                 | `osano_...`, `rxVisitor...` (No standard platform session cookie visible)                |

## Detailed Findings

### 1. Legacy Baseline: tgw.com
*   Platform: IBM WebSphere Commerce (confirmed via `WC_` cookies)
*   Tech Stack: Dojo + jQuery 2.1.1

### 2. Replatformed Site: playbaseball.com
*   Platform: CommerceTools (headless backend)
*   Implementation: "Strangler Fig" approach - frontend ported to ASP.NET MVC (`TsgMvc`) as API consumer
*   Tech Stack: AngularJS 1.8.2 frontend, CommerceTools backend
*   Key Difference: No WebSphere cookies despite identical look/feel

## Architecture Diagram Analysis
*   Backend: CommerceTools (headless, API-driven)
*   Multi-site: Shared cart between **playbaseball.com** and **playsoftball.playbaseball.com** (single CommerceTools project)
*   Frontend: AngularJS 1.8.2 (outdated)
*   Integration: Server-side proxy (BFF pattern) secures API keys

## Technical Deep Dive

### 1. Frontend Architecture
*   Framework: AngularJS 1.8.2 (EOL, security risk)
*   Library: jQuery 3.5.1
*   Rendering: Client-Side Rendering (CSR) - minimal semantic HTML, heavy JS injection

### 2. Backend & API
*   Platform: CommerceTools (headless)
*   Integration: Server-side proxy (BFF) - no direct API calls visible, secures API keys
*   Session: TGW uses WebSphere cookies; PlayBaseball uses stateless/token-based (no monolithic session cookie)

### 3. Infrastructure
*   CDN: Cloudflare
*   Hosting: Likely Azure (ASP.NET MVC stack)

## Conclusion
**playbaseball.com** successfully migrated to CommerceTools while preserving legacy UI. Frontend remains technically "legacy" (AngularJS 1.8.2) despite modern backend.
