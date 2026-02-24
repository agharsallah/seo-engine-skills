---
title: Ensure HTML containing data-nosnippet attribute is well‑formed
impact: HIGH
impactDescription: The documentation states that the HTML section must be valid HTML for data‑nosnippet to be machine‑readable
tags: data-nosnippet, html-validation
inputFields:
  - name: html
    required: true
    description: Full HTML content of the page
---

## Ensure HTML containing data-nosnippet attribute is well‑formed
The documentation states that the HTML section must be valid HTML for data‑nosnippet to be machine‑readable.

## Evidence to collect
- Collect all elements that declare data-nosnippet ([data-nosnippet])

## Logic (pseudocode)
Input: html
1. Parse the html using an HTML validator.
2. If the parser reports any well‑formedness errors, set observed = error details.
3. If errors exist, result = fail; else result = pass.

## Pass condition
HTML parses without any well‑formedness errors.

## Failure messages
- HTML parsing error detected: ${observed}

## Examples
### Passing
Valid HTML with a correctly closed data‑nosnippet element.
```html
<html>
  <head><title>Example</title></head>
  <body>
    <p>Snippet text <span data-nosnippet>hidden part</span>.</p>
  </body>
</html>
```

### Failing
HTML where a data‑nosnippet element is inside an unclosed tag, causing parsing errors.
```html
<html>
  <head><title>Bad Example</title></head>
  <body>
    <div data-nosnippet>
      <p>Unclosed div will cause the rest of the page to be treated as part of the element.
</html>
```

### test case passing
```html
<html><head></head><body><span data-nosnippet>hide</span></body></html>
```

### test case failing
```html
<html><head></head><body><div data-nosnippet><p>Missing closing div
```

### References
Reference: [Robots meta tag, data‑nosnippet, and X‑Robots‑Tag specifications](https://developers.google.com/search/docs/advanced/robots/robots_meta_tag)