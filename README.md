# Gaya UKM Thesis Writing & Formatting Skill (Multi-Platform)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Style: Gaya UKM 2015](https://img.shields.io/badge/Standard-Gaya%20UKM%20(2015)-blue.svg)](https://www.ukm.my/pusatsiswazah/)
[![Regulations: UKM Pascasiswazah 2026](https://img.shields.io/badge/Regulations-UKM%20Pascasiswazah%202026-brightgreen.svg)](https://www.ukm.my/pusatsiswazah/)
[![Platforms: ChatGPT | Claude | WorkBuddy | Antigravity](https://img.shields.io/badge/Platforms-ChatGPT%20|%20Claude%20|%20WorkBuddy%20|%20Antigravity-success.svg)](#multi-platform-adaptation-guide)

An authoritative, multi-platform AI assistant skill and automated compliance linter strictly implementing the **Universiti Kebangsaan Malaysia (UKM) Thesis Writing Style Guide (*Gaya UKM 2015*)**, updated with the **Kaedah-Kaedah & Peraturan-Peraturan UKM (Pengajian Pascasiswazah) 2026** and the latest **GayaUKM-rev15** official institutional templates published by the **UKM Graduate Centre (Pusat Pengajian Siswazah)**.

---

## 🌟 Overview / 项目概述 / Gambaran Keseluruhan

### English
Writing and formatting a Master's or PhD thesis at UKM requires strict adherence to institutional guidelines. Formatting errors (such as commas inside parenthetical citations, bracketed years in reference lists, improper headings, or non-compliant margins) frequently cause delays during proposal defense, external viva examination, and final hard-cover submission.

This repository packages the entire 129-page *Gaya UKM (2015)* official manual, the statutory **Kaedah-Kaedah & Peraturan-Peraturan UKM (Pengajian Pascasiswazah) 2026** (covering WoS/Scopus publication quotas, 3-month submission notices, Turnitin clearance, and Compilation Thesis options), and the latest **GayaUKM-rev15 Word templates** into an **all-in-one, multi-platform toolkit** ready for deployment across:
* 🤖 **ChatGPT** (Custom GPTs / Projects)
* 🧠 **Claude** (Claude Projects / Claude Code / Claude Desktop)
* 💼 **WorkBuddy** (Enterprise Assistant / 腾讯/钉钉智能助手)
* 🚀 **Antigravity / Gemini CLI** (Native Agentic Skill)
* 🐍 **Python CLI** (Automated manuscript compliance linter)

### Bahasa Melayu
Penulisan dan pemformatan tesis ijazah Sarjana atau Doktor Falsafah (PhD / DBA) di Universiti Kebangsaan Malaysia (UKM) memerlukan pematuhan yang ketat terhadap garis panduan rasmi universiti. Kesilapan format lazim—seperti meletakkan tanda koma di dalam kurungan sitasi teks `(Pengarang, 2020)`, meletakkan tanda kurungan pada tahun di senarai rujukan `Pengarang (2020).`, tajuk peringkat keempat memasuki jadual kandungan, kemunculan garis menegak pada jadual, serta ketidakpatuhan margin—sering mengakibatkan kelewatan dalam pembentangan cadangan penyelidikan (proposal defense), peperiksaan lisan (viva-voce), dan penyerahan jilid kulit keras (hard cover) akhir.

Repositori ini merumuskan manual rasmi **Gaya UKM (2015)**, **Kaedah-Kaedah & Peraturan-Peraturan UKM (Pengajian Pascasiswazah) 2026** (termasuk syarat penerbitan WoS/Scopus, notis 3 bulan penyerahan tesis, perakuan bebas plagiat Turnitin, dan Format Kompilasi), serta templat rasmi Word **GayaUKM-rev15** ke dalam satu **pakej perkakasan AI pelbagai platform** yang sedia digunakan untuk:
* 🤖 **ChatGPT** (Arahan tersuai Custom GPTs / ChatGPT Projects & pakej pangkalan pengetahuan)
* 🧠 **Claude** (Arahan berstruktur Claude Projects, Claude Desktop & Claude Code CLI)
* 💼 **WorkBuddy** (Tetapan peranan pembantu kerja perusahaan & pangkalan pengetahuan 19 kad Soal Jawab)
* 🚀 **Antigravity / Gemini CLI** (Kemahiran ejen pintar / Agentic Skill)
* 🐍 **Python CLI** (Skrip audit kepatuhan manuskrip automatik `check_gaya_ukm.py`)

### 中文概述
在马来西亚国民大学（UKM）撰写硕士（Master）或博士（PhD / DBA）学位论文及开题报告（Proposal）时，必须 100% 严格执行校方官方规范。诸如正文括号引用中误加逗号 `(Author, 2020)`、参考文献列表年份误带括号 `Author (2020).`、四级标题非法进入目录、表格出现纵向竖线以及页边距不合规等典型格式错误，往往会导致开题被拒、送审答辩（Viva Voce）延误以及最终精装本（Hard Cover）归档受阻。

本项目将 UKM 研究生院（Pusat Pengajian Siswazah）颁布的 **《Gaya UKM 2015》权威指南**、最新的 **《Kaedah-Kaedah & Peraturan-Peraturan UKM (Pengajian Pascasiswazah) 2026》研究生规章条例**（涵盖 WoS/Scopus 毕业发表硬指标、提前 3 个月提交送审通知、Turnitin 查重认证、发表汇编型论文 Format Kompilasi 等）以及官方最新的 **GayaUKM-rev15 Word 模板细则**（严禁设立单独献词页、摘要四项禁令等）完整提炼与结构化重构，打造了一套**跨平台、开箱即用的 AI 论文写作辅助与格式审查工具包**，已全面适配：
* 🤖 **ChatGPT**（自定义 GPTs / ChatGPT Projects 知识库与预设指令）
* 🧠 **Claude**（Claude Projects 结构化指令、Claude Desktop 与 Claude Code CLI）
* 💼 **WorkBuddy**（企业级 AI 工作助手角色设定与 19 组高频问答知识库）
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
│   ├── ukm-postgraduate-regulations-2026.md # 2026 UKM bylaws, WoS/Scopus quotas, 3-month notice, Turnitin
│   ├── formatting-specifications.md    # Margins, fonts, spacing, pagination, cover & spine
│   ├── structure-and-layout.md         # 14-item sequence, title pages, abstracts, rev15 Word styles
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
│       └── qa-knowledge-base.md        # 19 high-frequency Q&A cards for knowledge base import
├── scripts/
│   └── check_gaya_ukm.py               # Automated Python compliance checker (abstract citation check)
└── examples/
    ├── sample_chapter_before.md        # Chapter draft containing typical violations
    └── sample_chapter_after.md         # 100% compliant corrected sample
```

---

## 🚀 Multi-Platform Adaptation Guide / 多平台部署适配指南

### 1. 🤖 ChatGPT (Custom GPT or Project / 自定义 GPT 与项目)

**English Steps**:
1. Go to **ChatGPT** -> **Explore GPTs** -> **Create**.
2. In the **Configure** tab:
   * **Name**: `Gaya UKM Thesis Assistant (2015)`
   * **Description**: Copy from [`platforms/chatgpt/conversation-starters.md`](./platforms/chatgpt/conversation-starters.md).
   * **Instructions**: Copy the entire text from [`platforms/chatgpt/custom-gpt-instructions.md`](./platforms/chatgpt/custom-gpt-instructions.md).
   * **Conversation Starters**: Add the 4 prompts from [`platforms/chatgpt/conversation-starters.md`](./platforms/chatgpt/conversation-starters.md).
   * **Knowledge**: Click **Upload files** and select [`platforms/chatgpt/gaya-ukm-knowledge-pack.md`](./platforms/chatgpt/gaya-ukm-knowledge-pack.md).
   * **Capabilities**: Check *Code Interpreter* and *Web Browsing*.
3. Click **Save / Publish**.

**中文配置指南**:
1. 登录 **ChatGPT** -> 点击左侧导航栏 **Explore GPTs** -> 点击右上角 **+ Create** 创建专属助手。
2. 切换到 **Configure（配置）** 页面：
   * **Name（名称）**：`Gaya UKM Thesis Assistant (2015)`
   * **Description（简介）**：复制 [`platforms/chatgpt/conversation-starters.md`](./platforms/chatgpt/conversation-starters.md) 中的描述。
   * **Instructions（指令）**：复制粘贴 [`platforms/chatgpt/custom-gpt-instructions.md`](./platforms/chatgpt/custom-gpt-instructions.md) 的全部内容。
   * **Conversation Starters（开场预设问题）**：添加 [`platforms/chatgpt/conversation-starters.md`](./platforms/chatgpt/conversation-starters.md) 中的 4 条快捷提问。
   * **Knowledge（知识库）**：点击 **Upload files**，上传整合好的 [`platforms/chatgpt/gaya-ukm-knowledge-pack.md`](./platforms/chatgpt/gaya-ukm-knowledge-pack.md)。
   * **Capabilities（能力）**：勾选 *Code Interpreter（代码分析）* 与 *Web Browsing（网页浏览）*。
3. 点击右上角 **Save / Publish（保存发布）** 即可使用。

---

### 2. 🧠 Claude (Claude Projects & Claude Desktop / Code)

#### Option A: Claude Projects (Web 端项目知识库)
* **English**:
  1. In Claude.ai, create a new **Project** named `Gaya UKM Thesis Assistant`.
  2. Click **Set Project Instructions** and paste the contents of [`platforms/claude/project-instructions.md`](./platforms/claude/project-instructions.md).
  3. In **Project Knowledge**, upload the files inside [`references/`](./references/).
* **中文**:
  1. 打开 Claude.ai，在左侧点击 **Projects** 创建名为 `Gaya UKM Thesis Assistant` 的项目。
  2. 点击 **Set Project Instructions（设置项目指令）**，将 [`platforms/claude/project-instructions.md`](./platforms/claude/project-instructions.md) 中的 XML 结构化系统提示词粘贴进去。
  3. 在 **Project Knowledge（项目知识库）** 中上传 [`references/`](./references/) 目录下的参考文件。

#### Option B: Claude Code CLI / Claude Desktop (本地命令行与桌面端)
* **English**:
  If you are using Claude Code CLI or Claude Desktop in project mode, it will automatically detect and load [`CLAUDE.md`](./CLAUDE.md) located at the root of this repository.
* **中文**:
  如果您使用 Claude Code 命令行工具或 Claude Desktop 桌面端管理本地项目，它会自动识别并挂载仓库根目录下的 [`CLAUDE.md`](./CLAUDE.md)，无需额外手动配置。

---

### 3. 💼 WorkBuddy (企业级 AI / 办公助手)

**English Steps**:
1. Create a "New Agent / Expert Assistant" in WorkBuddy / Tencent Work Assistant / DingTalk.
2. **Role / System Prompt**: Copy and paste the text from [`platforms/workbuddy/system-prompt.md`](./platforms/workbuddy/system-prompt.md).
3. **Knowledge Base**: Import the Q&A card database from [`platforms/workbuddy/qa-knowledge-base.md`](./platforms/workbuddy/qa-knowledge-base.md).
4. Save and invoke the assistant directly during your daily academic writing and formatting workflow.

**中文配置指南**:
1. 在 WorkBuddy / 腾讯工作助手 / 钉钉助手 中点击“创建新智能体 / 专家助手”。
2. **角色设定 / 系统提示词**：复制粘贴 [`platforms/workbuddy/system-prompt.md`](./platforms/workbuddy/system-prompt.md) 的全部内容。
3. **知识库挂载**：在知识库配置中，将 [`platforms/workbuddy/qa-knowledge-base.md`](./platforms/workbuddy/qa-knowledge-base.md) 作为结构化问答库导入（内置 15 组关于边距、字体、摘要、中英文姓名著录、三线表规范的高频问答）。
4. 保存后即可在日常写作与开题论文排版中随时一键调用审查与修改建议。

---

### 4. 🚀 Antigravity / Gemini CLI (原生智能体技能库)

**English**:
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

**中文说明**:
将本仓库复制到 Antigravity / Gemini 的 skills 技能目录中即可生效：
```bash
# 全局安装（所有项目通用）
mkdir -p ~/.gemini/config/skills/gaya-ukm-thesis
cp -r . ~/.gemini/config/skills/gaya-ukm-thesis/

# 或当前项目工作空间独立安装
mkdir -p .agents/skills/gaya-ukm-thesis
cp -r . .agents/skills/gaya-ukm-thesis/
```
安装后，每当在对话中涉及 UKM 论文写作、开题报告、文献格式排版时，智能体将自动加载并激活此技能。

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
| **Abstract (rev15)** | Strictly NO literature citations `(Author Year)` or figures | ❌ Including citations or routine lab protocols in abstract |
| **Acknowledgements** | Max 1 page; 5-tier order; Dedication pages PROHIBITED | ❌ Separate "Dedication" page (strictly banned) |
| **Word Limits (2026)** | PhD $\le 100\text{k}$; Master Research $\le 60\text{k}$; Master Mixed $\le 50\text{k}$ | ❌ Exceeding cap without 3-month prior Dean approval |
| **Publication Quota** | PhD: 2 WoS/Scopus; Master: 1 WoS/Scopus (Supervisor co-author) | ❌ Non-indexed publications or omitting UKM supervisor |
| **Submission Notice** | *Borang Notis Serahan Tesis* filed $\ge 3$ months before submission | ❌ Submitting thesis without 3-month advance notice |

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
