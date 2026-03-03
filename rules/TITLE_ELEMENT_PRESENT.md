---
title: Verify presence of a <title> element
impact: MEDIUM
impactDescription: The <title> element is used by Google to generate title links in search results.
tags: title, seo
inputFields:
  - name: html
    required: true
    description: The full HTML source of the page.
---

## Verify presence of a <title> element
The <title> element is used by Google to generate title links in search results.

## Evidence to collect
- Text content of the <title> element: `title`

## Logic (pseudocode)
Inputs: html
Steps:
1. Parse html into a DOM.
2. Search for a <title> element in the <head>.
3. If a <title> element exists and its text is non‑empty, result = pass.
4. Otherwise, result = fail.

## Pass condition
Page contains a non‑empty <title> element.

## Failure messages
The page does not contain a <title> element or it is empty.

## Examples
### Passing
Page with a proper title.
```html
<head><title>Delicious Apple Pie Recipe</title></head>
```

### Failing
Missing title element.
```html
<head></head>
```

### test case passing
```html
<html><head><title>Example Page</title></head><body></body></html>
```

### test case failing
```html
<html><head></head><body></body></html>
```

### References
Reference: [SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)