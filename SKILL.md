---
name: seo-engine
description: Evaluate on-page technical requirements, content basics, optimization signals, and spam-policy compliance for a single page or site. Use when asked to audit HTML, robots.txt, redirects, or dashboard configs and to produce pass/fail evidence with actionable fixes.
license: MIT
metadata:
  author: Abderrahmen Gharsallah
  version: "1.0.0"
---

# SEO Engine

Use this skill to run deterministic checks on HTML, headers, robots.txt, and related resources.
It returns pass/fail outcomes with minimal heuristics and clear remediation steps.

## When to use
- Auditing a page’s indexability and crawlability
- Verifying content structure (title, headings, links, images)
- Flagging spam policy violations (cloaking, hidden text, keyword stuffing)
- Sanity-checking redirect behavior and HTTP status
- Verifying dashboard filters/metrics for SEO reporting


## Included Rules

| Rule ID                        | Title                                             | Priority  | Category                | Description                                                                                 |
|--------------------------------|---------------------------------------------------|-----------|-------------------------|---------------------------------------------------------------------------------------------|
| PAGE_TITLE_EXISTS              | Page title tag present and non-empty              | Low       | Content Basics          | Ensures the &lt;title&gt; tag exists and is not empty.                                            |
| MAIN_HEADING_EXISTS            | Main heading (&lt;h1&gt;) present and non-empty         | Low       | Content Basics          | At least one &lt;h1&gt; element exists with non-empty text.                                       |
| IMAGE_ALT_TEXT                 | All images have non-empty alt attributes          | Medium    | Content Basics          | Every &lt;img&gt; element includes a non-empty alt attribute.                                     |
| CRAWLABLE_LINKS                | All anchor links are crawlable (have valid href)  | Low       | Content Basics          | Every &lt;a&gt; element has a non-empty href that does not start with "javascript:".              |
| GOOGLEBOT_NOT_BLOCKED          | Googlebot is not blocked by robots.txt            | High      | Technical Requirements  | No Disallow rule for Googlebot (or *) matches the page URL.                                 |
| PAGE_HTTP_200_STATUS           | Page returns HTTP 200 status                      | Critical  | Technical Requirements  | Page responds with HTTP 200, not error or redirect.                                         |
| PAGE_INDEXABLE_CONTENT         | Page has indexable textual content                | Medium    | Technical Requirements  | Body contains at least one alphanumeric character after stripping markup.                   |
| HEAD_SECTION_VALID_HTML        | Head section must be valid HTML                   | High      | Technical Requirements  | The page contains exactly one &lt;head> element and the HTML parses without syntax errors.     |
| CLOAKING_DETECTION             | Detect cloaking by comparing bot vs user content  | High      | Spam Policies           | Content served to Googlebot and regular users is substantially identical (≥ 90% similarity).|
| HIDDEN_TEXT_DETECTION          | Detect hidden text or links intended for search   | Medium    | Spam Policies           | No elements with hidden styles contain visible text or links.                               |
| KEYWORD_STUFFING_DETECTION     | Detect excessive repetition of keywords           | Medium    | Spam Policies           | No single keyword exceeds a density of 5% of total words.                                   |
| SNEAKY_REDIRECT_DETECTION      | Detect sneaky redirects for bots vs users         | High      | Spam Policies           | Both HTTP status codes and final URLs are identical for Googlebot and regular users.        |
| MALWARE_HOSTING_DETECTION      | Detect presence of known malware signatures       | Critical  | Security                | Resource's hash does not match any known malware signatures.                                |
| TITLE_DESCRIPTIVE              | Page title is descriptive, specific, and accurate | Medium    | Content Optimization    | Title text contains at least two words.                                                     |
| META_DESCRIPTION_PRESENT       | Meta description tag is present and descriptive   | Medium    | Content Optimization    | Meta description is present and its length is at least 50 characters.                       |
| IMAGE_ALT_ATTRIBUTES           | All images have descriptive alt attributes        | Medium    | Content Optimization    | Every &lt;img&gt; element has a non-empty alt attribute.                                          |
| HEADING_HIERARCHY              | Page uses heading elements for hierarchy          | Low       | Content Optimization    | At least one &lt;h1&gt; element is present.                                                       |
| GA_FILTER_SOURCE_MEDIUM        | GA data filtered to source=google, medium=organic| Medium    | Dashboard Setup         | Both source=google and medium=organic filter conditions are present in dashboard config.    |
| DASHBOARD_METRICS_PRESENT      | Dashboard includes required five metrics          | Medium    | Dashboard Setup         | All five required metrics are present in the dashboard configuration.                       |
| DASHBOARD_DATA_SOURCES_CONNECTED| Dashboard connects to GA and SC                  | Medium    | Dashboard Setup         | Both Search Console and Google Analytics data sources are referenced in dashboard config.   |
| AMP_PAGE_MUST_FOLLOW_SPEC      | AMP page must follow AMP HTML specification       | Critical  | AMP Validation          | Ensures the page complies with the AMP HTML specification for Google Search features.       |
| BANNER_DATA_NOSNIPPET_PRESENT  | Ensure banner or popup uses data-nosnippet attribute | Medium | Site Functionality      | Prevents banner or popup content from being shown in search result snippets.               |
| ROBOTS_TXT_NOT_503             | robots.txt must not return HTTP 503 status       | High      | Site Availability       | A 503 response for robots.txt blocks all crawling, preventing indexing.                     |
| RETRY_AFTER_HEADER_PRESENT_ON_503 | 503 error pages must include a Retry-After header | Medium | Site Availability       | Provides crawlers with guidance on when to retry, reducing unnecessary load.                |
| NO_URL_FRAGMENTS               | Avoid URL fragments that change content           | High      | URL Structure           | Google Search may not crawl URLs where fragments are used to change content.                |
| HYPHENS_IN_PATH                | Use hyphens to separate words in URL path        | Medium    | URL Structure           | Hyphens improve readability for users and search engines, aiding crawlability.              |
| PERCENT_ENCODING_NECESSARY     | Percent‑encode non‑ASCII characters in URLs      | Medium    | URL Structure           | Percent‑encoding ensures URLs are valid, crawlable, and correctly interpreted.              |
| CHECK_REL_CANONICAL_PRESENT    | Presence of rel="canonical" link element        | Medium    | Canonicalization        | rel="canonical" link annotations influence how Google determines the canonical URL.         |
| CHECK_URL_IN_SITEMAP           | URL presence in sitemap.xml                      | Medium    | Canonicalization        | Presence of the URL in a sitemap is a factor influencing canonical selection.               |
| CHECK_HTTP_HTTPS_CONSISTENCY   | Consistent use of HTTPS scheme                    | Low       | Canonicalization        | The page's protocol (HTTP vs HTTPS) is a factor that influences canonicalization.           |
| DATA_NOSNIPPET_VALID_HTML      | Ensure HTML containing data-nosnippet attribute is well‑formed | High | Data Nosnippet | HTML section must be valid HTML for data‑nosnippet to be machine‑readable.                 |
| ROBOTS_TXT_ALLOW_INDEXING_RULES| URLs containing robots meta or X‑Robots‑Tag must not be disallowed | Critical | Robots.txt Rules | URLs with indexing/serving rules cannot be disallowed from crawling via robots.txt.        |
| NO_CLOAKING_DETECTED           | Ensure no cloaking between Googlebot and users   | High      | A/B Testing             | Cloaking violates spam policies and can cause demotion or removal from search results.      |
| REL_CANONICAL_PRESENT          | Use rel="canonical" on test variant URLs        | Medium    | A/B Testing             | rel=canonical signals the preferred URL, preventing duplicate indexing of test variants.    |
| TEMPORARY_REDIRECT_302         | Use 302 redirects for temporary test redirects   | Medium    | A/B Testing             | A 302 redirect signals a temporary change, ensuring the original URL remains indexed.       |
| CANONICAL_LINK_IN_HEAD         | rel="canonical" link element must be placed in <head> | High | Canonicalization        | The rel="canonical" link element is only accepted if it appears in the <head> section.    |
| CANONICAL_LINK_ABSOLUTE_URL    | rel="canonical" link element must use an absolute URL | Medium | Canonicalization        | Documentation recommends using absolute URLs for rel="canonical" link elements.            |
| CANONICAL_HEADER_ABSOLUTE_URL  | rel="canonical" HTTP header must use an absolute URL | Medium | Canonicalization        | Documentation states that absolute URLs must be used in the rel="canonical" HTTP header.  |
| AVOID_ROBOTS_TXT_FOR_CANONICAL | Do not use robots.txt for canonicalization       | Low       | Canonicalization        | Documentation explicitly advises against using robots.txt for canonicalization.             |
| CONSISTENT_CANONICAL_METHOD    | Do not specify different canonical URLs using different methods | High | Canonicalization | Specifying different canonical URLs via different techniques can cause conflicts.            |


