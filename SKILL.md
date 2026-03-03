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
- Auditing a page's indexability and crawlability  
- Verifying content structure (title, headings, links, images)
- Flagging spam policy violations (cloaking, hidden text, keyword stuffing)
- Sanity-checking redirect behavior and HTTP status
- Verifying dashboard filters/metrics for SEO reporting
- Analyzing website URLs provided by users (extracts HTML, robots.txt, and sitemap automatically)
- Analyzing existing HTML files, robots.txt files, sitemap.xml files


## Input Preparation

When provided with a website URL, use the input preparation scripts to extract all required data:

- **fetch_html.py** - Extracts HTML source code from the webpage
- **fetch_robots_txt.py** - Downloads robots.txt crawling permissions
- **fetch_sitemap.py** - Finds and downloads sitemap.xml structure

See `scripts/prepare_input/README.md` for detailed usage instructions.

## Quick Reference

### Analyze Website URL
Provide a website URL and the agent will extract all required data and run SEO analysis:
```
"Analyze https://example.com for SEO issues"
"Run SEO audit on example.com"  
"Check this website for technical SEO problems: https://site.com"
```

### Analyze Local Files
Provide local files and the agent will apply appropriate SEO rules:
```
"Analyze this HTML file for SEO compliance: page.html"
"Check these files: page.html, robots.txt"  
"What SEO issues exist in this webpage file?"
```

### Rule Information Lookup
Ask about specific rules or categories:
```
"What does the FAVICON_DIMENSIONS rule check?"
"Show me all Content Basics rules"
"Explain the PAGE_EXPERIENCE_DIVERSITY requirement"
"List all Critical priority SEO rules"
```

### File Requirements by Rule
Each rule specifies its required inputs in the YAML frontmatter:
- **inputFields.html** - Requires HTML file content
- **inputFields.robotsTxt** - Requires robots.txt file content  
- **inputFields.sitemap** - Requires sitemap.xml content

