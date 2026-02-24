---
title: Heading hierarchy is logical and valid
impact: MEDIUM
impactDescription: Logical heading hierarchy improves accessibility and SEO.
tags: heading, hierarchy
inputFields:
  - name: html
    required: true
    description: HTML content to evaluate for heading hierarchy.
---

## HEADING_HIERARCHY
Ensures the page uses a logical and valid heading hierarchy.

## Evidence to collect
- Structure and order of heading elements (<h1>, <h2>, <h3>, etc.)

## Logic (pseudocode)
Input: html
1. Parse html and extract heading elements.
2. Check for logical order and nesting.
3. If hierarchy is broken or illogical, result = fail; else pass.

## Pass condition
Heading hierarchy is logical and valid.

## Failure messages
Heading hierarchy is broken or illogical.

## Examples
### Passing
<h1>Main</h1><h2>Sub</h2><h3>Detail</h3>

### Failing
<h2>Sub</h2><h1>Main</h1>

### References
Accessibility documentation — https://www.w3.org/WAI/tutorials/page-structure/headings/