## Rule Categories and Included Rules

### Technical Requirements
- PAGE_HTTP_200_STATUS (Critical): Page returns HTTP 200 status. Ensures the page responds with HTTP 200, not error or redirect.
- GOOGLEBOT_NOT_BLOCKED (High): Googlebot is not blocked by robots.txt. No Disallow rule for Googlebot (or *) matches the page URL.
- PAGE_INDEXABLE_CONTENT (Medium): Page has indexable textual content. Body contains at least one alphanumeric character after stripping markup.
- HEAD_SECTION_VALID_HTML (High): Head section must be valid HTML. The page contains exactly one &lt;head&gt; element and the HTML parses without syntax errors.

### Spam Policies
- CLOAKING_DETECTION (High): Detect cloaking by comparing bot vs user content. Content served to Googlebot and regular users is substantially identical (≥ 90% similarity).
- HIDDEN_TEXT_DETECTION (Medium): Detect hidden text or links intended for search. No elements with hidden styles contain visible text or links.
- KEYWORD_STUFFING_DETECTION (Medium): Detect excessive repetition of keywords. No single keyword exceeds a density of 5% of total words.
- SNEAKY_REDIRECT_DETECTION (High): Detect sneaky redirects for bots vs users. Both HTTP status codes and final URLs are identical for Googlebot and regular users.