The agent automatically reads rule definitions and applies appropriate checks based on your provided files.

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
| PHP_HEADERS_BEFORE_OUTPUT      | Ensure HTTP redirect headers are sent before any body content in PHP redirects | High | Server-side redirects | The documentation states "You must set the headers before sending anything to the screen" for PHP redirects, requiring headers to precede any output. |
| NOINDEX_ON_LOGIN_PAGE          | Ensure login pages include a noindex robots meta tag | High | Edit or remove unwanted text before moving to a public file format | Login pages may expose redacted content; a noindex meta tag prevents search engines from indexing them. |
| URL_NO_EMAIL                   | URLs must not contain email addresses | Medium | Edit or remove unwanted text before moving to a public file format | Email addresses in URLs can be indexed and expose personal information. |
| IMAGE_NON_VECTOR_FORMAT        | Ensure exported images are in non-vector formats (PNG or WEBP) | Medium | Edit and export images before embedding them | Vector formats may retain hidden layers or metadata that can be indexed. |
| NOINDEX_META_TAG_PRESENT       | Presence of noindex meta tag in HTML head | Low | Implementing noindex | A &lt;meta name="robots" content="noindex"&gt; tag placed in the &lt;head&gt; prevents search engines that support the noindex rule from indexing the page. |
| FILETYPE_INDEXABLE_CHECK       | File extension is indexable by Google | Low | File types indexable by Google | Google can index the content of the listed text‑based and media file types; resources with other extensions may not be indexed. |
| REDIRECT_USES_PERMANENT_STATUS | Redirect uses permanent HTTP status | High | Redirects | Permanent redirects (301/308) preserve link equity and signal the move to Google. |
| REDIRECT_CHAIN_MAX_LENGTH      | Redirect chain length limit | Medium | Redirects | Long redirect chains add latency and may exceed Googlebot's limit. |
| CANONICAL_SELF_REFERENCING     | Self-referencing rel=canonical tag present | Medium | Canonical Tags | Self-referencing canonical informs Google of the preferred URL for the content. |
| HEAD_ALLOWED_ELEMENTS_MUST     | Only allowed elements in &lt;head&gt; | High | Page Metadata | Google processes only the allowed elements in the &lt;head&gt;; any invalid element causes the rest of the metadata to be ignored. |
| HEAD_INVALID_ELEMENTS_ORDER_SHOULD | Place invalid &lt;head&gt; elements after allowed elements | Medium | Page Metadata | If an invalid element appears before allowed elements, Google stops reading further elements, causing later metadata to be ignored. |
| REL_ATTRIBUTE_ALLOWED_VALUES   | Validate allowed rel attribute values on outbound links | Low | Qualify your outbound links to Google | Ensures that rel attributes on &lt;a&gt; elements use only the values documented (sponsored, ugc, nofollow) so Google can interpret link qualifications correctly. |
| ROBOTS_TXT_IMAGE_BLOCK         | Block image URLs via robots.txt Disallow rule | Low | robots.txt | Robots.txt Disallow rules prevent Googlebot-Image from indexing specified image URLs, removing them from search results. |
| NOINDEX_HEADER_IMAGE_BLOCK     | Block image URLs via noindex X-Robots-Tag header | High | noindex X-Robots-Tag | The noindex X-Robots-Tag header tells Googlebot not to index the image, but the URL must be crawlable for the header to be read. |
| NOINDEX_RULE_ABSENT            | Ensure noindex robots rule is not present on new site pages | Medium | Prepare the new hosting infrastructure | Prevents accidental indexing of the test site before it goes live. |
| TEMPORARY_BLOCKS_REMOVED       | Verify temporary crawling blocks are removed before launch | High | Start the move | Ensure the site is fully crawlable by Googlebot after the move. |
| SEARCH_CONSOLE_VERIFICATION_PRESENT | Verify Search Console verification assets are present on the new site | Medium | Prepare the new hosting infrastructure | Ownership verification must continue to work after the hosting move. |
| GOOGLEBOT_ACCESSIBLE           | Confirm Googlebot can access the new site (HTTP 200) | Critical | Check that Googlebot is able to access the new hosting infrastructure | Googlebot must be able to retrieve pages to index them after the move. |
| RESOURCES_NOT_BLOCKED_BY_ROBOTS_TXT | Ensure resources are not blocked by robots.txt | High | Resources | Resources such as images, CSS, and JavaScript must be accessible to Google; if they are blocked by robots.txt Google cannot crawl the page properly. |
| HREFLANG_TAGS_PRESENT | hreflang annotations present for multilingual pages | Medium | Internationalized or multi-lingual sites | hreflang tags tell Google which language or regional version of a page to serve, preventing duplicate content issues across locales. |
| SITE_USES_HTTPS | Site should be served over HTTPS | High | Manage the user experience | HTTPS provides security for users and is recommended by Google as a ranking signal. |
| TRUE_404_FOR_NOT_FOUND | Return proper 404 status for missing pages | High | Migrating a single URL | A true 404 response signals to Google that a page is permanently unavailable; soft 404s can mislead indexing. |
| SEO_SHOULD_NOT_LINK_TO_SEO | Avoid linking to SEO provider | Medium | Helpful guidelines | Linking to an SEO provider can be considered a link scheme and may violate Google's policies. |
| SEO_SHOULD_EXPLAIN_FTP_CHANGES | SEO with FTP access must explain changes | Low | Helpful guidelines | Transparency about changes made via FTP ensures the site owner can verify compliance and avoid hidden manipulations. |
| IMG_ALT_TEXT | Ensure all images have descriptive alt text | Medium | Add images to your site, and optimize them | Alt text helps search engines understand image content and improves accessibility. |
| TITLE_ELEMENT_PRESENT | Verify presence of a <title> element | Medium | Influence your title links | The <title> element is used by Google to generate title links in search results. |
| META_DESCRIPTION_PRESENT | Ensure presence of a meta description tag | Low | Control your snippets | Meta description often supplies the snippet shown in search results. |
| LINK_TEXT_DESCRIPTIVE | Verify that anchor text is non‑empty and descriptive | Medium | Link to relevant resources | Descriptive anchor text helps users and search engines understand linked content. |
| ROBOTS_TXT_DISALLOW_CRAWL | Ensure page is not disallowed by robots.txt | High | Crawling | Pages disallowed by robots.txt cannot be crawled, which prevents Google from discovering and indexing them. |
| HTTP_STATUS_NOT_5XX | Verify page does not return a server error status | High | Crawling | HTTP 5xx responses indicate server errors that prevent Googlebot from successfully crawling the page. |
| META_ROBOTS_NOINDEX | Ensure meta robots tag does not block indexing | High | Indexing | A meta robots tag containing "noindex" tells Google not to index the page, preventing it from appearing in search results. |
| PAGE_EXPERIENCE_DIVERSITY | Avoid focusing on only one or two aspects of page experience | Medium | Provide a great page experience | Google advises site owners not to focus on only one or two aspects of page experience, but to provide an overall great experience across many signals. |
| AI_GENERATED_IMAGE_METADATA_MUST_CONTAIN_IPTC_DIGITAL_SOURCE_TYPE | AI-generated images must include IPTC DigitalSourceType metadata | Low | AI-generated image metadata | Ensures AI‑generated images are identifiable and comply with Google Merchant Center policies. |
| AI_GENERATED_PRODUCT_DATA_MUST_BE_LABELED | AI-generated product titles and descriptions must be labeled as AI-generated | Low | AI-generated product data | Guarantees transparency for users and compliance with Google Merchant Center AI content policies. |
| FAVICON_CRAWLABILITY | Ensure favicon and home page are crawlable by Googlebot | High | Guidelines | Googlebot-Image and Googlebot must be able to crawl the favicon file and the home page; blocking them prevents the favicon from appearing in search results. |
| FAVICON_DIMENSIONS | Verify favicon is square and at least 8x8 pixels | Medium | Guidelines | Google requires the favicon to be a square image with a minimum size of 8x8 px to be eligible for display in search results. |
| FAVICON_URL_STABILITY | Ensure favicon URL is stable and not frequently changed | Low | Guidelines | A stable favicon URL prevents Google from losing the association between the site and its favicon, ensuring consistent display in search results. |
| CANONICAL_SELF_LINK | Web Story must have self-referential canonical link | High | Check if the Web Story is indexed | A self‑referential canonical link tells Google the definitive URL for the story, enabling correct indexing and avoiding duplicate content issues. |


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

