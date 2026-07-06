#!/usr/bin/env python3
"""Repack every unpacked skill folder back into its .skill archive.

Run from the repo root:  python output/repack-all-skills.py

For each entry below it zips  <folder>/<slug>/  ->  <folder>/<slug>.skill
with forward-slash internal paths (matching the original archives), then
removes the DO_NOT_FORGET_TO_REZIP.md marker for that folder.
"""
import zipfile
import os

BASE = os.path.dirname(os.path.abspath(__file__))

SPECS = [
    ("0 Company Brief", "company-brief", "rules-company-brief.md"),
    ("1 Value Proposition", "value-proposition", "rules-pso.md"),
    ("2 Competitor Analysis", "competitor-analysis", "rules-competitor-analysis.md"),
    ("3 Buyer Persona", "buyer-persona", "rules-buyer-persona.md"),
    ("4 Persona Experiments", "persona-experiments", "rules-experiments.md"),
    ("5 Buying Process", "buying-process", "rules-buying-processes.md"),
    ("6 Missing Value Propositions", "missing-value-propositions", "rules-missing-pso.md"),
    ("7 Messaging and Positioning", "messaging-positioning", "rules-messaging.md"),
]


def main():
    for folder, slug, rules in SPECS:
        fdir = os.path.join(BASE, folder)
        skill_md = os.path.join(fdir, slug, "SKILL.md")
        rules_md = os.path.join(fdir, slug, "references", rules)
        if not (os.path.exists(skill_md) and os.path.exists(rules_md)):
            print(f"SKIP {slug}: unpacked files not found")
            continue
        out_zip = os.path.join(fdir, slug + ".skill")
        with zipfile.ZipFile(out_zip, "w", zipfile.ZIP_DEFLATED) as z:
            z.write(skill_md, f"{slug}/SKILL.md")
            z.write(rules_md, f"{slug}/references/{rules}")
        marker = os.path.join(fdir, "DO_NOT_FORGET_TO_REZIP.md")
        if os.path.exists(marker):
            os.remove(marker)
        print(f"repacked {out_zip}  (marker removed)")


if __name__ == "__main__":
    main()
