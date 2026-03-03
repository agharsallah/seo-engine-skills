---
title: Verify temporary crawling blocks are removed before launch
impact: HIGH
impactDescription: Ensure the site is fully crawlable by Googlebot after the move
tags: robots, crawlability
inputFields:
  - name: robots_txt
    required: true
    description: Contents of the site's robots.txt file.
  - name: html
    required: true
    description: HTML of representative pages to check meta robots tags.
  - name: http_headers
    required: true
    description: HTTP response headers to check X‑Robots‑Tag.
---

## Verify temporary crawling blocks are removed before launch
Ensure the site is fully crawlable by Googlebot after the move.

## Evidence to collect
- Attribute: robots_txt (Look for lines matching '^Disallow:\\s*/' (disallow all).)
- Selector: meta[name="robots"] (Check for 'noindex' or 'nofollow' tokens.)
- Header: X-Robots-Tag (Check for 'noindex' or 'nofollow' tokens.)

## Logic (pseudocode)
Inputs: robots_txt, html, http_headers
1. Scan robots_txt for any line that matches '^Disallow:\\s*/'.
2. Extract meta[name="robots"] content from html and check for 'noindex' or 'nofollow'.
3. Extract X-Robots-Tag header value and check for 'noindex' or 'nofollow'.
4. If any of the above detections are true, set fail; otherwise, set pass.

## Pass condition
No disallow‑all rule in robots.txt and no noindex/nofollow directives in meta tags or X‑Robots‑Tag header.

## Failure messages
- Temporary block detected in ${source}: ${observed}

## Examples
### Passing
No disallow‑all and no noindex directives.
```
robots.txt:
User-agent: *
Allow: /
```

### Failing
robots.txt blocks all crawling.
```
robots.txt:
User-agent: *
Disallow: /
```

### test case passing
```json
{
  "html": "<html><head><meta name=\"robots\" content=\"index, follow\"></head></html>",
  "http_headers": {
    "X-Robots-Tag": "index, follow"
  },
  "robots_txt": "User-agent: *\nAllow: /"
}
```

### test case failing
```json
{
  "html": "<html><head><meta name=\"robots\" content=\"index, follow\"></head></html>",
  "http_headers": {
    "X-Robots-Tag": "index, follow"
  },
  "robots_txt": "User-agent: *\nDisallow: /"
}
```

### References
Reference: [Changing Your Web Hosting and SEO](https://developers.google.com/search/docs/hosting/migrate)