### Server-side redirects
- PHP_HEADERS_BEFORE_OUTPUT (High): Ensure HTTP redirect headers are sent before any body content in PHP redirects. The documentation states "You must set the headers before sending anything to the screen" for PHP redirects, requiring headers to precede any output.

### Edit or remove unwanted text before moving to a public file format
- NOINDEX_ON_LOGIN_PAGE (High): Ensure login pages include a noindex robots meta tag. Login pages may expose redacted content; a noindex meta tag prevents search engines from indexing them.
- URL_NO_EMAIL (Medium): URLs must not contain email addresses. Email addresses in URLs can be indexed and expose personal information.

### Edit and export images before embedding them
- IMAGE_NON_VECTOR_FORMAT (Medium): Ensure exported images are in non-vector formats (PNG or WEBP). Vector formats may retain hidden layers or metadata that can be indexed.

### Implementing noindex
- NOINDEX_META_TAG_PRESENT (Low): Presence of noindex meta tag in HTML head. A &lt;meta name="robots" content="noindex"&gt; tag placed in the &lt;head&gt; prevents search engines that support the noindex rule from indexing the page.

### File types indexable by Google
- FILETYPE_INDEXABLE_CHECK (Low): File extension is indexable by Google. Google can index the content of the listed text‑based and media file types; resources with other extensions may not be indexed.

### Redirects
- REDIRECT_USES_PERMANENT_STATUS (High): Redirect uses permanent HTTP status. Permanent redirects (301/308) preserve link equity and signal the move to Google.
- REDIRECT_CHAIN_MAX_LENGTH (Medium): Redirect chain length limit. Long redirect chains add latency and may exceed Googlebot's limit.

### Canonical Tags
- CANONICAL_SELF_REFERENCING (Medium): Self-referencing rel=canonical tag present. Self-referencing canonical informs Google of the preferred URL for the content.

