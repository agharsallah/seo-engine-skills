---
title: AMP page must follow AMP HTML specification
impact: CRITICAL
impactDescription: Ensures the page complies with AMP HTML specification for Google Search features
tags: amp, validation
inputFields:
  - name: html
    required: true
    description: Raw HTML of the AMP page.
---

## AMP page must follow AMP HTML specification
Ensures the page complies with the AMP HTML specification so it can be included in Google Search features.

## Evidence to collect
- Number of validation errors reported by the official AMP validator (amp_validation_errors)

## Logic (pseudocode)
Input: html
1. Run the official AMP validator on the provided html.
2. Capture the number of errors as amp_validation_errors.
3. If amp_validation_errors == 0, the check passes; otherwise it fails.

## Pass condition
No validation errors reported by the AMP validator.

## Failure messages
- AMP validation failed with ${observed} errors; expected 0 errors.

## Examples
### Passing
Valid AMP page with no errors.
```html
<!doctype html><html amp><head><meta charset='utf-8'><script async src='https://cdn.ampproject.org/v0.js'></script></head><body>...</body></html>
```

### Failing
AMP page missing required script tag, causing validation errors.
```html
<!doctype html><html amp><head><meta charset='utf-8'></head><body>...</body></html>
```

### test case passing
```html
<!doctype html><html amp><head><meta charset='utf-8'><script async src='https://cdn.ampproject.org/v0.js'></script></head><body></body></html>
```

### test case failing
```html
<!doctype html><html amp><head><meta charset='utf-8'></head><body></body></html>
```

### References
Reference: [Guidelines for AMP on Google Search](https://developers.google.com/search/amp/validate-amp.html)