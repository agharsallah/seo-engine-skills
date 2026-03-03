---
title: AI-generated product titles and descriptions must be labeled as AI-generated
impact: LOW
impactDescription: Guarantees transparency for users and compliance with Google Merchant Center AI content policies.
tags: ai, ecommerce, product
inputFields:
  - name: html
    required: true
    description: HTML source of the product page
---

## AI-generated product titles and descriptions must be labeled as AI-generated
Guarantees transparency for users and compliance with Google Merchant Center AI content policies.

## Evidence to collect
- Presence of AI‑generated labels: `meta[name='product-title'][data-ai-generated='true']` and `meta[name='product-description'][data-ai-generated='true']`

## Logic (pseudocode)
Inputs: html (string)
Steps:
1. Parse html into DOM.
2. IF meta[name='product-title'][data-ai-generated='true'] NOT FOUND:
3.     RETURN fail
4. IF meta[name='product-description'][data-ai-generated='true'] NOT FOUND:
5.     RETURN fail
6. RETURN pass

## Pass condition
Both product title and description meta tags are present with data-ai-generated="true"

## Failure messages
Missing AI‑generated label for product title or description.

## Examples
### Passing
Product page includes labeled meta tags for AI‑generated title and description.
```html
<meta name="product-title" content="Smartphone X" data-ai-generated="true">
<meta name="product-description" content="Latest model with AI features." data-ai-generated="true">
```

### Failing
Product page lacks AI‑generated labels.
```html
<meta name="product-title" content="Smartphone X">
<meta name="product-description" content="Latest model with AI features.">
```

### test case passing
```html
<meta name="product-title" content="Smartphone X" data-ai-generated="true"><meta name="product-description" content="Latest model" data-ai-generated="true">
```

### test case failing
```html
<meta name="product-title" content="Smartphone X"><meta name="product-description" content="Latest model">
```

### References
Reference: [Google Search's guidance on using generative AI content on your website](https://developers.google.com/search/blog/2023/02/google-search-and-ai-content)