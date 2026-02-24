# Cloaking Detection Script

This script detects cloaking by fetching content using different user agents (regular browser vs. Googlebot) and comparing content similarity.

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```bash
python scripts/cloaking-detection.py --url "https://example.com"
```

### Advanced Usage

```bash
python scripts/cloaking-detection.py \
  --url "https://example.com" \
  --similarity-threshold 0.85 \
  --request-delay 3 \
  --output-format summary
```

## Parameters

- `--url`: URL to check for cloaking (required)
- `--similarity-threshold`: Minimum content similarity threshold (0-1, default: 0.9)
- `--user-agent-regular`: Custom user agent for regular browser (optional)
- `--user-agent-googlebot`: Custom user agent for Googlebot (optional)
- `--request-delay`: Delay in seconds between requests (default: 2)
- `--output-format`: Output format - `json` (full details) or `summary` (simplified)

## Output

The script outputs JSON with:
- Content similarity score
- Whether cloaking was detected 
- Word counts for both user agents
- Sample text content
- Detailed analysis

## Example Output

```json
{
  "url": "https://example.com",
  "analysis": {
    "similarity_score": 0.95,
    "similarity_percentage": 95.0,
    "cloaking_detected": false,
    "status": "pass",
    "details": "No cloaking detected: Content similarity is 0.9500 (95.00%), above the threshold of 90.00%."
  }
}
```