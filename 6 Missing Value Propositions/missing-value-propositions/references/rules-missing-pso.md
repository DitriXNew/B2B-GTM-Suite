# Missing PSO (Problem · Solution · Outcome) Rules — Detailed Reference

## Coverage table

For each buyer persona, build a coverage table that maps problems, challenges, and objections onto the existing values from the PSO (Problem · Solution · Outcome).

### Coverage table pattern

```
COVERAGE TABLE — [Buyer persona name]
================================================

| # | Problem / Challenge / Objection (from the persona) | Role | Existing value from PSO | Status |
|---|-------------------------------------------|------|--------------------------|--------|
| 1 | [problem 1 from the persona]              | [person's role] | [value ID + title] (e.g. PV-03 + title) | Covered |
| 2 | [problem 2 from the persona]              | [person's role] | [value ID + title — partially] (e.g. SV-02 + title) | Weakly covered |
| 3 | [problem 3 from the persona]              | [person's role] | — none — | GAP |
| 4 | [objection 1 from the persona]            | [person's role] | [value ID + title] (e.g. AV-01 + title) | Covered |
| 5 | [challenge 1 from the persona]            | [person's role] | — none — | GAP |

SUMMARY:
  Covered: X / Y (Z%)
  Weakly covered: X
  Gaps: X <- these are candidates for new values
```

### Coverage statuses

- **Covered** — a PSO (Problem · Solution · Outcome) value directly addresses this problem with a concrete outcome
- **Weakly covered** — a value exists, but it's vague, lacks a concrete outcome, isn't tailored to the role, or addresses the problem only partially
- **GAP** — there is no value at all for this problem, challenge, or objection

### What to check in the persona

Work systematically through:
1. **The problems of each person involved in the purchase** — separately per role (CEO, Director, Manager, User)
2. **Challenges** — barriers that make it hard to reach the goals
3. **Objections** — reservations about the change or purchase
4. **Selection criteria** — if the persona describes them, check whether a value answers each one
5. **Buying process stages** — if described, check whether you have values for each stage (Solution exploration, Requirements building, Supplier selection, Purchase)

---

## Priority matrix

This Impact/Effort matrix belongs to the same Impact-vs-Effort prioritization family as ICE and RICE scoring: it weighs the likely payoff of a value against the effort to deliver it.

### Scoring dimensions

Score each dimension 1-10, then read off its band (**Easy/Low = 1-3, Medium = 4-7, Hard/High = 8-10**) to place the value on the matrix below.

**Implementation difficulty / cost (1-10):**

| Rating | Label | Description | Examples |
|-------|----------|------|-----------|
| 1-3 | Easy | Implementation immediately or within weeks. No significant cost. Mostly a matter of a decision and communication. | Changing how the offer is presented, adding a section to the website, creating a checklist, changing a service process |
| 4-7 | Medium | A few weeks to months of work, a moderate budget. New processes, tools, or team training. | Building an ROI calculator, an onboarding program, regular reporting, a new service procedure |
| 8-10 | Hard | Months of work, a large budget, new competencies, or hiring. Changes to the product or infrastructure. | Developing a new product module, certification, building a warehouse, a new production line |

**Impact on sales (1-10):**

| Rating | Label | Description | Examples |
|-------|----------|------|-----------|
| 1-3 | Low | Nice-to-have. Doesn't change the buying decision. Affects few customers or a peripheral problem. | An extra report, a minor convenience, a cosmetic improvement |
| 4-7 | Medium | Strengthens the offer and can tip the scales against the competition. A significant but not critical problem. | Better after-sales service, faster response time, additional training |
| 8-10 | High | Addresses a critical problem that blocks sales. Without this value, the company loses deals. Affects many customers. | Solving the customer's main pain, eliminating a key objection, a value that's impossible to copy |

### The 3×3 matrix with implementation priorities

```
                              IMPACT ON SALES
                    Low (1-3)   Medium (4-7)  High (8-10)
                  +------------+------------+------------+
    Easy (1-3)    | Priority   | Priority   | Priority   |
                  |    4       |    2       |    1       |
                  | Do it when | Do it this | DO IT NOW  |
                  | there's    | month      |            |
                  | time       |            |            |
D                 +------------+------------+------------+
I  Medium (4-7)   | Priority   | Priority   | Priority   |
F                 |    6       |    3       |    2       |
F                 | Consider   | Plan for   | Plan for   |
I                 |            | the quarter| this month |
C                 |            |            |            |
U                 +------------+------------+------------+
L   Hard (8-10)   | Priority   | Priority   | Priority   |
T                 |    7       |    5       |    3       |
Y                 | Shelve it  | Plan       | Plan for   |
                  |            | strategi-  | the quarter|
                  |            | cally      |            |
                  +------------+------------+------------+
```

### Order of priorities (sort results in this order)

