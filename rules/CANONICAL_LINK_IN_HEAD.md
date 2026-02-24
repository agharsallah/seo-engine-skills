---
title: rel="canonical" link element must be placed in <head>
impact: HIGH
impactDescription: The documentation states that the rel="canonical" link element is only accepted if it appears in the <head> section of the HTML
tags: canonical, html
inputFields:
  - name: html
    required: true
    description: Full HTML source of the page.
---

## rel="canonical" link element must be placed in <head>
The documentation states that the rel="canonical" link element is only accepted if it appears in the <head> section of the HTML.

## Evidence to collect
- href attribute of canonical link inside head (head > link[rel='canonical'])

## Logic (pseudocode)
Input: html
1. Parse html into DOM.
2. Search for <link> elements with rel='canonical' inside the <head>.
3. If at least one such element exists, set found = true else false.
4. Return found.

## Pass condition
At least one rel="canonical" link element is found inside the <head>.

## Failure messages
- No rel='canonical' link element found in the <head> section.

## Examples
### Passing
Correct placement of canonical link in head.
```html
<html>
<head>
  <link rel="canonical" href="https://example.com/page.html">
</head>
<body>...</body>
</html>
```

### Failing
Canonical link placed outside head.
```html
<html>
<body>
  <link rel="canonical" href="https://example.com/page.html">
</body>
</html>
```

### test case passing
```html
<html><head><link rel='canonical' href='https://example.com/page.html'></head></html>
```

### test case failing
```html
<html><body><link rel='canonical' href='https://example.com/page.html'></body></html>
```

### References
Reference: [How to specify a canonical URL with rel="canonical" and other methods](https://developers.google.com/search/docs/advanced/canonical/rel-canonical)