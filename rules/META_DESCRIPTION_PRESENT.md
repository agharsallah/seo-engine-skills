---
title: Ensure presence of a meta description tag
impact: LOW
impactDescription: Meta description often supplies the snippet shown in search results.
tags: meta, snippet
inputFields:
  - name: html
    required: true
    description: The full HTML source of the page.
---

## Ensure presence of a meta description tag
Meta description often supplies the snippet shown in search results.

## Evidence to collect
- Content attribute of the meta description: `meta[name='description'][content]`

## Logic (pseudocode)
Inputs: html
Steps:
1. Parse html into a DOM.
2. Locate <meta name="description"> element.
3. If element exists and its content attribute is non‑empty, result = pass.
4. Otherwise, result = fail.

## Pass condition
Page contains a non‑empty meta description tag.

## Failure messages
Meta description tag is missing or empty.

## Examples
### Passing
Page with meta description.
```html
<head><meta name="description" content="Learn how to bake a chocolate cake in 5 easy steps."></head>
```

### Failing
Missing meta description.
```html
<head></head>
```

### test case passing
```html
<html><head><meta name="description" content="A short summary."></head><body></body></html>
```

### test case failing
```html
<html><head></head><body></body></html>
```

### References
Reference: [SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)