| Priority | Difficulty | Impact | Recommendation |
|-----------|----------|-------|--------------|
| **1** | Easy (1-3) | High (8-10) | **DO IT NOW** — Quick wins. Maximum effect for minimal effort. |
| **2** | Easy (1-3) / Medium (4-7) | Medium-High (4-10) | **Plan for this month** — A strong return on the time and money invested. |
| **3** | Medium (4-7) / Hard (8-10) | High (8-10) | **Plan for the quarter** — Big impact, but resource-intensive. Worth it, just not right now. |
| **4** | Easy (1-3) | Low (1-3) | **Do it when there's time** — Simple, but little effect. Don't prioritize. |
| **5** | Hard (8-10) | Medium (4-7) | **Plan strategically** — Demands a lot, returns a moderate amount. Weigh whether it's worth it. |
| **6** | Medium (4-7) | Low (1-3) | **Consider** — Moderate effort, small effect. Low priority. |
| **7** | Hard (8-10) | Low (1-3) | **Shelve it** — A lot of work, small effect. Don't do it now. |

---

## Output file format

### File 1: `missing-pso.md` (Markdown — full documentation)

```markdown
# Missing Value Propositions — Gap Analysis
Company: [Company name]
Date: [date]
Model: Ananas-Agency Gap Analysis

## Coverage analysis

### Buyer Persona: [Persona 1 name]
[Coverage table — see pattern above]

### Buyer Persona: [Persona 2 name] (if applicable)
[Coverage table]

## Identified gaps

*Each gap carries a stable `MV-` ID (`MV = Missing Value` — proposed, not yet built). If a gap is later built, it becomes a regular `PV-/SV-/AV-` value in the Value Proposition skill.*

### Gap MV-01: [Title — a short description of the problem without a value]
- **Persona:** [persona name]
- **Role:** [who has this problem]
- **Problem from the persona:** [P — verbatim from the buyer persona]
- **Gap type:** Problem without a value / Role without a value / Stage without a value
- **Proposed value (PSO):**
  - **P:** [problem]
  - **S:** [what the company could do]
  - **O:** [what business outcome]
  > "[Complete PSO sentence in narrative form]"
- **Implementation difficulty:** [1-10] — [justification]
- **Impact on sales:** [1-10] — [justification]
- **Priority:** [1-7]

### Gap 2: [...]
[...]

## Priority matrix

[Visualization of the 3×3 matrix with the gaps placed in it]

## Implementation recommendations

### Do it now (Priority 1)
1. [Gap X] — [1 sentence on why first]

### Plan for this month (Priority 2)
1. [Gap Y]

### Plan for the quarter (Priority 3)
1. [Gap Z]

[...and so on for the remaining priorities, if any]

## Summary
- Personas analyzed: [number]
- Total number of problems/challenges/objections in the personas: [number]
- Covered by existing PSO: [number] ([%])
- Weakly covered: [number]
- Identified gaps: [number]
- New values proposed: [number]
- Quick wins (Priority 1): [number]
```

### File 2: `missing-pso.html` (styled, share-ready)

A single **self-contained** `.html` file (all CSS inline in one `<style>` block, **no external assets and no JavaScript**), so it opens in any browser, prints cleanly to PDF, and can be emailed as one file. Render the **same content** as the Markdown version. Keep the `<style>` block **identical to the shared design system** used across this suite (full CSS reproduced below).

- Render the per-persona coverage analysis as a `<table>`; mark each row's status with a `<span class="pill covered">COVERED</span>` or `<span class="pill gap">GAP</span>`.
- One `.card` per identified gap; show the priority as a `.badge`, and Problem / Solution / Outcome as `.row`s with the PSO (Problem · Solution · Outcome) sentence in a `<blockquote>`.
- Render the priority matrix and recommendations in their own blocks; close with a Summary block.


**Navigation & hints (required in every generated `.html`):**
- **Cross-link every reference to another deliverable.** Any mention of another document (the value list, a persona, the buying process, the dossier…) becomes a relative link to its canonical file (`value-propositions.html`, `buyer-persona.html`, …; see dossier-format.md for the full list). Any value ID cited here links back to the value list with a tooltip carrying the value's full title, e.g. `<a href="value-propositions.html" title="PV-01 — AI invoice auto-coding">PV-01</a>`; `MV-` IDs link to `missing-pso.html`, `H#` hypotheses to `experiments-plan.html`, personas to `buyer-persona.html`.
- **Hover hints on short terms — every occurrence, not just the first.** Give a `title` tooltip to **every** appearance of the shorthand set — PSO, DMU, ICP, the ID prefixes (PV/SV/AV/MV), and the `validated`/`hypothesis` statuses — e.g. `<abbr title="Problem · Solution · Outcome — the value-proposition format">PSO</abbr>`. Be consistent across the whole document; the final regeneration verifies these hints pack-wide.
- **No Previous / Next buttons in this file.** Do **not** add a `pagenav` (Previous/Next) block when generating this deliverable during the session — end the content with the Print hint instead. The walk navigation is wired **only in the final pack**, when the last skill regenerates every page in sequence order (see dossier-format.md, "Final consistency pass").
- **Print hint (no JavaScript).** End the page (after the last section, inside the content column) with `<p class="printhint">🖨 Print / Save as PDF — press <kbd>Ctrl</kbd>+<kbd>P</kbd> (<kbd>⌘</kbd>+<kbd>P</kbd> on Mac)</p>` — it uses the browser's own print (no button, no script) and hides itself automatically when printing.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Missing Value Propositions — Gap Analysis — [Company name]</title>
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
    <a class="pkgname" href="https://b2b-gtm-suite.ananas-agency.com/?utm_source=ananas-sales-skills&amp;utm_medium=deliverable&amp;utm_campaign=b2b-gtm-suite&amp;utm_content=missing-value-propositions" target="_blank" rel="noopener">B2B Go-to-Market Suite</a>
    <a class="brandlink" href="https://ananas-agency.com/?utm_source=ananas-sales-skills&amp;utm_medium=deliverable&amp;utm_campaign=b2b-gtm-suite&amp;utm_content=missing-value-propositions" target="_blank" rel="noopener">
      <span class="byline">by</span>
      <img class="brandlogo" src="https://ananas-agency.com/wp-content/uploads/2025/05/ananas-agency-logo-no-background-for-black.png" alt="Ananas Agency">
    </a>
  </div>