### Page Metadata
- HEAD_ALLOWED_ELEMENTS_MUST (High): Only allowed elements in &lt;head&gt;. Google processes only the allowed elements in the &lt;head&gt;; any invalid element causes the rest of the metadata to be ignored.
- HEAD_INVALID_ELEMENTS_ORDER_SHOULD (Medium): Place invalid &lt;head&gt; elements after allowed elements. If an invalid element appears before allowed elements, Google stops reading further elements, causing later metadata to be ignored.

### Qualify your outbound links to Google
- REL_ATTRIBUTE_ALLOWED_VALUES (Low): Validate allowed rel attribute values on outbound links. Ensures that rel attributes on &lt;a&gt; elements use only the values documented (sponsored, ugc, nofollow) so Google can interpret link qualifications correctly.

### robots.txt
- ROBOTS_TXT_IMAGE_BLOCK (Low): Block image URLs via robots.txt Disallow rule. Robots.txt Disallow rules prevent Googlebot-Image from indexing specified image URLs, removing them from search results.

### noindex X-Robots-Tag
- NOINDEX_HEADER_IMAGE_BLOCK (High): Block image URLs via noindex X-Robots-Tag header. The noindex X-Robots-Tag header tells Googlebot not to index the image, but the URL must be crawlable for the header to be read.

### Prepare the new hosting infrastructure
- NOINDEX_RULE_ABSENT (Medium): Ensure noindex robots rule is not present on new site pages. Prevents accidental indexing of the test site before it goes live.
- SEARCH_CONSOLE_VERIFICATION_PRESENT (Medium): Verify Search Console verification assets are present on the new site. Ownership verification must continue to work after the hosting move.

### Start the move
- TEMPORARY_BLOCKS_REMOVED (High): Verify temporary crawling blocks are removed before launch. Ensure the site is fully crawlable by Googlebot after the move.

### Check that Googlebot is able to access the new hosting infrastructure
- GOOGLEBOT_ACCESSIBLE (Critical): Confirm Googlebot can access the new site (HTTP 200). Googlebot must be able to retrieve pages to index them after the move.

### Resources
- RESOURCES_NOT_BLOCKED_BY_ROBOTS_TXT (High): Ensure resources are not blocked by robots.txt. Resources such as images, CSS, and JavaScript must be accessible to Google; if they are blocked by robots.txt Google cannot crawl the page properly.

### Internationalized or multi-lingual sites  
- HREFLANG_TAGS_PRESENT (Medium): hreflang annotations present for multilingual pages. hreflang tags tell Google which language or regional version of a page to serve, preventing duplicate content issues across locales.

### Manage the user experience
- SITE_USES_HTTPS (High): Site should be served over HTTPS. HTTPS provides security for users and is recommended by Google as a ranking signal.

### Migrating a single URL
- TRUE_404_FOR_NOT_FOUND (High): Return proper 404 status for missing pages. A true 404 response signals to Google that a page is permanently unavailable; soft 404s can mislead indexing.

### Helpful guidelines
- SEO_SHOULD_NOT_LINK_TO_SEO (Medium): Avoid linking to SEO provider. Linking to an SEO provider can be considered a link scheme and may violate Google's policies.
- SEO_SHOULD_EXPLAIN_FTP_CHANGES (Low): SEO with FTP access must explain changes. Transparency about changes made via FTP ensures the site owner can verify compliance and avoid hidden manipulations.

### Add images to your site, and optimize them
- IMG_ALT_TEXT (Medium): Ensure all images have descriptive alt text. Alt text helps search engines understand image content and improves accessibility.

### Influence your title links
- TITLE_ELEMENT_PRESENT (Medium): Verify presence of a <title> element. The <title> element is used by Google to generate title links in search results.

### Control your snippets
- META_DESCRIPTION_PRESENT (Low): Ensure presence of a meta description tag. Meta description often supplies the snippet shown in search results.

### Link to relevant resources
- LINK_TEXT_DESCRIPTIVE (Medium): Verify that anchor text is non‑empty and descriptive. Descriptive anchor text helps users and search engines understand linked content.

### Crawling
- ROBOTS_TXT_DISALLOW_CRAWL (High): Ensure page is not disallowed by robots.txt. Pages disallowed by robots.txt cannot be crawled, which prevents Google from discovering and indexing them.
- HTTP_STATUS_NOT_5XX (High): Verify page does not return a server error status. HTTP 5xx responses indicate server errors that prevent Googlebot from successfully crawling the page.

