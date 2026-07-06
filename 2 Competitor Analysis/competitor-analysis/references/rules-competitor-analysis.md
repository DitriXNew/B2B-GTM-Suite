# Competitor Analysis Rules — Detailed Reference

## Intake question bank

Use 2-3 questions per turn. Research competitors directly where you can, then confirm.

### Competitor set
- Who do you most often lose deals to?
- Who would a buyer shortlist alongside you?
- Is there a cheaper/simpler alternative buyers pick instead?
- For this purchase, is "do nothing / keep it in Excel / do it in-house" a real option? (the status quo)

### Per competitor
- What exactly do they sell, and to whom?
- How do they position themselves (their headline promise)?
- Where are they genuinely strong?
- Where do they fall short for your segment?
- What do they charge / how do they price, if you know? (optional)

### Differentiation
- For each of your values: does this competitor credibly offer the same thing? (yes / partial / no / unsure)
- Which of your values does *every* competitor also claim? (table stakes)
- Which does *no* competitor claim? (your real differentiators)

---

## Classifying competitors

- **Direct** — sells essentially the same offering to the same buyer.
- **Indirect** — solves the same problem a different way (a service vs a tool, an agency vs software).
- **Status-quo / in-house** — "do nothing", a spreadsheet, a manual process, or building it internally. For much of B2B this is the competitor that actually wins the deal. Never omit it when it applies.

Keep the set to the 3–5 that matter. More columns dilute the table and the analysis.

---

## Differentiation table pattern

Rows = your values (by ID). Columns = competitors. Each cell = whether that competitor **credibly claims** the value.

| Value | Competitor A | Competitor B | Status quo | Verdict |
|-------|--------------|--------------|------------|---------|
| PV-01 [title] | yes | partial | no | table stakes |
| SV-02 [title] | no | no | no | **unique** |
| AV-01 [title] | unsure | no | no | likely unique (verify) |

**Cell values:** `yes` (credibly claims it) · `partial` (weak or narrower version) · `no` (doesn't) · `unsure` (can't verify).

**Reading the verdict:**
- **unique** — no competitor claims it (`no`/`unsure` across the row, with at least the key rivals `no`). Candidate for the `unique` flag.
- **table stakes** — every competitor claims it (`yes` across the row). Real, but not a differentiator. Don't lead positioning with it.
- **contested** — a mix; a differentiator against some rivals but not others.

**Credibly claims** means a buyer would believe it, not merely that the competitor mentions the word. If verification isn't possible, mark `unsure` and do **not** flag the value unique: absence of evidence is not evidence of uniqueness.

---

## Positioning read

- **Where we win** — the `unique` values. These are the differentiators messaging should lead with, and the honest basis for "unlike [alternative]".
- **Where we're exposed** — (a) problems a competitor covers better than you, and (b) values that are table stakes (everyone claims them). These are the objections sales will hear and the gaps the Missing Value Propositions skill may target.

Name the **real alternative** for each strong value: a specific competitor, or the status quo ("doing it in Excel"). That named alternative is what the Messaging skill drops into "unlike [alternative]".

---

## Output file format

### File 1: `competitor-analysis.md` (Markdown — full documentation)

```markdown
# Competitor Analysis — [Company name]
Date: [date]
Model: Ananas-Agency Competitor Analysis

## Competitor set
| Competitor | Type | One-line profile |
|------------|------|------------------|
| [name] | direct / indirect / status-quo | [what they are] |

## Competitor profiles

### [Competitor name] — [direct / indirect / status-quo]
- **Offering:** [what they sell]
- **Positioning:** [headline promise, who they target]
- **Strengths:** [where they're strong]
- **Weaknesses:** [where they fall short for this segment]

[repeat per competitor]

## Differentiation table
[Values (by ID) × competitors — yes / partial / no / unsure, plus a Verdict column]

## Positioning read
- **Where we win:** [the unique values, by ID]
- **Where we're exposed:** [problems rivals cover better; table-stakes values]

## Unique-flag evidence (written back to the value list)
| Value ID | Verdict | Named alternative ("unlike …") |
|----------|---------|--------------------------------|
| SV-02 | unique | [competitor / status quo] |

## Summary
- Competitors analyzed: [n]
- Values that are unique: [n]
- Values that are table stakes: [n]
- Biggest exposure: [one line]
```

