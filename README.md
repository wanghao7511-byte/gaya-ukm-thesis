# Gaya UKM (2015) Thesis Writing & Formatting Skill (Multi-Platform)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Style: Gaya UKM 2015](https://img.shields.io/badge/Standard-Gaya%20UKM%20(2015)-blue.svg)](https://www.ukm.my/pusatsiswazah/)
[![Platforms: ChatGPT | Claude | WorkBuddy | Antigravity](https://img.shields.io/badge/Platforms-ChatGPT%20|%20Claude%20|%20WorkBuddy%20|%20Antigravity-success.svg)](#multi-platform-adaptation-guide)

An authoritative, multi-platform AI assistant skill and automated compliance linter strictly implementing the **Universiti Kebangsaan Malaysia (UKM) Thesis Writing Style Guide (*Gaya UKM 2015*)** published by the **UKM Graduate Centre (Pusat Pengajian Siswazah)**.

---

## 🌟 Overview / 项目概述 / Gambaran Keseluruhan

### English
Writing and formatting a Master's or PhD thesis at UKM requires strict adherence to institutional guidelines. Formatting errors (such as commas inside parenthetical citations, bracketed years in reference lists, improper headings, or non-compliant margins) frequently cause delays during proposal defense, external viva examination, and final hard-cover submission.

This repository packages the entire 129-page *Gaya UKM (2015)* official manual into an **all-in-one, multi-platform toolkit** ready for deployment across:
* 🤖 **ChatGPT** (Custom GPTs / Projects)
* 🧠 **Claude** (Claude Projects / Claude Code / Claude Desktop)
* 💼 **WorkBuddy** (Enterprise Assistant / 腾讯/钉钉智能助手)
* 🚀 **Antigravity / Gemini CLI** (Native Agentic Skill)
* 🐍 **Python CLI** (Automated manuscript compliance linter)

### Bahasa Melayu
Penulisan dan pemformatan tesis ijazah Sarjana atau Doktor Falsafah (PhD / DBA) di Universiti Kebangsaan Malaysia (UKM) memerlukan pematuhan yang ketat terhadap garis panduan rasmi universiti. Kesilapan format lazim—seperti meletakkan tanda koma di dalam kurungan sitasi teks `(Pengarang, 2020)`, meletakkan tanda kurungan pada tahun di senarai rujukan `Pengarang (2020).`, tajuk peringkat keempat memasuki jadual kandungan, kemunculan garis menegak pada jadual, serta ketidakpatuhan margin—sering mengakibatkan kelewatan dalam pembentangan cadangan penyelidikan (proposal defense), peperiksaan lisan (viva-voce), dan penyerahan jilid kulit keras (hard cover) akhir.

Repositori ini merumuskan keseluruhan manual rasmi **Gaya UKM (2015)** setebal 129 muka surat yang diterbitkan oleh **Pusat Pengajian Siswazah UKM** ke dalam satu **pakej perkakasan AI pelbagai platform** yang sedia digunakan untuk:
* 🤖 **ChatGPT** (Arahan tersuai Custom GPTs / ChatGPT Projects & pakej pangkalan pengetahuan)
* 🧠 **Claude** (Arahan berstruktur Claude Projects, Claude Desktop & Claude Code CLI)
* 💼 **WorkBuddy** (Tetapan peranan pembantu kerja perusahaan & pangkalan pengetahuan 15 kad Soal Jawab)
* 🚀 **Antigravity / Gemini CLI** (Kemahiran ejen pintar / Agentic Skill)
* 🐍 **Python CLI** (Skrip audit kepatuhan manuskrip automatik `check_gaya_ukm.py`)

### 中文概述
在马来西亚国民大学（UKM）撰写硕士（Master）或博士（PhD / DBA）学位论文及开题报告（Proposal）时，必须 100% 严格执行校方官方规范。诸如正文括号引用中误加逗号 `(Author, 2020)`、参考文献列表年份误带括号 `Author (2020).`、四级标题非法进入目录、表格出现纵向竖线以及页边距不合规等典型格式错误，往往会导致开题被拒、送审答辩（Viva Voce）延误以及最终精装本（Hard Cover）归档受阻。

本项目将 UKM 研究生院（Pusat Pengajian Siswazah）颁布的 **129 页官方《Gaya UKM 2015》权威指南**完整提炼与结构化重构，打造了一套**跨平台、开箱即用的 AI 论文写作辅助与格式审查工具包**，已全面适配：
* 🤖 **ChatGPT**（自定义 GPTs / ChatGPT Projects 知识库与预设指令）
* 🧠 **Claude**（Claude Projects 结构化指令、Claude Desktop 与 Claude Code CLI）
* 💼 **WorkBuddy**（企业级 AI 工作助手角色设定与 15 组结构化问答知识库）
* 🚀 **Antigravity / Gemini CLI**（原生智能体专业技能库）
* 🐍 **Python CLI**（本地一键全自动文稿合规性审查脚本 `check_gaya_ukm.py`）

---

## 📁 Repository Structure

```text
gaya-ukm-thesis/
├── README.md                           # Main documentation & multi-platform deployment guide
├── LICENSE                             # MIT License
├── CLAUDE.md                           # Direct configuration for Claude Code / Claude Desktop
├── SKILL.md                            # Antigravity / Agentic IDE skill manifest
├── references/                         # In-depth technical specifications
│   ├── formatting-specifications.md    # Margins, fonts, spacing, pagination, cover & spine
│   ├── structure-and-layout.md         # 14-item sequence, title pages, abstracts, heading levels
│   └── citation-and-references.md      # Author-Date rules & 50+ real reference templates
├── platforms/                          # Platform-specific prompt & configuration packs
│   ├── chatgpt/
│   │   ├── custom-gpt-instructions.md  # Copy-paste prompt for ChatGPT Custom GPT Builder
│   │   ├── conversation-starters.md    # Recommended starter questions
│   │   └── gaya-ukm-knowledge-pack.md  # Single consolidated file for GPT Knowledge Base upload
│   ├── claude/
│   │   └── project-instructions.md     # XML-optimized prompt for Claude Project Instructions
│   └── workbuddy/
│       ├── system-prompt.md            # WorkBuddy role definition & response template
│       └── qa-knowledge-base.md        # 15 high-frequency Q&A cards for knowledge base import
├── scripts/
│   └── check_gaya_ukm.py               # Automated Python compliance checker
└── examples/
    ├── sample_chapter_before.md        # Chapter draft containing typical violations
    └── sample_chapter_after.md         # 100% compliant corrected sample
```

---

## 🚀 Multi-Platform Adaptation Guide

### 1. 🤖 ChatGPT (Custom GPT or Project)
1. Go to **ChatGPT** -> **Explore GPTs** -> **Create**.
2. In the **Configure** tab:
   * **Name**: `Gaya UKM Thesis Assistant (2015)`
   * **Description**: Copy from [`platforms/chatgpt/conversation-starters.md`](./platforms/chatgpt/conversation-starters.md).
   * **Instructions**: Copy the entire text from [`platforms/chatgpt/custom-gpt-instructions.md`](./platforms/chatgpt/custom-gpt-instructions.md).
   * **Conversation Starters**: Add the 4 prompts from [`platforms/chatgpt/conversation-starters.md`](./platforms/chatgpt/conversation-starters.md).
   * **Knowledge**: Click **Upload files** and select [`platforms/chatgpt/gaya-ukm-knowledge-pack.md`](./platforms/chatgpt/gaya-ukm-knowledge-pack.md).
   * **Capabilities**: Check *Code Interpreter* and *Web Browsing*.
3. Click **Save / Publish**.

---

### 2. 🧠 Claude (Claude Projects & Claude Desktop / Code)

#### Option A: Claude Projects (Web)
1. In Claude.ai, create a new **Project** named `Gaya UKM Thesis Assistant`.
2. Click **Set Project Instructions** and paste the contents of [`platforms/claude/project-instructions.md`](./platforms/claude/project-instructions.md).
3. In **Project Knowledge**, upload the files inside [`references/`](./references/).

#### Option B: Claude Code CLI / Claude Desktop
If you are using Claude Code CLI or Claude Desktop in project mode, it will automatically detect and load [`CLAUDE.md`](./CLAUDE.md) located at the root of this repository.

---

### 3. 💼 WorkBuddy (企业级 AI / 办公助手)
1. 在 WorkBuddy / 腾讯工作助手 / 钉钉助手 中创建“新智能体 / 专家助手”。
2. **角色设定 / 系统提示词**：复制粘贴 [`platforms/workbuddy/system-prompt.md`](./platforms/workbuddy/system-prompt.md) 的内容。
3. **知识库挂载**：在助手知识库配置中，将 [`platforms/workbuddy/qa-knowledge-base.md`](./platforms/workbuddy/qa-knowledge-base.md) 作为问答知识库导入。
4. 保存后即可在日常写作时一键调用审核与排版功能。

---

### 4. 🚀 Antigravity / Gemini CLI
Copy the repository into your skills directory:
```bash
# Global installation (available across all projects)
mkdir -p ~/.gemini/config/skills/gaya-ukm-thesis
cp -r . ~/.gemini/config/skills/gaya-ukm-thesis/

# Or workspace-level installation
mkdir -p .agents/skills/gaya-ukm-thesis
cp -r . .agents/skills/gaya-ukm-thesis/
```
The agent will automatically trigger the skill whenever UKM thesis writing or formatting is mentioned.

---

## ⚡ Core Rules Quick Reference (Gaya UKM 2015)

| Specification | Gaya UKM Standard | Common Mistake to Avoid |
| :--- | :--- | :--- |
| **In-Text Parentheses** | `(Author 2020)` | ❌ `(Author, 2020)` (NO comma inside parentheses) |
| **Author Conjunction** | `Author & Author (2020)` in brackets; `and` in prose | ❌ `(Author and Author 2020)` |
| **Reference Year** | `Author. 2020.` | ❌ `Author. (2020).` (NO parentheses around year) |
| **Reference Spacing** | Single-spaced within entry, hanging indent `12.5 mm` | ❌ 1.5 spacing or missing hanging indent |
| **Heading Hierarchy** | Max 5 levels (`1.1.1` max decimal); TOC stops at Level 3 | ❌ `1.1.1.1` (Forbidden) |
| **Margins** | Top `30 mm`, Bottom `25 mm`, Left `38 mm`, Right `25 mm` | ❌ Using default 1-inch (25.4 mm) Word margins |
| **Chapter Opening Drop** | `50 mm` from top edge | ❌ Starting directly at 30 mm top margin |
| **Typography** | Times New Roman (12 pt body, 11 pt headings, 10 pt tables) | ❌ Mixing Arial or Calibri |
| **Table Layout** | Title ABOVE table (10 pt), 3-line table, no vertical lines | ❌ Title below table, or gridlines present |
| **Figure Layout** | Title BELOW figure (10 pt), text referral precedes figure | ❌ Title above figure, or figure before text |

---

## 🛠️ Automated Python Linter Tool

This repository includes a standalone Python checker in [`scripts/check_gaya_ukm.py`](./scripts/check_gaya_ukm.py) that inspects Markdown, LaTeX, or plain-text chapters for typical UKM violations.

### Usage
```bash
python3 scripts/check_gaya_ukm.py path/to/chapter.md
```

### Try with the Example Files
```bash
# Test on file with typical formatting errors
python3 scripts/check_gaya_ukm.py examples/sample_chapter_before.md

# Test on 100% compliant file
python3 scripts/check_gaya_ukm.py examples/sample_chapter_after.md
```

---

## 📤 How to Push this Repository to GitHub

```bash
# 1. Navigate to the repository directory
cd gaya-ukm-thesis

# 2. Initialize Git (if not already initialized)
git init

# 3. Add all files and make initial commit
git add .
git commit -m "Initial commit: Multi-platform Gaya UKM 2015 Thesis Skill"

# 4. Link to your GitHub remote repository (replace with your repo URL)
git remote add origin https://github.com/<your-username>/gaya-ukm-thesis.git

# 5. Push to GitHub
git branch -M main
git push -u origin main
```

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

Official guidelines reference: *UKM Thesis Writing Style (Gaya UKM 2015)*, Pusat Pengajian Siswazah, Universiti Kebangsaan Malaysia.