### Content Basics
- PAGE_TITLE_EXISTS (Low): Page title tag present and non-empty. Ensures the &lt;title&gt; tag exists and is not empty.
- MAIN_HEADING_EXISTS (Low): Main heading (&lt;h1&gt;) present and non-empty. At least one &lt;h1&gt; element exists with non-empty text.
- CRAWLABLE_LINKS (Low): All anchor links are crawlable (have valid href). Every &lt;a&gt; element has a non-empty href that does not start with "javascript:".
- IMAGE_ALT_TEXT (Medium): All images have non-empty alt attributes. Every &lt;img&gt; element includes a non-empty alt attribute.

### Content Optimization
- TITLE_DESCRIPTIVE (Medium): Page title is descriptive, specific, and accurate. Title text contains at least two words.
- META_DESCRIPTION_PRESENT (Medium): Meta description tag is present and descriptive. Meta description is present and its length is at least 50 characters.
- IMAGE_ALT_ATTRIBUTES (Medium): All images have descriptive alt attributes. Every &lt;img&gt; element has a non-empty alt attribute.
- HEADING_HIERARCHY (Low): Page uses heading elements for hierarchy. At least one &lt;h1&gt; element is present.

### Security
- MALWARE_HOSTING_DETECTION (Critical): Detect presence of known malware signatures. Resource's hash does not match any known malware signatures.

### Dashboard Setup
- GA_FILTER_SOURCE_MEDIUM (Medium): GA data filtered to source=google, medium=organic. Both source=google and medium=organic filter conditions are present in dashboard config.
- DASHBOARD_METRICS_PRESENT (Medium): Dashboard includes required five metrics. All five required metrics are present in the dashboard configuration.
- DASHBOARD_DATA_SOURCES_CONNECTED (Medium): Dashboard connects to GA and SC. Both Search Console and Google Analytics data sources are referenced in dashboard config.

### AMP Validation
- AMP_PAGE_MUST_FOLLOW_SPEC (Critical): AMP page must follow AMP HTML specification. Ensures the page complies with the AMP HTML specification for Google Search features.

### Site Functionality
- BANNER_DATA_NOSNIPPET_PRESENT (Medium): Ensure banner or popup uses data-nosnippet attribute. Prevents banner or popup content from being shown in search result snippets.

### Site Availability
- ROBOTS_TXT_NOT_503 (High): robots.txt must not return HTTP 503 status. A 503 response for robots.txt blocks all crawling, preventing indexing.
- RETRY_AFTER_HEADER_PRESENT_ON_503 (Medium): 503 error pages must include a Retry-After header. Provides crawlers with guidance on when to retry, reducing unnecessary load.

### URL Structure
- NO_URL_FRAGMENTS (High): Avoid URL fragments that change content. Google Search may not crawl URLs where fragments are used to change content.
- HYPHENS_IN_PATH (Medium): Use hyphens to separate words in URL path. Hyphens improve readability for users and search engines, aiding crawlability.
- PERCENT_ENCODING_NECESSARY (Medium): Percent‑encode non‑ASCII characters in URLs. Percent‑encoding ensures URLs are valid, crawlable, and correctly interpreted.

