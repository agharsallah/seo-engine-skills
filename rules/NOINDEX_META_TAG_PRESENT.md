---
title: Presence of noindex meta tag in HTML head
impact: LOW
impactDescription: Prevents search engines that support the noindex rule from indexing the page
tags: noindex, meta, seo
inputFields:
  - name: html
    required: true
    description: The full HTML source of the page to be evaluated.
---

## Presence of noindex meta tag in HTML head
A &lt;meta name="robots" content="noindex"&gt; tag placed in the &lt;head&gt; prevents search engines that support the noindex rule from indexing the page, as described in the documentation.

## Evidence to collect
- Selector: head meta[name='robots'][content~='noindex']

## Logic (pseudocode)
Inputs: html
Steps:
1. Parse the HTML document.
2. Search within the &lt;head&gt; element for a &lt;meta&gt; tag where:
   a. attribute name equals "robots"
   b. attribute content contains the token "noindex" (case-insensitive).
3. If such a tag exists, set observed = true; else observed = false.

## Pass condition
The page contains a &lt;meta name="robots" content="...noindex..."&gt; tag in its &lt;head&gt;.

## Failure messages
- No &lt;meta name="robots" content="...noindex..."&gt; tag found in the &lt;head&gt; of the page.

## Examples
### Passing
Page includes the required meta tag.
```html
<html>
  <head>
    <meta name="robots" content="noindex">
  </head>
  <body>...</body>
</html>
```

### Failing
Page lacks the required meta tag.
```html
<html>
  <head>
    <title>Example</title>
  </head>
  <body>...</body>
</html>
```

### test case passing
```html
<html><head><meta name="robots" content="noindex"></head><body></body></html>
```

### test case failing
```html
<html><head><title>Test</title></head><body></body></html>
```

### References
Reference: [Block Search indexing with noindex](https://developers.google.com/search/docs/advanced/crawling/block-indexing-noindex)