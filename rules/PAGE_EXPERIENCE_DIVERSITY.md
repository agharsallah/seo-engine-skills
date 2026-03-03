---
title: Avoid focusing on only one or two aspects of page experience
impact: MEDIUM
impactDescription: Google advises site owners not to focus on only one or two aspects of page experience, but to provide an overall great experience across many signals.
tags: page_experience, seo, guideline
inputFields:
  - name: lighthouse_metrics
    required: true
    description: Lighthouse performance metrics including core web vitals and other page‑experience signals.
---

## Avoid focusing on only one or two aspects of page experience
Google advises site owners not to focus on only one or two aspects of page experience, but to provide an overall great experience across many signals.

## Evidence to collect
- Pass/fail for each core page‑experience signal: LCP, FID, CLS, mobile_friendly, safe_browsing, https, no_intrusive_interstitials

## Logic (pseudocode)
Inputs: lighthouse_metrics (object with boolean fields for each signal)
Steps:
1. Define signals = [LCP, FID, CLS, mobile_friendly, safe_browsing, https, no_intrusive_interstitials].
2. Initialize pass_count = 0.
3. For each signal in signals:
     if lighthouse_metrics[signal] == true:
         pass_count += 1
4. If pass_count >= 5 then result = "pass" else result = "fail".

## Pass condition
At least five of the seven core page‑experience signals have passing scores.

## Failure messages
Only ${observed} of the required 5 page‑experience signals passed.

## Examples
### Passing
All core web vitals and other signals pass.
```
lighthouse_metrics:
  LCP: true
  FID: true
  CLS: true
  mobile_friendly: true
  safe_browsing: true
  https: true
  no_intrusive_interstitials: true
```

### Failing
Only two signals pass, indicating narrow focus.
```
lighthouse_metrics:
  LCP: true
  FID: false
  CLS: false
  mobile_friendly: true
  safe_browsing: false
  https: false
  no_intrusive_interstitials: false
```

### test case passing
```
LCP: Pass, FID: Pass, CLS: Pass, Mobile: Pass, Safe: Pass, HTTPS: Fail, Interstitials: Fail
```

### test case failing
```
LCP: Pass, FID: Fail, CLS: Fail, Mobile: Fail, Safe: Fail, HTTPS: Fail, Interstitials: Fail
```

### References
Reference: [Provide a great page experience](https://developers.google.com/search/docs/advanced/guidelines/content)