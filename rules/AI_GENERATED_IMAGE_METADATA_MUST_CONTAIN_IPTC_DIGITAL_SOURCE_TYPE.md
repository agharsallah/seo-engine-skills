---
title: AI-generated images must include IPTC DigitalSourceType metadata
impact: LOW
impactDescription: Ensures AI‑generated images are identifiable and comply with Google Merchant Center policies.
tags: ai, image, metadata
inputFields:
  - name: image_metadata
    required: true
    description: IPTC metadata extracted from the image file
---

## AI-generated images must include IPTC DigitalSourceType metadata
Ensures AI‑generated images are identifiable and comply with Google Merchant Center policies.

## Evidence to collect
- DigitalSourceType field presence in IPTC metadata

## Logic (pseudocode)
Inputs: image_metadata (object with IPTC fields)
Steps:
1. IF "DigitalSourceType" NOT IN image_metadata:
2.     RETURN fail
3. IF image_metadata["DigitalSourceType"] != "TrainedAlgorithmicMedia":
4.     RETURN fail
5. RETURN pass

## Pass condition
IPTC DigitalSourceType metadata exists and equals "TrainedAlgorithmicMedia"

## Failure messages
Missing IPTC DigitalSourceType metadata or value is '${observed}' instead of required 'TrainedAlgorithmicMedia'.

## Examples
### Passing
Image file contains IPTC DigitalSourceType set to TrainedAlgorithmicMedia.
```json
{
  "DigitalSourceType": "TrainedAlgorithmicMedia",
  "OtherField": "value"
}
```

### Failing
Image file lacks DigitalSourceType or has a different value.
```json
{
  "OtherField": "value"
}
```

### test case passing
```json
{"DigitalSourceType":"TrainedAlgorithmicMedia"}
```

### test case failing
```json
{}
```

### References
Reference: [Google Search's guidance on using generative AI content on your website](https://developers.google.com/search/blog/2023/02/google-search-and-ai-content)