### Indexing
- META_ROBOTS_NOINDEX (High): Ensure meta robots tag does not block indexing. A meta robots tag containing "noindex" tells Google not to index the page, preventing it from appearing in search results.

### Provide a great page experience
- PAGE_EXPERIENCE_DIVERSITY (Medium): Avoid focusing on only one or two aspects of page experience. Google advises site owners not to focus on only one or two aspects of page experience, but to provide an overall great experience across many signals.

### AI-generated image metadata
- AI_GENERATED_IMAGE_METADATA_MUST_CONTAIN_IPTC_DIGITAL_SOURCE_TYPE (Low): AI-generated images must include IPTC DigitalSourceType metadata. Ensures AI‑generated images are identifiable and comply with Google Merchant Center policies.

### AI-generated product data
- AI_GENERATED_PRODUCT_DATA_MUST_BE_LABELED (Low): AI-generated product titles and descriptions must be labeled as AI-generated. Guarantees transparency for users and compliance with Google Merchant Center AI content policies.

### Guidelines
- FAVICON_CRAWLABILITY (High): Ensure favicon and home page are crawlable by Googlebot. Googlebot-Image and Googlebot must be able to crawl the favicon file and the home page; blocking them prevents the favicon from appearing in search results.
- FAVICON_DIMENSIONS (Medium): Verify favicon is square and at least 8x8 pixels. Google requires the favicon to be a square image with a minimum size of 8x8 px to be eligible for display in search results.
- FAVICON_URL_STABILITY (Low): Ensure favicon URL is stable and not frequently changed. A stable favicon URL prevents Google from losing the association between the site and its favicon, ensuring consistent display in search results.

### Check if the Web Story is indexed
- CANONICAL_SELF_LINK (High): Web Story must have self-referential canonical link. A self‑referential canonical link tells Google the definitive URL for the story, enabling correct indexing and avoiding duplicate content issues.

## Analysis Workflows

The SEO engine supports two main analysis workflows:

### Workflow A: Analyze Website URL

When provided with a website URL, extract all required data and apply SEO rules:

#### 1. Prepare Input Data

Use the input preparation scripts to extract all required data from the target website:

```bash
cd scripts/prepare_input/

# Set your target URL
URL="https://example.com"

# Extract all required data (takes 1-3 minutes)
python fetch_html.py $URL           # Gets HTML source code
python fetch_robots_txt.py $URL     # Gets crawling permissions  
python fetch_sitemap.py $URL        # Gets site structure
```

This creates input files:
- `example.com.html` - Page source for content analysis
- `example.com_robots.txt` - Crawling rules and restrictions
- `example.com_sitemap.xml` - Site URL inventory

### 2. Apply SEO Rules

With input data prepared, check relevant SEO rules under rules
The agent will:
1. **Analyze the downloaded files** - Read and understand the content structure
2. **Select relevant rules** - Choose applicable rules based on available file types
3. **Apply rule logic** - Execute the checks described in each rule's documentation
3.a GO THROUGH ALL THE RULES IN THE RULES DIRECTORY AND CHECK WHICH ONES CAN BE APPLIED BASED ON THE FILES PROVIDED.UNLESS SPECIFICALLY EXCLUDED.
4. **Report findings** - Provide pass/fail results with actionable recommendations

### Workflow B: Analyze Existing Files

When you already have HTML files, robots.txt, sitemap.xml, the agent will directly apply SEO rules by reading the rule definitions and checking the provided files.

#### 1. File Requirements

The SEO engine accepts these file types:

- **HTML files** (`.html`, `.htm`) - Webpage source code for content analysis
- **robots.txt files** - Crawling permissions and restrictions  
- **Sitemap files** (`.xml`) - Site URL structure and priorities

#### 2. Intelligent Rule Application

