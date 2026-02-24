---
title: Do not specify different canonical URLs for the same page using different methods
impact: HIGH
impactDescription: Documentation warns that specifying different canonical URLs via different techniques for the same page can cause conflicts
tags: canonical, consistency
inputFields:
  - name: html
    required: true
    description: Full HTML source of the page.
  - name: http_headers
    required: true
    description: Response headers of the page.
  - name: sitemap_xml
    required: false
    description: Sitemap XML content (if page is listed).
---

## Do not specify different canonical URLs for the same page using different methods
Documentation warns that specifying different canonical URLs via different techniques for the same page can cause conflicts.

## Evidence to collect
- HTML canonical URL (head > link[rel='canonical'])
- Parse Link header for rel="canonical"
- If page URL appears in sitemap, treat as canonical candidate (//url/loc)

## Logic (pseudocode)
Input: html, http_headers, sitemap_xml
1. Extract canonical URL from HTML <link rel='canonical'> (html_canonical).
2. Extract canonical URL from Link header with rel='canonical' (header_canonical).
3. If sitemap_xml provided, locate <url><loc> matching the page URL (sitemap_canonical).
4. Build list of all non-null canonical URLs.
5. If list length <= 1, pass.
6. If more than one distinct URL exists, fail.

## Pass condition
All discovered canonical URLs (HTML, header, sitemap) are identical or only one method is used.

## Failure messages
- Conflicting canonical URLs detected: ${observed_urls}.

## Examples
### Passing
Same canonical URL via HTML and header.
```html
<!-- HTML -->
<head><link rel="canonical" href="https://example.com/page.html"></head>
<!-- HTTP Header -->
Link: <https://example.com/page.html>; rel="canonical"
```

### Failing
Different canonical URLs in HTML and header.
```html
<!-- HTML -->
<head><link rel="canonical" href="https://example.com/page.html"></head>
<!-- HTTP Header -->
Link: <https://example.com/other.html>; rel="canonical"
```

### test case passing
```html
<head><link rel='canonical' href='https://example.com/page.html'></head>
```

### test case failing
```html
<!-- Different URLs in HTML vs header -->
<head><link rel='canonical' href='https://example.com/page.html'></head>
<!-- Link: <https://example.com/other.html>; rel="canonical" -->
```

### References
Reference: [How to specify a canonical URL with rel="canonical" and other methods](https://developers.google.com/search/docs/advanced/canonical/rel-canonical)