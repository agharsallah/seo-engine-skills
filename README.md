# SEO Engine Skills


> A comprehensive technical SEO auditing skill that evaluates on-page optimization, content structure, spam policies, and crawlability for websites and web pages.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/your-repo/seo-engine-skills)

## Overview

The SEO Engine Skills
 provides **deterministic, rule-based SEO analysis** with clear pass/fail outcomes and actionable remediation steps.

### Key Features

- 🔍 **40+ SEO Rules** across 12 categories
- 🚫 **Spam Detection** (cloaking, hidden text, keyword stuffing)
- 🔧 **Technical Audits** (robots.txt, redirects, status codes)
- 📊 **Content Analysis** (titles, headings, alt text)
- 🎯 **Clear Remediation** with specific fix instructions
- 🤖 **Bot vs User Testing** for cloaking detection
- 📱 **AMP Validation** support

## Quick Start

### Installation

1. **Add the skill:**
   ```bash
   npx skills add https://github.com/agharsallah/seo-engine-skills --skill seo-engine
   ```

2. **Set up Python environment:**
   ```bash
   cd scripts/cloaking_detection
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

### Basic Usage

Skills are automatically available once installed. The agent will use them when relevant tasks are detected. For example, if the agent is asked to audit a website's SEO, it will apply the relevant rules from this skill.

**Examples:**
```
Audit the SEO of https://example.com
```

## Rule Categories

| Category | Rules | Priority Levels |
|----------|--------|----------------|
| **Technical Requirements** | 4 rules | Critical, High, Medium |
| **Spam Policies** | 4 rules | High, Medium |
| **Content Basics** | 4 rules | Low, Medium |
| **Content Optimization** | 4 rules | Low, Medium |
| **Canonicalization** | 8 rules | Low, Medium, High |
| **A/B Testing** | 3 rules | Medium, High |
| **URL Structure** | 3 rules | Medium, High |
| **Security** | 1 rule | Critical |
| **AMP Validation** | 1 rule | Critical |
| **Dashboard Setup** | 3 rules | Medium |

### Priority Levels

- 🚨 **Critical**: Issues that prevent indexing entirely
- ⚠️ **High**: Significant ranking/crawlability impact
- 📊 **Medium**: Important optimization opportunities
- ℹ️ **Low**: Minor improvements for best practices

### Skill Structure
- 📋 **[SKILL.md](./SKILL.md)** - Complete skill documentation with all 40+ rules
- 📁 **[rules/](./rules/)** - Individual rule files with examples and implementation
- 🛠️ **[scripts/](./scripts/)** - Automated detection utilities

### Rule File Structure
Each rule file contains:
- ✅ **Why it matters** - SEO impact explanation
- ❌ **Incorrect example** - What not to do
- ✅ **Correct example** - Proper implementation
- 🔗 **Additional context** - References and best practices

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-rule`
3. Follow the rule template in [`rules/_template.md`](./rules/_template.md)
4. Add tests for new detection scripts
5. Submit a pull request

### Adding New Rules

Use the template structure:
```markdown
# Rule Name
## Why This Matters
## Incorrect Example
## Correct Example  
## Additional Context
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Abderrahmen Gharsallah** - *Initial work*

---

For detailed implementation guides and complete rule specifications, see [SKILL.md](./SKILL.md).