</div>

<div class="wrap">
  <header class="doc">
    <h1>Missing Value Propositions — Gap Analysis</h1>
    <div class="meta"><b>Company:</b> [Company name] &nbsp;·&nbsp; <b>Date:</b> [date] &nbsp;·&nbsp; <b>Model:</b> Ananas-Agency Gap Analysis</div>
  </header>

  <section class="block">
    <h2 class="section">Coverage analysis — [Persona 1 name]</h2>
    <table>
      <tr><th>#</th><th>Problem / Challenge / Objection</th><th>Role</th><th>Existing value</th><th>Status</th></tr>
      <tr><td>1</td><td>[problem]</td><td>[role]</td><td><span class="id">PV-03</span></td><td><span class="pill covered">COVERED</span></td></tr>
      <tr><td>2</td><td>[problem]</td><td>[role]</td><td>— none —</td><td><span class="pill gap">GAP</span></td></tr>
    </table>
    <div class="row"><span class="k">Coverage</span>X/Y (Z%) &nbsp;·&nbsp; <span class="k">Gaps</span>X</div>
  </section>

  <section class="block">
    <h2 class="section">Identified gaps</h2>
    <article class="card">
      <h3><span class="id">MV-01</span> Gap — [Title] <span class="badge">Priority [1-7]</span></h3>
      <div class="row"><span class="k">Persona</span>[name] &nbsp;·&nbsp; <span class="k">Role</span>[who]</div>
      <div class="row"><span class="k">Gap type</span>[Problem / Role / Stage without a value]</div>
      <div class="row"><span class="k">Problem</span>[P]</div>
      <div class="row"><span class="k">Solution</span>[S]</div>
      <div class="row"><span class="k">Outcome</span>[O]</div>
      <blockquote>"[Complete PSO sentence]"</blockquote>
      <div class="row"><span class="k">Difficulty</span>[1-10] &nbsp;·&nbsp; <span class="k">Impact</span>[1-10]</div>
    </article>
    <!-- further gaps as more .card blocks -->
  </section>

  <section class="block">
    <h2 class="section">Priority matrix</h2>
    <div class="row">[3×3 matrix with the gaps placed in it]</div>
  </section>

  <section class="block">
    <h2 class="section">Implementation recommendations</h2>
    <div class="row"><span class="k">Do it now (Priority 1)</span>[Gap X] — [why first]</div>
    <div class="row"><span class="k">This month (Priority 2)</span>[Gap Y]</div>
    <div class="row"><span class="k">This quarter (Priority 3)</span>[Gap Z]</div>
  </section>

  <section class="block">
    <h2 class="section">Summary</h2>
    <div class="row"><span class="k">Personas analyzed</span>[n]</div>
    <div class="row"><span class="k">Covered by existing PSO</span>[n] ([%])</div>
    <div class="row"><span class="k">Gaps / new values</span>[n] / [n]</div>
    <div class="row"><span class="k">Quick wins (Priority 1)</span>[n]</div>
  </section>
  <p class="printhint">🖨 Print / Save as PDF — press <kbd>Ctrl</kbd>+<kbd>P</kbd> (<kbd>⌘</kbd>+<kbd>P</kbd> on Mac)</p>
</div>

<footer class="doc">
  <div class="fwrap">
    <a class="brandlink" href="https://ananas-agency.com/?utm_source=ananas-sales-skills&amp;utm_medium=deliverable&amp;utm_campaign=b2b-gtm-suite&amp;utm_content=missing-value-propositions" target="_blank" rel="noopener">
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

Released under the MIT License — keeping the copyright notice is all that is required, and a credit to the author is warmly appreciated. Full license text: [LICENSE.md](../LICENSE.md)
