#!/usr/bin/env python3
"""
Gaya UKM (2015) Automated Linter & Compliance Checker
Checks Markdown, LaTeX, or plain text manuscripts for common UKM Thesis Style Guide violations.
"""

import sys
import os
import re

def check_file(filepath):
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)

    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    errors = []
    warnings = []

    in_references_section = False

    for idx, line in enumerate(lines, 1):
        stripped = line.strip()

        # Check section boundaries
        if re.match(r"^#+\s*(REFERENCES|RUJUKAN)", stripped, re.IGNORECASE) or stripped == "REFERENCES":
            in_references_section = True
            continue

        if re.match(r"^#+\s*(APPENDIX|LAMPIRAN)", stripped, re.IGNORECASE):
            in_references_section = False

        # --- In-Text Citation Checks (Body Text) ---
        if not in_references_section:
            # 1. Comma between author and year inside parentheses: (Author, 2020) or (Smith et al., 2019)
            illegal_comma_cites = re.findall(r"\(([A-Z][a-zA-Z\s\.\&]+?),\s*([12]\d{3}[a-z]?)\)", line)
            for match in illegal_comma_cites:
                author, year = match
                # Ignore if it's e.g. (e.g., 2020) or (Figure 1, 2020)
                if not any(k in author.lower() for k in ["see", "eg", "e.g.", "table", "figure", "appendix"]):
                    errors.append((
                        idx,
                        "In-text citation comma violation",
                        f"Found '({author}, {year})'. Gaya UKM strictly forbids commas between author and year. Use '({author} {year})'."
                    ))

            # 2. Use of 'and' inside parenthetical citation: (Author and Author 2020) -> should be '&'
            parenthetical_and = re.findall(r"\(([A-Z][a-zA-Z\s\.]+)\sand\s([A-Z][a-zA-Z\s\.]+)\s([12]\d{3}[a-z]?)\)", line)
            for p in parenthetical_and:
                errors.append((
                    idx,
                    "In-text citation conjunction violation",
                    f"Found 'and' inside parenthesis '{p[0]} and {p[1]} {p[2]}'. Gaya UKM requires '&' inside parentheses: '({p[0]} & {p[1]} {p[2]})'."
                ))

            # 3. Deep heading decimal numbers (Level 4+ like 1.1.1.1)
            deep_heading = re.findall(r"^\s*(?:#+\s*)?(\d+\.\d+\.\d+\.\d+)", line)
            for dh in deep_heading:
                errors.append((
                    idx,
                    "Heading level depth violation",
                    f"Found decimal heading '{dh}'. Gaya UKM only permits decimal numbering up to level 3 (e.g. 1.1.1). Level 4 must use letters (a., b.), level 5 roman numerals (i., ii.)."
                ))

            # 4. SI Unit missing space (Appendix T): e.g. 5kg, 10cm, 100ppm
            si_no_space = re.findall(r"\b(\d+)(cm|mm|km|kg|ppm|kPa|MPa)\b", line)
            for val, unit in si_no_space:
                warnings.append((
                    idx,
                    "SI Unit spacing rule (Appendix T)",
                    f"Found '{val}{unit}' without space. Gaya UKM requires space between number and unit: '{val} {unit}'."
                ))

            # 5. SI Unit plural form: e.g. 4 cms, 2 kgs
            si_plural = re.findall(r"\b(\d+\s*(?:cms|kgs|mms|kms))\b", line, re.IGNORECASE)
            for sp in si_plural:
                warnings.append((
                    idx,
                    "SI Unit plural violation (Appendix T)",
                    f"Found plural unit '{sp}'. Gaya UKM states units have no plural forms (e.g. '4 cm', not '4 cms')."
                ))

        # --- Reference Section Checks ---
        else:
            # 1. Year with parentheses in reference list: Author. (2020).
            year_in_parens = re.findall(r"^([A-Z][^\.\n]+(?:\.[A-Z]\.|\b))\s*\(([12]\d{3}[a-z]?)\)", stripped)
            for auth, yr in year_in_parens:
                errors.append((
                    idx,
                    "Reference year in parentheses",
                    f"Found '{auth} ({yr})'. Gaya UKM requires year without parentheses: '{auth}. {yr}.'"
                ))

            # 2. Underscored URL or missing access date bracket
            if "http://" in line or "https://" in line:
                if not re.search(r"\[\d{1,2}\s+[A-Za-z]+\s+[12]\d{3}\]\.", line):
                    warnings.append((
                        idx,
                        "Electronic resource access date missing or unbracketed",
                        "Online reference should end with access date in brackets: '[DD Month YYYY].'"
                    ))

    # Output report
    print(f"\n========================================================")
    print(f" Gaya UKM (2015) Compliance Audit Report: {os.path.basename(filepath)}")
    print(f"========================================================\n")

    if not errors and not warnings:
        print("✅ Congratulations! No Gaya UKM formatting violations detected.\n")
        return

    if errors:
        print(f"❌ ERRORS ({len(errors)} found - must be fixed for thesis compliance):")
        for line_no, category, desc in errors:
            print(f"  [Line {line_no:4d}] {category}:")
            print(f"             {desc}")
        print()

    if warnings:
        print(f"⚠️  WARNINGS & STYLE NOTICES ({len(warnings)} found):")
        for line_no, category, desc in warnings:
            print(f"  [Line {line_no:4d}] {category}:")
            print(f"             {desc}")
        print()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 check_gaya_ukm.py <manuscript.md | chapter.txt | thesis.tex>")
        sys.exit(1)
    check_file(sys.argv[1])
