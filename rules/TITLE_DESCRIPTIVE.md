---
title: Page title is descriptive, specific, and accurate
impact: MEDIUM
impactDescription: The documentation advises ensuring title elements are descriptive, specific, and accurate to improve SEO.
tags: seo
inputFields:
  - name: html
    required: true
    description: HTML content to evaluate for descriptive title.
---

## TITLE_DESCRIPTIVE
Ensures the page title is descriptive, specific, and accurate.

## Evidence to collect
- Text content of <title> element
- Word count in title

## Logic (pseudocode)
Input: html
1. Parse html and locate the <title> element.
2. Extract its text content and trim whitespace.
3. Split the text into words (separated by whitespace).
4. Count the number of words.
5. Store count as observed_word_count.

## Pass condition
Title text contains at least two words.

## Failure messages
Title is missing or too short (${observed_word_count} words).

## Examples
### Passing
<title>My Awesome Website</title>

### Failing
<title>Home</title>
<title>   </title>

### References
Google Search documentation — https://developers.google.com/search/docs/appearance/title-link