
---
title: Rule Title Here
impact: MEDIUM | HIGH | LOW | CRITICAL
impactDescription: Optional description of impact (e.g., "20-50% improvement")
tags: tag1, tag2
inputFields:
  - name: html | robots_txt
    required: true | false
    description: Description of the input field and its role in the rule evaluation.
---

## Rule Title Here
If applicable, add a brief summary of why this rule matters for SEO or performance.

## Evidence to collect
- List evidence fields required for evaluation (e.g., status_code, DOM element, etc.)

## Logic (pseudocode)
Input: [inputFields]
1. Step-by-step logic for evaluating the rule
2. If [condition] -> pass; else -> fail

## Pass condition
Describe what constitutes a passing result for this rule.

## Failure messages
List or template for failure messages (e.g., "Missing <title> tag")

## Examples
### Passing
Show a passing example (code, markup, config, etc.)

### Failing
Show a failing example (code, markup, config, etc.)

### test case passing
```html
<!-- Example of passing case -->
```
### test case failing
```html
<!-- Example of failing case -->
```

### References
Reference: [Link to documentation or resource](https://example.com)
