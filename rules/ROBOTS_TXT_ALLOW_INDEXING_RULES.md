---
title: URLs containing robots meta or X‑Robots‑Tag must not be disallowed by robots.txt
impact: CRITICAL
impactDescription: Documentation requires that if indexing or serving rules must be followed, the URLs containing those rules cannot be disallowed from crawling via robots.txt
tags: robots.txt, indexing-rules
inputFields:
  - name: robots_txt
    required: true
    description: Content of the site's robots.txt file
  - name: url
    required: true
    description: Full URL of the page being evaluated
  - name: html
    required: false
    description: HTML content of the page (to detect meta robots tags)
  - name: http_headers
    required: false
    description: HTTP response headers (to detect X‑Robots‑Tag)
---

## URLs containing robots meta or X‑Robots‑Tag must not be disallowed by robots.txt
Documentation requires that if indexing or serving rules must be followed, the URLs containing those rules cannot be disallowed from crawling via robots.txt.

## Evidence to collect
- Collect content of any robots meta tags (meta[name~='robots|googlebot|googlebot-news'])
- Collect X‑Robots‑Tag header values

## Logic (pseudocode)
Input: robots_txt, url, html, http_headers
1. Determine if html contains a <meta name="robots"...> or similar tag.
2. Determine if http_headers contain an X-Robots-Tag header.
3. If neither is present, result = not_applicable.
4. Parse robots_txt to extract all Disallow paths (ignore comments, blank lines).
5. Extract the path component of url.
6. If any Disallow path matches the url path (exact prefix match), then result = fail.
7. Otherwise, result = pass.

## Pass condition
No Disallow rule in robots.txt matches the URL path when the page includes robots meta or X‑Robots‑Tag.

## Failure messages
- URL ${url} is disallowed by robots.txt while containing indexing/serving rules.

## Examples
### Passing
Page with robots meta tag and robots.txt that allows crawling.
```
robots.txt:
User-agent: *
Disallow: /private/

Page URL: https://example.com/public/page.html
<meta name="robots" content="noindex">
```

### Failing
Page with X‑Robots‑Tag header but robots.txt disallows the path.
```
robots.txt:
User-agent: *
Disallow: /secret/

Page URL: https://example.com/secret/report.pdf
HTTP header: X-Robots-Tag: noindex
```

### test case passing
```
robots.txt: User-agent: *\nDisallow: /private/
URL: https://example.com/public/page.html
HTML: <meta name="robots" content="noindex">
```

### test case failing
```
robots.txt: User-agent: *\nDisallow: /secret/
URL: https://example.com/secret/report.pdf
Headers: X-Robots-Tag: noindex
```

### References
Reference: [Robots meta tag, data‑nosnippet, and X‑Robots‑Tag specifications](https://developers.google.com/search/docs/advanced/robots/robots_meta_tag)