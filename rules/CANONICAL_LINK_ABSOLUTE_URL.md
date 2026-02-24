---
title: rel="canonical" link element must use an absolute URL
impact: MEDIUM
impactDescription: Documentation recommends using absolute URLs for rel="canonical" link elements to avoid problems
tags: canonical, url
inputFields:
  - name: html
    required: true
    description: Full HTML source of the page.
---

## rel="canonical" link element must use an absolute URL
Documentation recommends using absolute URLs for rel="canonical" link elements to avoid problems.

## Evidence to collect
- href attribute of canonical link inside head (head > link[rel='canonical'])

## Logic (pseudocode)
Input: html
1. Parse html into DOM.
2. Locate <link rel='canonical'> inside <head>.
3. If element not found, result = not_applicable.
4. Extract href attribute.
5. If href matches regex ^https?://, result = pass else fail.

## Pass condition
The href attribute of the rel="canonical" link starts with "http://" or "https://".

## Failure messages
- Canonical link href '${observed}' is not an absolute URL.

## Examples
### Passing
Absolute URL in canonical link.
```html
<head>
  <link rel="canonical" href="https://example.com/page.html">
</head>
```

### Failing
Relative URL in canonical link.
```html
<head>
  <link rel="canonical" href="/page.html">
</head>
```

### test case passing
```html
<head><link rel='canonical' href='https://example.com/page.html'></head>
```

### test case failing
```html
<head><link rel='canonical' href='/page.html'></head>
```

### References
Reference: [How to specify a canonical URL with rel="canonical" and other methods](https://developers.google.com/search/docs/advanced/canonical/rel-canonical)