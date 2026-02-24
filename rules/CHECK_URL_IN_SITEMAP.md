---
title: URL presence in sitemap.xml
impact: MEDIUM
impactDescription: Presence of the URL in a sitemap is mentioned as a factor influencing canonical selection
tags: sitemap, canonical
inputFields:
  - name: sitemap_xml
    required: true
    description: The XML content of the site's sitemap.
  - name: url
    required: true
    description: The absolute URL of the page being evaluated.
---

## URL presence in sitemap.xml
Presence of the URL in a sitemap is mentioned as a factor influencing canonical selection.

## Evidence to collect
- Search for URL in sitemap <loc> elements (//url/loc[text() = '${url}'])

## Logic (pseudocode)
Input: sitemap_xml, url
1. Parse sitemap_xml as XML.
2. Search for any <loc> element whose text equals the given url.
3. If found, set found = true; else found = false.

## Pass condition
The URL is listed in the sitemap.xml file.

## Failure messages
- URL ${url} not found in sitemap.xml.

## Examples
### Passing
URL appears in the sitemap.
```xml
<urlset><url><loc>https://example.com/page</loc></url></urlset>
```

### Failing
URL missing from sitemap.
```xml
<urlset></urlset>
```

### test case passing
```xml
<urlset><url><loc>https://example.com/page</loc></url></urlset>
```

### test case failing
```xml
<urlset></urlset>
```

### References
Reference: [What is URL Canonicalization](https://developers.google.com/search/docs/advanced/crawling/consolidate-duplicate-urls)