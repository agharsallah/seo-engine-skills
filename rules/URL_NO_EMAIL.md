---
title: URLs must not contain email addresses
impact: MEDIUM
impactDescription: Prevents email addresses from being indexed and exposing personal information
tags: redaction, url_privacy
inputFields:
  - name: url
    required: true
    description: The full URL of the page being evaluated
---

## URLs must not contain email addresses
Email addresses in URLs can be indexed and expose personal information.

## Evidence to collect
- Regex: url (Detects patterns like user@example.com in the URL)

## Logic (pseudocode)
Inputs: url
1. Define regex pattern for email addresses: [A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}
2. If regex matches any substring of url:
      result = fail
   else:
      result = pass

## Pass condition
URL does not contain any substring matching an email address pattern.

## Failure messages
- URL contains an email address; observed: ${observed}

## Examples
### Passing
URL without email
```
https://example.com/report/2024-summary
```

### Failing
URL containing an email address
```
https://example.com/user/jane.doe@example.com/report
```

### test case passing
```
https://example.com/report/2024-summary
```

### test case failing
```
https://example.com/user/jane.doe@example.com/report
```

### References
Reference: [Keep redacted information out of Google Search](https://developers.google.com/search/docs/keep-redacted-info)