---
title: Ensure all images have descriptive alt text
impact: MEDIUM
impactDescription: Alt text helps search engines understand image content and improves accessibility.
tags: images, accessibility, alt-text
inputFields:
  - name: html
    required: true
    description: The full HTML source of the page to be evaluated.
---

## Ensure all images have descriptive alt text
Alt text helps search engines understand image content and improves accessibility.

## Evidence to collect
- Alt attribute value for each img element: `img[alt]`

## Logic (pseudocode)
Inputs: html
Steps:
1. Parse html into a DOM.
2. For each <img> element in the DOM:
   a. Retrieve the value of its "alt" attribute.
   b. If the attribute is missing or empty, record a failure.
3. If any failures recorded, result = fail; else result = pass.

## Pass condition
All <img> elements have a non‑empty alt attribute.

## Failure messages
Image at index ${index} is missing a non‑empty alt attribute.

## Examples
### Passing
Image with descriptive alt text.
```html
<img src="cat.jpg" alt="A tabby cat sitting on a windowsill">
```

### Failing
Image missing alt attribute.
```html
<img src="cat.jpg">
```

### test case passing
```html
<html><body><img src="a.jpg" alt="A scenic mountain"></body></html>
```

### test case failing
```html
<html><body><img src="b.jpg"></body></html>
```

### References
Reference: [SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)