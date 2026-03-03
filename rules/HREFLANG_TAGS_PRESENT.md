---
title: hreflang annotations present for multilingual pages
impact: MEDIUM
impactDescription: hreflang tags tell Google which language or regional version of a page to serve, preventing duplicate content issues across locales.
tags: hreflang, multilingual
inputFields:
  - name: html
    required: true
    description: HTML content of the page to inspect for hreflang link elements.
---

## hreflang annotations present for multilingual pages
hreflang tags tell Google which language or regional version of a page to serve, preventing duplicate content issues across locales.

## Evidence to collect
- Value of the hreflang attribute for each alternate link: `link[rel=alternate][hreflang]`

## Logic (pseudocode)
Input: html
1. Parse html and find all <link> elements where rel="alternate" and hreflang attribute exists.
2. If at least one such element is found, the check passes.
3. Otherwise, it fails.

## Pass condition
At least one hreflang link element is present in the page.

## Failure messages
No hreflang link tags found on the page.

## Examples
### Passing
Page includes hreflang links for English and French versions.
```html
<link rel="alternate" hreflang="en" href="https://example.com/en/page.html">
<link rel="alternate" hreflang="fr" href="https://example.com/fr/page.html">
```

### Failing
Page has no hreflang annotations.
```html
<title>Example Page</title>
```

### test case passing
```html
<link rel="alternate" hreflang="es" href="https://example.com/es/page.html">
```

### test case failing
```html
<title>Sample</title>
```

### References
Reference: [Technical SEO Techniques and Strategies](https://developers.google.com/search/docs/technical-seo)