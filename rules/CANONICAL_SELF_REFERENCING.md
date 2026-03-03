---
title: Self-referencing rel=canonical tag present
impact: MEDIUM
impactDescription: Self-referencing canonical informs Google of the preferred URL for the content
tags: canonical, seo
inputFields:
  - name: html
    required: true
    description: HTML source of the page
---

## Self-referencing rel=canonical tag present
Self-referencing canonical informs Google of the preferred URL for the content.

## Evidence to collect
- Selector: link[rel='canonical'] (Href of canonical link)

## Logic (pseudocode)
Input: html
1. Parse HTML and locate &lt;link rel="canonical"&gt; element.
2. Extract its href attribute.
3. Compare href to the page's own URL (provided externally via context, assume variable page_url).
4. Pass if href equals page_url.

## Pass condition
Canonical href matches the page's own URL

## Failure messages
- Canonical href ${observed} does not match page URL ${expected}

## Examples
### Passing
Page has &lt;link rel='canonical' href='https://example.com/page'&gt;
```html
<link rel="canonical" href="https://example.com/page">
```

### Failing
Canonical points to different URL
```html
<link rel="canonical" href="https://example.com/old-page">
```

### test case passing
```html
<html><head><link rel='canonical' href='https://example.com/page'></head></html>
```

### test case failing
```html
<html><head><link rel='canonical' href='https://example.com/old'></head></html>
```

### References
Reference: [Update annotations](https://developers.google.com/search/consolidate-duplicate-urls.html)