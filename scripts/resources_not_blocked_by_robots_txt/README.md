# Resources Not Blocked by robots.txt Checker

This script checks if page resources (images, CSS, JavaScript) are blocked by robots.txt.

## Usage

```bash
python3 resources_not_blocked_by_robots_txt.py <html_file> <robots_txt_file>
```

## Arguments

- `html_file`: Path to HTML file to analyze
- `robots_txt_file`: Path to robots.txt file

## Dependencies

```bash
pip install beautifulsoup4 lxml
```

## Output

JSON result with:
- `passed`: Boolean indicating if all resources are allowed
- `total_resources`: Total number of resources found
- `blocked_resources`: List of URLs blocked by robots.txt
- `message`: Human-readable summary

## Example

```bash
python3 resources_not_blocked_by_robots_txt.py page.html robots.txt
```

Returns:
```json
{
  "rule_id": "RESOURCES_NOT_BLOCKED_BY_ROBOTS_TXT",
  "passed": false,
  "total_resources": 5,
  "blocked_resources": [
    "/js/analytics.js"
  ],
  "message": "Found 1 blocked resources out of 5 total"
}
```