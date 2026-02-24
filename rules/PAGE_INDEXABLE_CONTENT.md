---
title: Page has indexable textual content
impact: MEDIUM
impactDescription: Google indexes pages that contain textual content in supported file types and that do not violate spam policies.
tags: indexability
inputFields:
  - name: html
    required: true
    description: HTML content to evaluate for indexable text.
---

## PAGE_INDEXABLE_CONTENT
Ensures the page contains indexable textual content for search engines.

## Evidence to collect
- Text inside <body> tags, excluding script and style sections

## Logic (pseudocode)
Input: html
1. Extract text inside <body> tags, removing script and style sections.
2. Strip HTML tags to obtain plain text.
3. If resulting text contains at least one alphanumeric character, result = pass.
4. Otherwise, result = fail.

## Pass condition
Body contains at least one alphanumeric character after stripping markup.

## Failure messages
Page lacks indexable textual content

## Examples
### Passing
<body>Hello world!</body>

### Failing
<body><script>...</script></body>
<body><style>...</style></body>

### References
Google Search documentation — https://developers.google.com/search/docs/appearance/content