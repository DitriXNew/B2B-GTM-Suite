#!/usr/bin/env python3
"""Rebuild the compiled Handbook from the unpacked skill sources.

Run from anywhere:  python output/build-handbook.py

For each skill it emits:  # <N>. <Title> / Skill ID / <SKILL.md body> /
reference materials / <rules-*.md body>, matching the Handbook's format. Internal
links are rewritten to the Handbook's root context (../LICENSE.md -> LICENSE.md,
../dossier-format.md -> dossier-format.md); references/ links are left as-is.

Run this after editing any skill so the Handbook stays in sync with output/<slug>/.
"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "B2B Go-to-Market Suite - Handbook by Ananas Agency.md")

# (label, title, folder, slug, rules_filename)  — order = Handbook order
SKILLS = [
    ("0",   "Company Brief",                                          "0 Company Brief",              "company-brief",              "rules-company-brief.md"),
    ("1",   "Value Propositions (PSO (Problem · Solution · Outcome))", "1 Value Proposition",         "value-proposition",          "rules-pso.md"),
    ("2",   "Competitor Analysis",                                    "2 Competitor Analysis",        "competitor-analysis",        "rules-competitor-analysis.md"),
    ("3",   "Buyer Persona B2B",                                      "3 Buyer Persona",              "buyer-persona",              "rules-buyer-persona.md"),
    ("4",   "Experiments Validating the Buyer Persona",               "4 Persona Experiments",        "persona-experiments",        "rules-experiments.md"),
    ("5",   "B2B Segment Buying Process",                             "5 Buying Process",             "buying-process",             "rules-buying-processes.md"),
    ("6",   "Missing Value Propositions — Gap Analysis",              "6 Missing Value Propositions", "missing-value-propositions", "rules-missing-pso.md"),
    ("7",   "Messaging & Positioning",                                "7 Messaging and Positioning",  "messaging-positioning",      "rules-messaging.md"),
]

SEP = "\n\n================================================================================\n\n"


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def strip_frontmatter(text):
    if text.startswith("---"):
        idx = text.find("\n---", 3)
        if idx != -1:
            return text[idx + 4:].lstrip("\n")
    return text.lstrip("\n")


def fix_links(t):
    t = t.replace("](../../LICENSE.md)", "](LICENSE.md)")
    t = t.replace("](../LICENSE.md)", "](LICENSE.md)")
    t = t.replace("](../dossier-format.md)", "](dossier-format.md)")
    return t


def block(label, title, folder, slug, rules):
    skill = fix_links(strip_frontmatter(read(os.path.join(BASE, folder, slug, "SKILL.md")))).rstrip()
    rulesbody = fix_links(read(os.path.join(BASE, folder, slug, "references", rules))).lstrip("\n").rstrip()
    return (
        f"# {label}. {title}\n\n"
        f"**Skill ID:** `{slug}`\n\n"
        f"{skill}\n\n"
        f"---\n\n"
        f"## Skill reference materials: {slug}\n\n"
        f"### Reference: {rules}\n\n"
        f"{rulesbody}"
    )


def main():
    intro = ("# B2B Go-to-Market Suite - Handbook\n\n"
             "_by Ananas Agency._ Every skill and its reference, compiled into one document. No stages - one suite.")
    blocks = [block(*s) for s in SKILLS]
    doc = intro + SEP + SEP.join(blocks) + "\n"
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(doc)
    print(f"wrote {OUT}  ({len(blocks)} skills, {len(doc)} chars)")


if __name__ == "__main__":
    main()
