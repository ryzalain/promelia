# 🚀 Promelia
> **The fully autonomous, AI-driven job application agent.**
> Discover, score, tailor, and apply to roles—completely hands-free.

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL%203.0-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![GitHub Stars](https://img.shields.io/github/stars/ryzalain/Promelia?style=social)](https://github.com/ryzalain/Promelia)

---

## ✨ How It Works

Promelia operates a relentless, 6-stage autonomous pipeline designed to secure interviews while you sleep:

| Stage | Action | Description |
| :--- | :--- | :--- |
| 🔍 | **Discover** | Scrapes 5+ major job boards (Indeed, LinkedIn, Glassdoor, etc.) + 48 Workday portals + 30 direct career sites. |
| 🧠 | **Enrich** | Extracts full job descriptions using structured data, CSS selectors, or AI fallback. |
| ⭐ | **Score** | AI rates the job fit (1–10) strictly against your resume and personal preferences. |
| 📝 | **Tailor** | Dynamically rewrites your resume for *each specific job*—emphasizing relevant experience without fabricating facts. |
| 💌 | **Cover Letter** | Drafts hyper-targeted cover letters tailored to the company and role. |
| 🤖 | **Auto-Apply** | Browser automation seamlessly fills forms, uploads documents, answers screening questions, and submits the application. |

---

## ⚡ Quick Start

### Prerequisites
* **Python 3.11+**
* **Node.js 18+** (Required for the auto-apply browser automation)
* **Google Chrome**
* **[Gemini API key](https://aistudio.google.com)** (Free tier supported)

### Installation
```bash
# 1. Install Promelia
pip install promelia

# 2. Install dependencies (Bypassing strict resolver conflicts)
pip install --no-deps python-jobspy 
pip install pydantic tls-client requests markdownify regex
```

### Setup & Execution
```bash
# Initialize your profile, resume, and API keys
promelia init      

# Verify your environment is ready
promelia doctor    

# Launch the full autonomous pipeline
promelia run              

# Launch browser-driven auto-submission
promelia apply 
```

---

## 📋 CLI Command Reference

| Command | Function |
| :--- | :--- |
| `promelia init` | Launch the first-time setup wizard. |
| `promelia doctor` | Diagnose and fix missing system requirements. |
| `promelia run` | Execute the discovery, scoring, and tailoring stages. |
| `promelia run -w 4` | Run discovery and enrichment with 4 parallel workers. |
| `promelia apply` | Launch the browser automation to submit applications. |
| `promelia apply --dry-run` | Fill out application forms without hitting submit. |
| `promelia dashboard` | Open the HTML dashboard to view application results. |

---

## 🛡️ License & Attribution

This project is licensed under the GNU Affero General Public License v3.0 (AGPL-3.0).

Originally based on ApplyPilot by Pickle-Pixel. You are free to use, modify, and distribute this software. However, if you deploy a modified version of this software as a service over a network, you must release your complete source code under the same AGPL-3.0 license.
