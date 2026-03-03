---
title: Verify user has required Search Console role for URL Inspection indexing request
impact: HIGH
impactDescription: The documentation states that a user must be an owner or full user of the Search Console property to request indexing via the URL Inspection tool
tags: search_console, url_inspection, access_control
inputFields:
  - name: search_console_user_role
    required: true
    description: Role of the user in the Search Console property (e.g., owner, full_user, restricted_user)
---

## Verify user has required Search Console role for URL Inspection indexing request
The documentation states that a user must be an owner or full user of the Search Console property to request indexing via the URL Inspection tool.

## Evidence to collect
- Attribute: search_console_user_role (Role value retrieved from Search Console API or UI)

## Logic (pseudocode)
Input: search_console_user_role
1. Define allowed_roles = ["owner", "full_user"]
2. If search_console_user_role is in allowed_roles, result = pass
3. Else result = fail

## Pass condition
User role is either "owner" or "full_user".

## Failure messages
- User role ${observed} is not sufficient; required role is owner or full_user.

## Examples
### Passing
User is an owner of the Search Console property.
```
search_console_user_role: "owner"
```

### Failing
User is a restricted user and cannot request indexing.
```
search_console_user_role: "restricted_user"
```

### test case passing
```json
{
  "search_console_user_role": "owner"
}
```

### test case failing
```json
{
  "search_console_user_role": "restricted_user"
}
```

### References
Reference: [Ask Google to Recrawl Your Website](https://developers.google.com/search/docs/monitoring/recrawl)