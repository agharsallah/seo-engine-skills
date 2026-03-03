---
title: Validate allowed rel attribute values on outbound links
impact: LOW
impactDescription: Ensures that rel attributes use only documented values so Google can interpret link qualifications correctly
tags: outbound_links, rel_attribute
inputFields:
  - name: html
    required: true
    description: The full HTML source of the page to be inspected.
---

## Validate allowed rel attribute values on outbound links
Ensures that rel attributes on &lt;a&gt; elements use only the values documented (sponsored, ugc, nofollow) so Google can interpret link qualifications correctly.

## Evidence to collect
- Attribute: a[rel] (Collect the value of the rel attribute from each &lt;a&gt; tag.)

## Logic (pseudocode)
Inputs: html
Steps:
1. Parse the HTML document.
2. For each &lt;a&gt; element that has a rel attribute:
   a. Retrieve the rel attribute value.
   b. Split the value on whitespace to get individual tokens.
   c. For each token, check if it is in the allowed set {"sponsored", "ugc", "nofollow"}.
   d. If any token is not in the allowed set, record a failure with the observed token.
3. If no disallowed tokens were found, the check passes.

## Pass condition
All rel attribute tokens on &lt;a&gt; elements are within the allowed set {sponsored, ugc, nofollow}.

## Failure messages
- Disallowed rel value '${observed}' found in &lt;a&gt; tag.

## Examples
### Passing
&lt;a&gt; tag with allowed rel values.
```html
<a href="https://example.com" rel="sponsored">Sponsored Link</a>
```

### Failing
&lt;a&gt; tag with a disallowed rel value.
```html
<a href="https://example.com" rel="external">External Link</a>
```

### test case passing
```html
<p>Check <a href="https://example.com" rel="ugc">User Content</a></p>
```

### test case failing
```html
<p>Check <a href="https://example.com" rel="external">External Link</a></p>
```

### References
Reference: [Qualify Outbound Links for SEO](https://developers.google.com/search/docs/links/outbound-links)