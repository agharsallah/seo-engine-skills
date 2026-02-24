---
title: Meta description tag is present and descriptive
impact: MEDIUM
impactDescription: Documentation suggests ensuring description meta tags are descriptive, specific, and accurate.
tags: seo
inputFields:
  - name: html
    required: true
    description: HTML content to evaluate for meta description.
---

## META_DESCRIPTION_PRESENT
Ensures the meta description tag is present and descriptive.

## Evidence to collect
- Presence and content of <meta name="description"> element
- Length of content attribute

## Logic (pseudocode)
Input: html
1. Parse html and locate <meta name="description"> element.
2. If not found, set observed_present = false.
3. If found, extract its content attribute, trim whitespace.
4. Compute length of content in characters as observed_length.

## Pass condition
Meta description is present and its length is at least 50 characters.

## Failure messages
Meta description missing or too short (${observed_length} characters).

## Examples
### Passing
<meta name="description" content="This is a descriptive summary of the page that is specific and accurate.">

### Failing
<meta name="description" content="Short.">
<!-- No meta description present -->

### References
Google Search documentation — https://developers.google.com/search/docs/appearance/meta-description