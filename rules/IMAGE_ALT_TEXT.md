---
title: All images have non-empty alt attributes
impact: MEDIUM
impactDescription: Alt text is recommended for images to describe content for users and search engines.
tags: accessibility
inputFields:
  - name: html
    required: true
    description: HTML content to evaluate for image alt attributes.
---

## IMAGE_ALT_TEXT
Ensures all <img> elements have non-empty alt attributes for accessibility and SEO.

## Evidence to collect
- Presence and value of alt attributes for all <img> elements

## Logic (pseudocode)
Input: html
1. Parse html into a DOM.
2. Select all <img> elements.
3. For each <img>, retrieve its 'alt' attribute.
4. If any <img> lacks an 'alt' attribute or its trimmed value is empty, result = fail.
5. If all images have non‑empty alt text, result = pass.

## Pass condition
Every <img> element includes a non‑empty alt attribute.

## Failure messages
Image with src '${src}' is missing alt text.

## Examples
### Passing
<img src="logo.png" alt="Company Logo">

### Failing
<img src="logo.png">
<img src="logo.png" alt="   ">

### References
Google Search documentation — https://developers.google.com/search/docs/appearance/images