# Page Experience Diversity Checker

This script checks if at least 5 out of 7 core page experience signals pass.

## Usage

```bash
python3 page_experience_diversity.py <lighthouse_metrics_json_file>
```

## Arguments

- `lighthouse_metrics_json_file`: Path to JSON file with lighthouse metrics

## Expected JSON Format

```json
{
  "LCP": true,
  "FID": false,
  "CLS": true,
  "mobile_friendly": true,
  "safe_browsing": true,
  "https": false,
  "no_intrusive_interstitials": true
}
```

## Dependencies

No external dependencies required (uses stdlib only).

## Output

JSON result with:
- `passed`: Boolean indicating if at least 5 signals pass
- `pass_count`: Number of signals that passed
- `required_passes`: Required number of passes (5)
- `signal_results`: Individual results for each signal
- `message`: Human-readable summary

## Example

```bash
python3 page_experience_diversity.py metrics.json
```

Returns:
```json
{
  "rule_id": "PAGE_EXPERIENCE_DIVERSITY",
  "passed": true,
  "pass_count": 5,
  "required_passes": 5,
  "signal_results": {
    "LCP": true,
    "FID": true,
    "CLS": true,
    "mobile_friendly": true,
    "safe_browsing": true,
    "https": false,
    "no_intrusive_interstitials": false
  },
  "message": "Passed 5 of 7 signals (need 5)"
}
```