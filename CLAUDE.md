# CLAUDE.md: Gaya UKM Thesis Assistant (2015)

## Overview
This repository contains the complete specification, formatting rules, reference templates, and linting tools for academic dissertations, theses, and proposals following the official **Universiti Kebangsaan Malaysia (UKM) Thesis Writing Style Guide (Gaya UKM 2015)**.

## Core Directives for Claude
When assisting users with academic writing in this project:
1. **In-Text Citations**:
   - Strictly Author-Date system.
   - **NO COMMA** between author and year in parenthetical citations: `(Reid 2012)`, NOT `(Reid, 2012)`.
   - Two authors: in text use `and` (`Adams and White 2007`), in parentheses use `&` (`(Adams & White 2007)`).
   - 3+ authors: `(Shafaratul et al. 2011)`.
   - Multiple citations in one parenthesis: sort alphabetically, separate with semicolon: `(Azahan 2011; Jamaluddin 2010)`.
2. **References List**:
   - Single-spaced within entry, hanging indent of `12.5 mm`, one blank line between entries.
   - **NO PARENTHESES** around publication years: `Smith, J. 2010.`, NOT `Smith, J. (2010).`
   - Journal volume & issue format: tightly joined as `Volume(Issue): Pages.` e.g., `Journal of Management 38(2): 235-243.`
   - Western authors: Surname first (`Bowen, H.J.M.`).
   - Malay authors: Direct full name (`Noor Azlan Ghazali. 2012.`).
   - Chinese authors: Surname first (`Ding, Choo Ming. 2008.` or `Lim, E.H.T. 2005.`).
3. **Headings & Structure**:
   - Max 5 levels of headings: Level 1 (`CHAPTER I`), Level 2 (`1.1`), Level 3 (`1.1.1`), Level 4 (`a., b.`), Level 5 (`i., ii.`).
   - **TOC Constraint**: Only Levels 1–3 are allowed in the Table of Contents.
   - 14-item mandatory preliminary sequence: Title Page -> Malay Translation Title Page -> Declaration -> Acknowledgements -> Malay Abstrak -> English Abstract -> Contents -> Lists -> Body -> References -> Appendices.
4. **Typography & Layout**:
   - Times New Roman throughout. Margins: Top 30mm, Bottom 25mm, Left 38mm, Right 25mm.
   - Chapter opening pages begin 50mm from top edge.
   - Body font: 12 pt, 1.5 spacing. Tables & Figures: 10 pt.
   - Table title: Above table. Figure title: Below figure.
   - Quotes >40 words: block indented 12.7mm, single-spaced, no quotes.
5. **Postgraduate Regulations (2026) & rev15 Word Templates**:
   - **Graduation Publication Requirement**: PhD: Min 2 WoS/Scopus articles (Science) / 2 WoS/Scopus or 1 WoS/Scopus + 1 UKM/MyCite/chapter (Social Science). Master Research: 1 WoS/Scopus (Science) / 1 ERA/WoS/Scopus/UKM (Social Science). UKM supervisor must be an author.
   - **Notice of Submission**: *Borang Notis Serahan Tesis* must be filed $\ge 3$ months in advance.
   - **Anti-Plagiarism Screening**: Official *Pengesahan Bebas Plagiat* (Turnitin) required.
   - **Word Count Caps**: PhD Research $\le 100,000$; PhD Mixed $\le 60,000$; Master Research $\le 60,000$; Master Coursework/Mixed $\le 50,000$.
   - **Acknowledgements (rev15)**: Max 1 page; separate Dedication pages are STRICTLY FORBIDDEN; 5-tier order (God $\to$ Supervisors $\to$ Faculty $\to$ Grants $\to$ Family/Peers).
   - **Abstract (rev15)**: 200–350 words, 1 paragraph, single-spaced; strictly NO citations `(Author Year)` or figures.
   - **Compilation Format**: Thesis by publication recognized; automatically permits writing in English.

## Validation Tooling
Run the automated compliance linter over any draft or chapter:
```bash
python3 scripts/check_gaya_ukm.py <manuscript.md | chapter.txt | thesis.tex>
```
