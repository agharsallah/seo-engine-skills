---
title: Head section contains valid HTML
impact: MEDIUM
impactDescription: Valid HTML in the head section ensures proper rendering and SEO.
tags: html, head
inputFields:
  - name: html
    required: true
    description: HTML content to evaluate for valid head section.
---

## HEAD_SECTION_VALID_HTML
Ensures the <head> section contains valid HTML markup.

## Evidence to collect
- Structure and elements within the <head> section

## Logic (pseudocode)
Input: html
1. Parse html and extract <head> section.
2. Validate HTML structure and required elements.
3. If invalid or missing elements, result = fail; else pass.

## Pass condition
Head section contains valid HTML and required elements.

## Failure messages
Head section contains invalid HTML or is missing required elements.

## Examples
### Passing
<head><title>Valid</title><meta charset="UTF-8"></head>

### Failing
<head><title></head>

### References
HTML documentation — https://developer.mozilla.org/en-US/docs/Web/HTML/Element/head