### Canonicalization
- CHECK_REL_CANONICAL_PRESENT (Medium): Presence of rel="canonical" link element. rel="canonical" link annotations influence how Google determines the canonical URL.
- CHECK_URL_IN_SITEMAP (Medium): URL presence in sitemap.xml. Presence of the URL in a sitemap is a factor influencing canonical selection.
- CHECK_HTTP_HTTPS_CONSISTENCY (Low): Consistent use of HTTPS scheme. The page's protocol (HTTP vs HTTPS) is a factor that influences canonicalization.
- CANONICAL_LINK_IN_HEAD (High): rel="canonical" link element must be placed in &lt;head&gt;. The rel="canonical" link element is only accepted if it appears in the &lt;head&gt; section.
- CANONICAL_LINK_ABSOLUTE_URL (Medium): rel="canonical" link element must use an absolute URL. Documentation recommends using absolute URLs for rel="canonical" link elements.
- CANONICAL_HEADER_ABSOLUTE_URL (Medium): rel="canonical" HTTP header must use an absolute URL. Documentation states that absolute URLs must be used in the rel="canonical" HTTP header.
- AVOID_ROBOTS_TXT_FOR_CANONICAL (Low): Do not use robots.txt for canonicalization. Documentation explicitly advises against using robots.txt for canonicalization.
- CONSISTENT_CANONICAL_METHOD (High): Do not specify different canonical URLs using different methods. Specifying different canonical URLs via different techniques can cause conflicts.

### Data Nosnippet
- DATA_NOSNIPPET_VALID_HTML (High): Ensure HTML containing data-nosnippet attribute is well‑formed. HTML section must be valid HTML for data‑nosnippet to be machine‑readable.

### Robots.txt Rules
- ROBOTS_TXT_ALLOW_INDEXING_RULES (Critical): URLs containing robots meta or X‑Robots‑Tag must not be disallowed. URLs with indexing/serving rules cannot be disallowed from crawling via robots.txt.

### A/B Testing
- NO_CLOAKING_DETECTED (High): Ensure no cloaking between Googlebot and users. Cloaking violates spam policies and can cause demotion or removal from search results.
- REL_CANONICAL_PRESENT (Medium): Use rel="canonical" on test variant URLs. rel=canonical signals the preferred URL, preventing duplicate indexing of test variants.
- TEMPORARY_REDIRECT_302 (Medium): Use 302 redirects for temporary test redirects. A 302 redirect signals a temporary change, ensuring the original URL remains indexed.

## How to Use

Read individual rule files for detailed explanations and code examples:

```
rules/PAGE_TITLE_EXISTS.md
rules/MAIN_HEADING_EXISTS.md
rules/IMAGE_ALT_TEXT.md
rules/CRAWLABLE_LINKS.md
rules/GOOGLEBOT_NOT_BLOCKED.md
rules/PAGE_HTTP_200_STATUS.md
rules/PAGE_INDEXABLE_CONTENT.md
rules/CLOAKING_DETECTION.md
rules/HIDDEN_TEXT_DETECTION.md
rules/KEYWORD_STUFFING_DETECTION.md
rules/SNEAKY_REDIRECT_DETECTION.md
rules/MALWARE_HOSTING_DETECTION.md
rules/TITLE_DESCRIPTIVE.md
rules/META_DESCRIPTION_PRESENT.md
rules/IMAGE_ALT_ATTRIBUTES.md
rules/HEADING_HIERARCHY.md
rules/GA_FILTER_SOURCE_MEDIUM.md
rules/DASHBOARD_METRICS_PRESENT.md
rules/DASHBOARD_DATA_SOURCES_CONNECTED.md
rules/HEAD_SECTION_VALID_HTML.md
rules/AMP_PAGE_MUST_FOLLOW_SPEC.md
rules/BANNER_DATA_NOSNIPPET_PRESENT.md
rules/ROBOTS_TXT_NOT_503.md
rules/RETRY_AFTER_HEADER_PRESENT_ON_503.md
rules/NO_URL_FRAGMENTS.md
rules/HYPHENS_IN_PATH.md
rules/PERCENT_ENCODING_NECESSARY.md
rules/CHECK_REL_CANONICAL_PRESENT.md
rules/CHECK_URL_IN_SITEMAP.md
rules/CHECK_HTTP_HTTPS_CONSISTENCY.md
rules/DATA_NOSNIPPET_VALID_HTML.md
rules/ROBOTS_TXT_ALLOW_INDEXING_RULES.md
rules/NO_CLOAKING_DETECTED.md
rules/REL_CANONICAL_PRESENT.md
rules/TEMPORARY_REDIRECT_302.md
rules/CANONICAL_LINK_IN_HEAD.md
rules/CANONICAL_LINK_ABSOLUTE_URL.md
rules/CANONICAL_HEADER_ABSOLUTE_URL.md
rules/AVOID_ROBOTS_TXT_FOR_CANONICAL.md
rules/CONSISTENT_CANONICAL_METHOD.md
```

Each rule file contains:
- Brief explanation of why it matters
- Incorrect example with explanation
- Correct example with explanation
- Additional context and references

## Full Compiled Document

For the complete guide with all rules expanded: `rules/_sections.md`