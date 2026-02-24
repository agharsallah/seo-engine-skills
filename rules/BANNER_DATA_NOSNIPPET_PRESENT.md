---
title: Ensure banner or popup uses data-nosnippet attribute
impact: MEDIUM
impactDescription: Prevents banner or popup content from being shown in search result snippets
tags: banner, data-nosnippet, snippet-prevention
inputFields:
  - name: html
    required: true
    description: Full HTML of the page to be evaluated.
---

## Ensure banner or popup uses data-nosnippet attribute
Prevents banner or popup content from being shown in search result snippets.

## Evidence to collect
- Any element that has the data-nosnippet attribute (*[data-nosnippet])

## Logic (pseudocode)
Input: html
1. Parse the HTML document.
2. Search for any element that has a 'data-nosnippet' attribute.
3. If at least one such element is found, result = pass.
4. Otherwise, result = fail.

## Pass condition
At least one element with a data-nosnippet attribute is present on the page.

## Failure messages
- No element with data-nosnippet attribute found on the page.

## Examples
### Passing
Banner element includes data-nosnippet attribute.
```html
<div class="banner" data-nosnippet>We are temporarily closed.</div>
```

### Failing
Banner element lacks data-nosnippet attribute.
```html
<div class="banner">We are temporarily closed.</div>
```

### test case passing
```html
<div class="banner" data-nosnippet>Closed</div>
```

### test case failing
```html
<div class="banner">Closed</div>
```

### References
Reference: [Temporarily pause or disable a website](https://developers.google.com/search/docs/monitor-site/temporarily-pause-or-disable-website)