The agent will:
1. **Analyze the provided files** - Read and understand the content structure
2. **Select relevant rules** - Choose applicable rules based on available file types
3. **Apply rule logic** - Execute the checks described in each rule's documentation
3.a GO THROUGH ALL THE RULES IN THE RULES DIRECTORY AND CHECK WHICH ONES CAN BE APPLIED BASED ON THE FILES PROVIDED.UNLESS SPECIFICALLY EXCLUDED.
4. **Report findings** - Provide pass/fail results with actionable recommendations
5. **Fix issues when possible** - For certain rules, the agent can suggest or implement fixes directly in the files

#### 3. Supported Analysis Types

**Single HTML File Analysis:**
```
Provide an HTML file and the agent will check:
- Page title existence and quality  
- Heading hierarchy (h1, h2, etc.)
- Image alt attributes
- Link crawlability
- Favicon dimensions and format
- Content structure and indexability
- And other HTML-based rules...
```

**HTML + robots.txt Analysis:**  
```
Provide both files and the agent will additionally check:
- Resource blocking by robots.txt
- Page crawlability permissions
- robots.txt syntax and rules
- And other crawling-related rules...
```

## Individual Rule Documentation

Each rule is documented in detail in the `rules/` directory. The agent can access and explain any rule:

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
rules/PHP_HEADERS_BEFORE_OUTPUT.md
rules/NOINDEX_ON_LOGIN_PAGE.md
rules/URL_NO_EMAIL.md
rules/IMAGE_NON_VECTOR_FORMAT.md
rules/NOINDEX_META_TAG_PRESENT.md
rules/FILETYPE_INDEXABLE_CHECK.md
rules/REDIRECT_USES_PERMANENT_STATUS.md
rules/REDIRECT_CHAIN_MAX_LENGTH.md
rules/CANONICAL_SELF_REFERENCING.md
rules/HEAD_ALLOWED_ELEMENTS_MUST.md
rules/HEAD_INVALID_ELEMENTS_ORDER_SHOULD.md
rules/REL_ATTRIBUTE_ALLOWED_VALUES.md
rules/ROBOTS_TXT_IMAGE_BLOCK.md
rules/NOINDEX_HEADER_IMAGE_BLOCK.md
rules/NOINDEX_RULE_ABSENT.md
rules/TEMPORARY_BLOCKS_REMOVED.md
rules/SEARCH_CONSOLE_VERIFICATION_PRESENT.md
rules/GOOGLEBOT_ACCESSIBLE.md
rules/RESOURCES_NOT_BLOCKED_BY_ROBOTS_TXT.md
rules/HREFLANG_TAGS_PRESENT.md
rules/SITE_USES_HTTPS.md
rules/TRUE_404_FOR_NOT_FOUND.md
rules/SEO_SHOULD_NOT_LINK_TO_SEO.md
rules/SEO_SHOULD_EXPLAIN_FTP_CHANGES.md
rules/IMG_ALT_TEXT.md
rules/TITLE_ELEMENT_PRESENT.md
rules/META_DESCRIPTION_PRESENT.md
rules/LINK_TEXT_DESCRIPTIVE.md
rules/ROBOTS_TXT_DISALLOW_CRAWL.md
rules/HTTP_STATUS_NOT_5XX.md
rules/META_ROBOTS_NOINDEX.md
rules/PAGE_EXPERIENCE_DIVERSITY.md
rules/AI_GENERATED_IMAGE_METADATA_MUST_CONTAIN_IPTC_DIGITAL_SOURCE_TYPE.md
rules/AI_GENERATED_PRODUCT_DATA_MUST_BE_LABELED.md
rules/FAVICON_CRAWLABILITY.md
rules/FAVICON_DIMENSIONS.md
rules/FAVICON_URL_STABILITY.md
rules/CANONICAL_SELF_LINK.md
```

Each rule file contains:
- Brief explanation of why it matters
- Incorrect example with explanation  
- Correct example with explanation
- Additional context and references

Ask the agent about any specific rule for detailed information, examples, and guidance.

## Complete SEO Analysis

The agent provides comprehensive SEO analysis by:
1. **Reading all rule definitions** from the rules directory
2. **Understanding each rule's logic and requirements** 
3. **Applying appropriate rules** based on your input files
4. **Providing detailed pass/fail results** with actionable recommendations
5. **Explaining rule violations** with examples and fixes

Simply provide your files or website URL and ask for SEO analysis!