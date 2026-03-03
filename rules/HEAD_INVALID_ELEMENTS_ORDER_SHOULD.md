---
title: Place invalid <head> elements after allowed elements
impact: MEDIUM
impactDescription: If an invalid element appears before allowed elements, Google stops reading further elements, causing later metadata to be ignored
tags: metadata, head, ordering
inputFields:
  - name: html
    required: true
    description: HTML content of the page
---

## Place invalid &lt;head&gt; elements after allowed elements
If an invalid element appears before allowed elements, Google stops reading further elements, causing later metadata to be ignored.

## Evidence to collect
- Selector: head > * (Collect ordered list of tag names of direct children of &lt;head&gt;)

## Logic (pseudocode)
Inputs: html
1. Parse html and locate the &lt;head&gt; element.
2. Create list TAGS of tag names of each direct child in order.
3. Define ALLOWED = {title, meta, link, script, style, base, noscript, template}
4. Find index of first tag not in ALLOWED (first_invalid_index). If none, pass.
5. For each tag after first_invalid_index:
   a. If tag is in ALLOWED, record as violation.
6. If any violation recorded, fail; else pass.

## Pass condition
No allowed element appears after the first invalid element within &lt;head&gt;.

## Failure messages
- Allowed element &lt;${observed}&gt; appears after invalid element &lt;${invalid}&gt; in &lt;head&gt;.

## Examples
### Passing
Invalid element placed after all allowed elements.
```html
<head>
  <title>Example</title>
  <meta name="description" content="...">
  <iframe src="..."></iframe>
</head>
```

### Failing
Allowed element appears after an invalid element.
```html
<head>
  <iframe src="..."></iframe>
  <meta name="description" content="...">
</head>
```

### test case passing
```html
<html><head><title>Test</title><iframe src=''></iframe></head></html>
```

### test case failing
```html
<html><head><iframe src=''></iframe><meta charset='utf-8'></head></html>
```

### References
Reference: [Valid Page Metadata for Google Search](https://developers.google.com/search/docs/appearance/metadata)