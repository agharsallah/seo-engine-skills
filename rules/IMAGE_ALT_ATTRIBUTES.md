---
title: All images have descriptive alt attributes
impact: MEDIUM
impactDescription: Documentation advises alt attributes be descriptive, specific, and accurate.
tags: seo
inputFields:
  - name: html
    required: true
    description: HTML content to evaluate for descriptive alt attributes.
---

## IMAGE_ALT_ATTRIBUTES
Ensures all images have descriptive alt attributes.

## Evidence to collect
- Presence and value of alt attributes for all <img> elements
- Description quality of alt text

## Logic (pseudocode)
Input: html
1. Parse html and find all <img> elements.
2. For each img, check if alt attribute exists and is non‑empty after trimming.
3. If any img fails, record its index (starting at 1) as failing_index.

## Pass condition
All <img> elements have descriptive, non-empty alt attributes.

## Failure messages
Image at index ${failing_index} is missing a descriptive alt attribute.

## Examples
### Passing
<img src="logo.png" alt="Company Logo">

### Failing
<img src="logo.png" alt=" ">
<img src="logo.png">

### References
Google Search documentation — https://developers.google.com/search/docs/appearance/images