### File 2: `competitor-analysis.html` (styled, share-ready)

A single **self-contained** `.html` file (all CSS inline in one `<style>` block, **no external assets and no JavaScript**), so it opens in any browser, prints cleanly to PDF, and can be emailed as one file. Render the **same content** as the Markdown version. Keep the `<style>` block **identical to the shared design system** used across this suite (full CSS reproduced below).

- Render the competitor set and the differentiation table as `<table>`s, each inside its own `<section class="block">`.
- One `.card` per competitor profile; Offering / Positioning / Strengths / Weaknesses as `.row`s.
- In the differentiation table, mark a `unique` verdict with `<span class="tag unique">unique</span>` and a table-stakes verdict with `<span class="verdict-common">table stakes</span>`.
- Render the positioning read and the unique-flag evidence in their own blocks; close with a Summary block.


**Navigation & hints (required in every generated `.html`):**
- **Cross-link every reference to another deliverable.** Any mention of another document (the value list, a persona, the buying process, the dossier…) becomes a relative link to its canonical file (`value-propositions.html`, `buyer-persona.html`, … — see dossier-format.md for the full list). Any value ID cited here links back to the value list with a tooltip carrying the value's full title, e.g. `<a href="value-propositions.html" title="PV-01 — AI invoice auto-coding">PV-01</a>`; `MV-` IDs link to `missing-pso.html`, `H#` hypotheses to `experiments-plan.html`, personas to `buyer-persona.html`.
- **Hover hints on short terms — every occurrence, not just the first.** Give a `title` tooltip to **every** appearance of the shorthand set — PSO, DMU, ICP, the ID prefixes (PV/SV/AV/MV), and the `validated`/`hypothesis` statuses — e.g. `<abbr title="Problem · Solution · Outcome — the value-proposition format">PSO</abbr>`. Be consistent across the whole document; the final regeneration verifies these hints pack-wide.
- **No Previous / Next buttons in this file.** Do **not** add a `pagenav` (Previous/Next) block when generating this deliverable during the session — end the content with the Print hint instead. The walk navigation is wired **only in the final pack**, when the last skill regenerates every page in sequence order (see dossier-format.md, "Final consistency pass").
- **Print hint (no JavaScript).** End the page (after the last section, inside the content column) with `<p class="printhint">🖨 Print / Save as PDF — press <kbd>Ctrl</kbd>+<kbd>P</kbd> (<kbd>⌘</kbd>+<kbd>P</kbd> on Mac)</p>` — it uses the browser's own print (no button, no script) and hides itself automatically when printing.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Competitor Analysis — [Company name]</title>
<style>
:root{--page:#f5f5f7;--paper:#ffffff;--ink:#111111;--soft:#5b5852;--line:#e2e2e7;
--brand:#d99a2b;--brand-deep:#946618;--band:#0b0b0a;--band-ink:#b8b2a4}
*{box-sizing:border-box}
body{margin:0;background:var(--page);color:var(--ink);
font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.brandband{background:var(--band)}
.bwrap{max-width:1060px;margin:0 auto;padding:16px 20px;
display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap}
.brandlink{display:inline-flex;align-items:center;text-decoration:none;border-radius:4px;
cursor:pointer;transition:opacity .18s ease}
.brandlink:hover{opacity:.85}
.brandlink:focus-visible{outline:2px solid var(--brand);outline-offset:3px}
.brandlogo{display:block;height:44px;width:auto}
.pkgname{font-size:16px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;
color:#fff;line-height:1.5;text-decoration:none;transition:opacity .18s ease}
.pkgname:hover{opacity:.85}
.pkgname:focus-visible{outline:2px solid var(--brand);outline-offset:3px}
.byline{font-size:12px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--band-ink);margin-right:9px;white-space:nowrap}
@media (max-width:560px){.brandlogo{height:34px}}
.wrap{max-width:1040px;margin:0 auto;padding:0 20px 40px}
header.doc{margin:28px 0 6px;padding:22px 24px 20px;background:var(--paper);
border:1px solid var(--line);border-top:3px solid var(--brand);border-radius:2px}
header.doc h1{margin:0 0 6px;font-size:28px;line-height:1.25;font-weight:700;letter-spacing:-.01em}
header.doc .tagline{margin:0 0 14px;color:var(--soft);font-size:16px;font-style:italic}
header.doc .meta{color:var(--soft);font-size:14px}
header.doc .meta b{color:var(--ink);font-weight:600}
section.block{margin-top:36px}
h2.section{margin:0 0 14px;font-size:18px;font-weight:800;letter-spacing:-.01em;
display:flex;align-items:center;gap:12px}
h2.section .no{flex:none;width:28px;height:28px;display:inline-flex;align-items:center;
justify-content:center;background:var(--band);color:#fff;font-size:14px;font-weight:700;
border-radius:2px;font-variant-numeric:tabular-nums}
h2.section::after{content:"";flex:1;height:1px;background:var(--line)}
article.card,.card{background:var(--paper);border:1px solid var(--line);border-radius:2px;
padding:16px 20px;margin:10px 0}
.card h3{margin:0 0 12px;padding-bottom:11px;border-bottom:1px solid var(--line);
font-size:16px;font-weight:700;display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.id{font-size:12px;font-weight:700;color:#43444a;background:#eef0f4;
border:1px solid #d8dae1;border-radius:2px;padding:3px 8px;letter-spacing:.03em}
.badge,.scoreno{font-size:14px;color:var(--soft);font-variant-numeric:tabular-nums}
.scorewrap{margin-left:auto;display:flex;align-items:center;gap:8px;white-space:nowrap}
.meter{width:64px;height:5px;background:var(--line);overflow:hidden}
.meter i{display:block;height:100%;background:var(--ink)}
.tag,.pill{font-size:12px;font-weight:650;border-radius:2px;padding:2.5px 8px;line-height:1.35}
.tag.validated{background:#ddefe1;color:#14603c}
.tag.hypothesis{background:#f6e6b6;color:#6d5410}
.tag.unique,.tag-unique{font-size:11px;font-weight:650;border-radius:2px;padding:3px 9px;
background:var(--band);color:var(--brand);text-transform:uppercase;letter-spacing:.09em}
.tag.unique::before,.tag-unique::before{content:"\25C6\00A0";font-size:9px;vertical-align:1px}
.pill.covered{background:#ddefe1;color:#14603c}
.pill.gap{background:#f7e6e1;color:#a53d2e}
.verdict-common{color:var(--soft);font-size:13px}
.row{margin:4px 0;font-size:16px}
.row .k{font-weight:650;margin-right:2px}
blockquote{margin:12px 0 2px;padding:0 0 0 14px;border-left:2px solid var(--ink);
color:#494540;font-style:italic;font-size:16px}
.tablewrap{overflow-x:auto;background:var(--paper);border:1px solid var(--line);
border-radius:2px;padding:6px 20px 10px;margin-top:10px}
table{width:100%;border-collapse:collapse;font-size:14px;font-variant-numeric:tabular-nums}
th{text-align:left;padding:10px 12px 8px 0;font-size:14px;font-weight:700;
border-bottom:2px solid var(--ink)}
td{text-align:left;padding:9px 12px 9px 0;border-bottom:1px solid var(--line);vertical-align:top}
tr:last-child td{border-bottom:none}
ul.clean{margin:6px 0;padding-left:18px}
a{color:var(--brand-deep)}
abbr[title],.term[title]{text-decoration:none;border-bottom:1px dotted #9a958c;cursor:help}
.nextbtn{display:inline-block;margin:36px 0 8px;background:var(--band);color:#fff;
padding:12px 22px;border-radius:2px;text-decoration:none;font-weight:650}
.nextbtn:hover{color:var(--brand)}
.pagenav{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;margin:36px 0 8px}
.pagenav .nextbtn,.pagenav .prevbtn{margin:0}
.pagenav .nextbtn{margin-left:auto}
.prevbtn{display:inline-block;background:var(--paper);color:var(--ink);border:1px solid var(--line);
padding:12px 22px;border-radius:2px;text-decoration:none;font-weight:650}
.prevbtn:hover{border-color:var(--brand);color:var(--brand-deep)}
.printhint{margin:22px 0 8px;font-size:13px;color:var(--soft);text-align:center}
.printhint kbd{font:inherit;background:#eef0f4;border:1px solid #d8dae1;border-bottom-width:2px;border-radius:3px;padding:1px 6px;font-weight:650}
.ctablock{background:var(--band);border-radius:2px;padding:36px 28px;text-align:center;margin-top:36px}
.ctablock .ctahead{font-size:22px;font-weight:800;letter-spacing:-.01em;margin:0 0 6px;color:#fff}
.ctablock .ctasub{color:var(--band-ink);font-size:15px;margin:0 0 18px}
.ctabtn{display:inline-block;background:var(--brand);color:#231a06;font-weight:700;
padding:12px 26px;border-radius:2px;text-decoration:none}
.ctabtn:hover{background:#e2a83d}
.openbtn{font-size:13px;font-weight:650;color:var(--ink);background:var(--paper);
border:1px solid var(--line);border-radius:2px;padding:5px 12px;text-decoration:none;white-space:nowrap}
.openbtn:hover{border-color:var(--brand);color:var(--brand-deep)}
h2.section .openbtn{order:3;margin-left:12px}
h2.section::after{order:2}
footer.doc{margin-top:40px;background:var(--band);color:var(--band-ink);font-size:12px}
.fwrap{max-width:1060px;margin:0 auto;padding:28px 20px 30px;text-align:center;
display:flex;flex-direction:column;align-items:center;gap:10px}
.footlogo{display:block;height:32px;width:auto}
.footmail{color:var(--brand);font-weight:600;text-decoration:none}
.footmail:hover{text-decoration:underline}
.footmail:focus-visible{outline:2px solid var(--brand);outline-offset:3px}
@media print{body{background:#fff}
article.card,.card,.tablewrap{border-color:#ccc}
header.doc{border-color:#ccc;border-top-color:var(--brand)}
.nextbtn,.openbtn,.prevbtn,.pagenav,.printhint{display:none}
.brandband,footer.doc,.ctablock,.tag,.pill,.meter i,.id,h2.section .no,.tag-unique{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
</style>
</head>
<body>
<div class="brandband">
  <div class="bwrap">
    <a class="pkgname" href="https://b2b-gtm-suite.ananas-agency.com/?utm_source=ananas-sales-skills&amp;utm_medium=deliverable&amp;utm_campaign=b2b-gtm-suite&amp;utm_content=competitor-analysis" target="_blank" rel="noopener">B2B Go-to-Market Suite</a>
    <a class="brandlink" href="https://ananas-agency.com/?utm_source=ananas-sales-skills&amp;utm_medium=deliverable&amp;utm_campaign=b2b-gtm-suite&amp;utm_content=competitor-analysis" target="_blank" rel="noopener">
      <span class="byline">by</span>
      <img class="brandlogo" src="https://ananas-agency.com/wp-content/uploads/2025/05/ananas-agency-logo-no-background-for-black.png" alt="Ananas Agency">
    </a>
  </div>
</div>

<div class="wrap">
  <header class="doc">
    <h1>Competitor Analysis — [Company name]</h1>
    <div class="meta"><b>Date:</b> [date] &nbsp;·&nbsp; <b>Model:</b> Ananas-Agency Competitor Analysis</div>
  </header>

  <section class="block">
    <h2 class="section">Competitor set</h2>
    <table>
      <tr><th>Competitor</th><th>Type</th><th>One-line profile</th></tr>
      <tr><td>[name]</td><td>direct / indirect / status-quo</td><td>[what they are]</td></tr>
    </table>
  </section>

  <section class="block">
    <h2 class="section">Competitor profiles</h2>
    <article class="card">
      <h3>[Competitor name] <span class="badge">[type]</span></h3>
      <div class="row"><span class="k">Offering</span>[what they sell]</div>
      <div class="row"><span class="k">Positioning</span>[headline promise]</div>
      <div class="row"><span class="k">Strengths</span>[where strong]</div>
      <div class="row"><span class="k">Weaknesses</span>[where they fall short]</div>
    </article>
    <!-- one .card per competitor -->
  </section>

  <section class="block">
    <h2 class="section">Differentiation table</h2>
    <table>
      <tr><th>Value</th><th>[Comp A]</th><th>[Comp B]</th><th>Status quo</th><th>Verdict</th></tr>
      <tr><td><span class="id">SV-02</span> [title]</td><td>no</td><td>no</td><td>no</td><td><span class="tag unique">unique</span></td></tr>
      <tr><td><span class="id">PV-01</span> [title]</td><td>yes</td><td>partial</td><td>no</td><td><span class="verdict-common">table stakes</span></td></tr>
    </table>
  </section>

  <section class="block">
    <h2 class="section">Positioning read</h2>
    <div class="row"><span class="k">Where we win</span>[unique values by ID]</div>
    <div class="row"><span class="k">Where we're exposed</span>[problems rivals cover better; table-stakes values]</div>
  </section>

  <section class="block">
    <h2 class="section">Unique-flag evidence</h2>
    <table>
      <tr><th>Value</th><th>Verdict</th><th>Unlike [alternative]</th></tr>
      <tr><td><span class="id">SV-02</span></td><td>unique</td><td>[competitor / status quo]</td></tr>
    </table>
  </section>

  <section class="block">
    <h2 class="section">Summary</h2>
    <div class="row"><span class="k">Competitors analyzed</span>[n]</div>
    <div class="row"><span class="k">Unique values / table stakes</span>[n] / [n]</div>
    <div class="row"><span class="k">Biggest exposure</span>[one line]</div>
  </section>
  <p class="printhint">🖨 Print / Save as PDF — press <kbd>Ctrl</kbd>+<kbd>P</kbd> (<kbd>⌘</kbd>+<kbd>P</kbd> on Mac)</p>
</div>

<footer class="doc">
  <div class="fwrap">
    <a class="brandlink" href="https://ananas-agency.com/?utm_source=ananas-sales-skills&amp;utm_medium=deliverable&amp;utm_campaign=b2b-gtm-suite&amp;utm_content=competitor-analysis" target="_blank" rel="noopener">
      <img class="footlogo" src="https://ananas-agency.com/wp-content/uploads/2025/05/ananas-agency-logo-no-background-for-black.png" alt="Ananas Agency">
    </a>
    <a class="footmail" href="mailto:juicy@ananas-agency.com">juicy@ananas-agency.com</a>
    <div>© 2026 Ananas-Agency — generated [date]. MIT License.</div>
  </div>
</footer>
</body>
</html>
```


---

## License

Copyright (c) 2026 Kostiantyn Ivanov (Ananas-Agency, ananas-agency.com).

Released under the MIT License — keeping the copyright notice is all that is required, and a credit to the author is warmly appreciated. Full license text: [LICENSE](../../../LICENSE)
