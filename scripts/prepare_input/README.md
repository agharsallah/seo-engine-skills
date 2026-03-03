# SEO Engine Input Preparation Scripts

This directory contains scripts to extract and prepare data from websites for SEO analysis. Each script handles a specific type of input data needed by the SEO engine rules.

## Overview

When analyzing a website URL, you need several types of data:

1. **HTML Content** - The actual webpage source code
2. **robots.txt** - Crawling permissions and restrictions
3. **Sitemap** - List of URLs the site wants crawled

## Scripts

### fetch_html.py
Extracts HTML content from a webpage.

**Usage:**
```bash
python fetch_html.py <url> [output_file]
```

**Examples:**
```bash
python fetch_html.py https://example.com
python fetch_html.py example.com
python fetch_html.py https://example.com custom_page.html
```

**Output:** HTML file containing the webpage source code


### fetch_robots_txt.py
Downloads the robots.txt file from a domain.

**Usage:**
```bash
python fetch_robots_txt.py <url> [output_file]
```

**Examples:**
```bash
python fetch_robots_txt.py https://example.com
python fetch_robots_txt.py example.com
python fetch_robots_txt.py https://example.com custom_robots.txt
```

**Output:** robots.txt file with crawling rules

**Behavior:**
- HTTP 200: Saves actual robots.txt content
- HTTP 404: Creates placeholder indicating "allow all"
- Other errors: Documents the error in output file

### fetch_sitemap.py
Finds and downloads the sitemap.xml file.

**Usage:**
```bash
python fetch_sitemap.py <url> [output_file]
```

**Examples:**
```bash  
python fetch_sitemap.py https://example.com
python fetch_sitemap.py example.com custom_sitemap.xml
```

**Output:** XML sitemap file

**Discovery Method:**
1. Checks robots.txt for Sitemap: declarations
2. Tries common locations:
   - /sitemap.xml
   - /sitemap_index.xml
   - /sitemap.xml.gz
   - /sitemaps/sitemap.xml
   - /sitemaps.xml

## Quick Start - Analyze a Website

To prepare all inputs for SEO analysis of a website:

```bash
# Set target URL
URL="https://example.com"

# Fetch all required data
python fetch_html.py $URL
python fetch_robots_txt.py $URL  
python fetch_sitemap.py $URL

# Files created:
# - example.com.html
# - example.com_robots.txt
# - example.com_sitemap.xml
```

## Integration with SEO Rules

Once you have the input files, you can apply SEO rules:

```bash
# Example: Check if resources are blocked by robots.txt
python ../resources_not_blocked_by_robots_txt/resources_not_blocked_by_robots_txt.py example.com.html example.com_robots.txt

# Example: Check favicon dimensions
python ../favicon_dimensions/favicon_dimensions.py example.com.html
```

## Dependencies

Install required Python packages:
```bash
pip install requests
```


## Error Handling

All scripts handle common error scenarios gracefully:

- **Network timeouts**: Configurable timeouts for web requests
- **Missing files**: Create placeholder files when resources don't exist
- **Invalid responses**: Document errors in output files for analysis
- **Missing dependencies**: Clear error messages with installation instructions

## Output Files

All scripts generate files in the current directory by default. File names are auto-generated based on the domain name unless explicitly specified.

**Naming Convention:**
- HTML: `domain.com.html`
- Robots: `domain.com_robots.txt`  
- Sitemap: `domain.com_sitemap.xml`

## Advanced Usage

### Batch Processing
```bash
# Process multiple URLs
for url in "site1.com" "site2.com" "site3.com"; do
    python fetch_html.py $url
    python fetch_robots_txt.py $url
    python fetch_sitemap.py $url
done
```

### Custom Output Directory  
```bash
mkdir analysis_output
cd analysis_output
python ../fetch_html.py example.com
# Files will be created in analysis_output/
```

### Using with SEO Engine
After preparing inputs, run the full SEO analysis using the main SEO engine with these prepared files as input data.