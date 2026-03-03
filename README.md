

# SEO Engine Skills

<p align="center">
   <b>A comprehensive, deterministic technical SEO auditing skill for agents and automation.</b><br>
   <i>Evaluates on-page optimization, content structure, spam policies, and crawlability for websites and web pages.</i>
</p>

<p align="center">
   <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
   <a href="https://github.com/your-repo/seo-engine-skills"><img src="https://img.shields.io/badge/version-1.0.0-blue.svg" alt="Version"></a>
</p>

---

## 🚀 Overview

SEO Engine Skills delivers **deterministic, rule-based SEO analysis** with clear pass/fail outcomes and actionable remediation steps. Designed for agents, automation, and technical SEOs.

### ✨ Features

- 🔍 **70+ SEO Rules** across 20+ categories
- 🚫 **Spam Detection** (cloaking, hidden text, keyword stuffing)
- 🔧 **Technical Audits** (robots.txt, redirects, status codes)
- 📊 **Content Analysis** (titles, headings, alt text)
- 🎯 **Actionable Remediation** with specific fix instructions
- 🤖 **Bot vs User Testing** for cloaking detection
- ⚡ **Fast, Deterministic Results** (no heuristics)
- 📱 **AMP Validation** support

---


## ⚡ Quick Start

### Installation

```bash
npx skills add https://github.com/agharsallah/seo-engine-skills --skill seo-engine
```

### Usage

Once installed, the skill is automatically available to your agent. Just ask for an SEO audit or analysis:

**Examples:**

   Audit the SEO of https://example.com
   Analyze this HTML file for SEO compliance: page.html
   What SEO issues exist in these files: page.html, robots.txt

The agent will extract the required data and apply all relevant rules.



## 📚 Rule Categories

| Category | Example Rules | Priority Levels |
|----------|--------------|----------------|
| Technical Requirements | 4+ | Critical, High, Medium |
| Spam Policies | 4+ | High, Medium |
| Content Basics | 4+ | Low, Medium |
| Content Optimization | 4+ | Low, Medium |
| Canonicalization | 8+ | Low, Medium, High |
| A/B Testing | 3+ | Medium, High |
| URL Structure | 3+ | Medium, High |
| Security | 1+ | Critical |
| AMP Validation | 1+ | Critical |
| Dashboard Setup | 3+ | Medium |
| ...and more! | | |

See [SKILL.md](./SKILL.md) for the full list of categories and rules.

### Priority Levels

- 🚨 **Critical**: Issues that prevent indexing entirely
- ⚠️ **High**: Significant ranking/crawlability impact
- 📊 **Medium**: Important optimization opportunities
- ℹ️ **Low**: Minor improvements for best practices


### 📦 Skill Structure
- **[SKILL.md](./SKILL.md)** — Complete documentation with all rules
- **[rules/](./rules/)** — Individual rule files with examples and implementation
- **[scripts/](./scripts/)** — Automated detection utilities

#### Rule File Format
Each rule file includes:
- **Why it matters** — SEO impact explanation
- **Incorrect example** — What not to do
- **Correct example** — Proper implementation
- **Additional context** — References and best practices


## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-rule`
3. Follow the rule template in [`rules/_template.md`](./rules/_template.md)
4. Add tests for new detection scripts
5. Submit a pull request

#### Rule Template
```markdown
# Rule Name
## Why This Matters
## Incorrect Example
## Correct Example
## Additional Context
```


## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👤 Author

**Abderrahmen Gharsallah** — *Initial work*

---

For detailed implementation guides and the complete rule set, see [SKILL.md](./SKILL.md).