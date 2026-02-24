---
title: Page title tag present and non-empty
impact: LOW
impactDescription: Title is a prominent location for keywords as recommended in the documentation.
tags: content
inputFields:
  - name: html
    required: true
    description: HTML content to evaluate for the presence of a <title> tag.
---

## PAGE_TITLE_EXISTS
Ensures the page has a <title> tag with non-empty text, which is important for SEO and keyword prominence.

## Evidence to collect
- Presence and text content of <title> element

## Logic (pseudocode)
Input: html
1. Parse html into a DOM.
2. Locate the <title> element using selector "head > title".
3. If the element is not found, set observed = null.
4. Else, set observed = trimmed text content of the element.
5. If observed is not null and length(observed) > 0, result = pass else fail.

## Pass condition
A <title> element exists and its text is non‑empty.

## Failure messages
Missing or empty <title> tag.

## Examples
### Passing
<head><title>My Page Title</title></head>

### Failing
<head></head>
<head><title>   </title></head>

### References
Google Search documentation — https://developers.google.com/search/docs/appearance/title-link