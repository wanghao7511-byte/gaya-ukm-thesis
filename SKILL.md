---
name: gaya-ukm-thesis
description: >-
  Comprehensive formatting, citation, and writing assistant for dissertations, theses, and proposals
  following the official Universiti Kebangsaan Malaysia (UKM) thesis writing style (Gaya UKM 2015).
  Use whenever drafting, formatting, reviewing, or validating UKM academic writing (PhD/Master proposals,
  chapters, tables, figures, in-text citations, reference lists, or front matter).
---

# Gaya UKM Thesis Writing & Formatting Skill (2015 Edition)

This skill provides an authoritative, end-to-end framework and automated auditing tools for producing, formatting, and verifying academic theses, dissertations, and research proposals strictly adhering to **Gaya UKM (2015)** published by the **UKM Graduate Centre (Pusat Pengajian Siswazah)**.

---

## 1. Quick Reference: Technical Hard Specifications

| Item | Requirement | Gaya UKM Reference |
| :--- | :--- | :--- |
| **Paper Size** | A4 (`210 mm × 297 mm`), min. 80 gsm simile paper | Sec 1.1 |
| **Printing** | Single-sided only (Romanized script on the right side) | Sec 1.3 |
| **Primary Font** | **Times New Roman** throughout the entire thesis | Sec 1.2.1 |
| **Font Sizes** | **12 pt**: Regular body text<br>**11 pt**: Chapter headings and all subheadings<br>**10 pt**: Table titles, table contents, figure titles, footnotes<br>**18 pt**: Cover & spine gold lettering (all CAPITALS) | Sec 1.2.1, 1.6, 3.12.6 |
| **Margins** | **Top**: `30 mm` \| **Bottom**: `25 mm` \| **Left (binding)**: `38 mm` \| **Right**: `25 mm`<br>*(Exception: Chapter opening page starts `50 mm` from top)* | Sec 2.1.1 |
| **Line Spacing** | **1.5 spacing**: General body text<br>**1.0 single spacing**: Declarations, acknowledgements, abstracts, TOC, list of tables/illustrations, table contents, block quotes (>40 words), footnotes, reference items | Sec 1.2.4 |
| **Paragraphing** | **First paragraph** under any heading: **No indent (Flush Left)**<br>**Subsequent paragraphs**: First line indented **`12.7 mm` (0.5 in)** | Sec 1.2.5 |
| **Pagination** | **Top-right corner**, `15 mm` from top edge, `25 mm` from right edge.<br>• Prelim pages: lower-case Roman (`i, ii, iii...`), title page is `i` (hidden).<br>• Main text & appendices: Arabic (`1, 2, 3...`), chapter first pages count but hidden. | Sec 2.2 |
| **Word Limits** | • **PhD**: Max 100,000 words or 400 pages.<br>• **Master (Research)**: Max 60,000 words or 250 pages.<br>• **Master (Coursework/Mixed Dissertation)**: Max 30,000 words or 130 pages.<br>*(Excludes footnotes, quotations, appendices, formulas, tables, figures)* | Sec 3.12.1-3.12.2 |
| **Cover Colors** | • **PhD / DBA / DrPH**: Navy Blue (Hard cover, gold lettering)<br>• **Master**: Maroon (Hard cover, gold lettering)<br>• **Postgraduate Diploma**: Black | Sec 1.5.2 |

---

## 2. Core Workflows & Execution Checklists

When assisting with a UKM thesis or chapter, execute the following phased workflows:

### Workflow Phase 1: Structure & Front Matter Assembly
Ensure the thesis strictly follows the 14-item mandatory order (Chapter III):
1. `TITLE PAGE` (Inverted pyramid title `60 mm` from top, Year `40 mm` from bottom)
2. `TRANSLATION OF TITLE PAGE` (Bahasa Melayu translation for English thesis)
3. `DECLARATION` (Single-spaced, author signature & matric no.)
4. `ACKNOWLEDGEMENTS` (Single-spaced, heading centered `30 mm` from top)
5. `ABSTRAK` (Malay abstract, single paragraph, single-spaced, 200–350 words)
6. `ABSTRACT` (English abstract, single paragraph, single-spaced, 200–350 words)
7. `CONTENTS` (Table of contents, only levels 1–3 allowed)
8. `LIST OF TABLES`
9. `LIST OF ILLUSTRATIONS`
10. `LIST OF SYMBOLS / ABBREVIATIONS / GLOSSARY`
11. `LIST OF CASES` / `LIST OF STATUTES` (if applicable)
12. `BODY TEXT` (Chapters 1 to 5/6)
13. `REFERENCES` (Author-Date system, hanging indent `12.5 mm`)
14. `APPENDICES` (APPENDIX A, B, etc.)

> Refer to [Structure and Layout Detailed Guide](./references/structure-and-layout.md) for verbatim templates and layout spacing.

---

### Workflow Phase 2: Heading Hierarchy & Typing Standards
Strictly enforce the 5-tier heading boundary. Do not allow subheadings deeper than level 5, and do not allow subheadings deeper than level 3 to leak into the Table of Contents:

