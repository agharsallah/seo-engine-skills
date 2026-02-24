---
title: Ensure no cloaking between Googlebot and users
impact: HIGH
impactDescription: Cloaking violates spam policies and can cause demotion or removal from Google Search results
tags: cloaking, spam_policy
inputFields:
  - name: html_googlebot
    required: true
    description: Full HTML content returned when the page is fetched with a Googlebot user‑agent.
  - name: html_user
    required: true
    description: Full HTML content returned when the page is fetched with a typical browser user‑agent.
---

## Ensure no cloaking between Googlebot and users
Cloaking violates spam policies and can cause demotion or removal from Google Search results.

## Evidence to collect
- Capture the entire HTML document for each user‑agent to compute a content hash

## Logic (pseudocode)
Input: html_googlebot, html_user
1. Compute hash_g = hash(html_googlebot)
2. Compute hash_u = hash(html_user)
3. If hash_g == hash_u then result = PASS else result = FAIL

## Pass condition
The HTML content served to Googlebot and to regular users is identical.

## Failure messages
- Cloaking detected: content hash for Googlebot (${hash_g}) differs from user view (${hash_u}).

## Examples
### Passing
Both fetches return identical HTML.
```
html_googlebot = "<html><body>Content</body></html>"
html_user = "<html><body>Content</body></html>"
```

### Failing
Googlebot receives stripped content while users see full page.
```
html_googlebot = "<html><body></body></html>"
html_user = "<html><body>Full Content</body></html>"
```

### test case passing
```html
<html><body>Same</body></html>
```

### test case failing
```html
<!-- Googlebot: --><html><body></body></html>
<!-- User: --><html><body>Visible</body></html>
```

### References
Reference: [A/B Testing Best Practices for Search](https://developers.google.com/search/docs/ab-testing)