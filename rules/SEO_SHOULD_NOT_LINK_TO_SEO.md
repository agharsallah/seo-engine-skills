---
title: Avoid linking to SEO provider
impact: MEDIUM
impactDescription: Linking to an SEO provider can be considered a link scheme and may violate Google's policies.
tags: link_scheme, outbound_links
inputFields:
  - name: html
    required: true
    description: HTML content of the site to analyze outbound links.
---

## Avoid linking to SEO provider
Linking to an SEO provider can be considered a link scheme and may violate Google's policies.

## Evidence to collect
- URLs of all outbound links: `a[href]`

## Logic (pseudocode)
Input: html
1. Parse html and extract all <a> elements with href.
2. For each href, extract domain.
3. If any domain matches known SEO provider domains (provided via configuration), flag as violation.
4. If no such links, pass.

## Pass condition
No outbound links point to the SEO provider's domain.

## Failure messages
Found outbound link to SEO provider domain: ${observed}

## Examples
### Passing
Page without links to SEO provider.
```html
<html><body><a href='https://example.com'>Home</a></body></html>
```

### Failing
Page contains link to SEO provider.
```html
<html><body><a href='https://seo-provider.com'>SEO</a></body></html>
```

### test case passing
```html
<a href='https://example.com'>Home</a>
```

### test case failing
```html
<a href='https://seo-provider.com'>SEO</a>
```

### References
Reference: [Helpful guidelines](https://developers.google.com/search/docs/seo/choose-an-seo)