```text
Level 1: CHAPTER I           (Centered, bold, 11 pt, 50 mm from top margin)
         INTRODUCTION        (Centered, bold, 11 pt, 2 line spaces below)
Level 2: 1.1 BACKGROUND     (Flush left, bold, 11 pt, 2 spaces below title)
Level 3: 1.1.1 Problem Scope (Flush left, bold, 11 pt, 2 decimal places max)
Level 4: a. Market Dynamics  (Flush left, regular/bold, 11 pt, not in TOC)
Level 5: i. Price factors    (Flush left, regular, 11 pt, not in TOC)
```

---

### Workflow Phase 3: Tables, Figures & Quotations Validation

1. **Tables (Sec 3.12.6a)**:
   - Title MUST be positioned **above** the table: `Table 4.1  Descriptive statistics` (10 pt).
   - Use standard **three-line table** formatting (Top line, Header separator, Bottom line). **No vertical gridlines**.
   - Table content font: **10 pt**.
   - If landscape: table head must point towards the **bound edge (left margin)**.
   - If continuing onto next page: repeat header with `Table 4.1 (continued)`.
2. **Figures/Illustrations (Sec 3.12.6b)**:
   - Title MUST be positioned **below** the figure: `Figure 2.1  Research model` (10 pt).
   - Figure content font: **10 pt**.
   - Text explanation MUST precede the figure: `...as depicted in Figure 2.1`.
3. **Direct Quotations (Sec 3.12.7)**:
   - **$\le 40$ words**: Embedded in-line surrounded by double quotation marks `"..."`.
   - **$> 40$ words**: Standalone block paragraph, **single-spaced**, **indented `12.7 mm`** from left margin, **no quotation marks**, separated by 1.5 line spaces above and below.
   - Foreign language quotes: italicized.

---

### Workflow Phase 4: Gaya UKM Author-Date Citation & Reference Verification

UKM uses a specialized variant of the Author-Date Harvard system. You must check and correct common formatting errors:

1. **In-Text Parenthetical Citations**:
   - ❌ **Wrong (APA style)**: `(Reid, 2012)`, `(Smith & Jones, 2018)`
   - ✅ **Correct (Gaya UKM)**: `(Reid 2012)`, `(Smith & Jones 2018)` — **NO COMMA between author and year**.
   - Narrative in text: `Reid (2012) stated that...`
   - Two authors: in narrative use `and` (`Adams and White 2007`), in parentheses use `&` (`(Adams & White 2007)`).
   - Three or more authors: `(Shafaratul et al. 2011)`.
   - Multiple parenthetical citations: sort alphabetically by first author, separate with semicolon: `(Azahan 2011; Jamaluddin 2010; Kadir 2012)`.
2. **References List**:
   - Single-spaced within entry, hanging indent of **`12.5 mm`**, blank line between entries.
   - Year is **NEVER in parentheses**: `Smith, J. 2010.`, not `Smith, J. (2010).`
   - Journal format: `Journal Name(Italics) Volume(Issue): Pages.` -> `Journal of Management 38(2): 235-243.`
   - Western authors: Surname first with initials (`Bowen, H.J.M.`).
   - Malay authors: Full direct name (`Noor Azlan Ghazali 2012.`).
   - Chinese authors: Surname first followed by given names (`Ding, Choo Ming` or `Lim, E.H.T.`).

> Refer to [Citation and References Comprehensive Manual](./references/citation-and-references.md) for templates covering all publication categories (Books, Edited Chapters, Theses, Government Gazettes, Acts, Websites, Reports).

---

### Workflow Phase 5: Technical Details & Appendix T Rules
Verify that writing conforms to SI units and technical conventions:
- Space required between number and unit: `3 cm`, `4 kg`, `200 s`, `2 M` (never `3cm`, `4kg`).
- Units never have plural forms: `4 cm`, never `4 cms`.
- Dates: `26 January 1992` (no commas).
- 12-month period: use slash `1991/92`; multi-year period: use hyphen `1820-1910`.
- Acronyms: no periods (`UKM`, `DOSH`, `DBP`). Personal initials: space included (`A.R. Ahmad`).

---

## 3. Automation Tools & Helper Scripts

This skill includes an automated Python verification script in `./scripts/check_gaya_ukm.py` that parses text, markdown, or TeX manuscripts to catch:
- Parenthetical citations with illegal commas (e.g. `(Author, 2020)`)
- Reference items with bracketed years (e.g. `Author (2020)`)
- Deep headings (level 4+) appearing in table of contents
- Missing spaces in SI units (e.g. `10kg`, `5cm`)

Run the script over any draft or chapter:
```bash
python3 ~/.gemini/config/skills/gaya-ukm-thesis/scripts/check_gaya_ukm.py path/to/chapter.md
```

---

## 4. References Directory Overview

* [Technical Formatting Specifications](./references/formatting-specifications.md): Exact measurements, cover layouts, spine dimensions, margins, and paper requirements.
* [Structure and Layout Standards](./references/structure-and-layout.md): Complete preliminary page templates, word count caps, and chapter outlines.
* [Citation and References Manual](./references/citation-and-references.md): Comprehensive reference guide with 50+ real examples matching Chapter IV and V of Gaya UKM.
