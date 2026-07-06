# Buying Process Rules — Detailed Reference

### How the 5 stages map to recognized models

The 5 stages are Ananas-Agency's own framing of the **buyer's journey**. They map roughly onto Gartner's six B2B "buying jobs": problem identification, solution exploration, requirements building, supplier selection, validation, and consensus creation. The Ananas-Agency stages compress and rephrase these jobs rather than mirror them one-to-one. Use this only as orientation: keep the 5 stages as named below.

## Probing questions per stage

### Stage 1: Problem identification
- What most often kicks off the buying process in this segment? (a specific event)
- Who at the customer's company is the first to notice the problem?
- Is the trigger sudden (a failure, losing a customer) or gradual (results declining over several quarters)?
- How strong does the trigger have to be before the company acts on a purchase?
- What % of companies in the segment have this problem but aren't doing anything about it yet?

### Stage 2: Solution exploration
- How does the customer look for solution options? (Google, asking contacts, conferences, a consultant)
- What ALTERNATIVE concepts do they weigh? (e.g. instead of buying a CRM, hiring an Excel admin)
- Who at the customer's company takes part in choosing the concept?
- Does the customer know ballpark prices at this stage? Where do they get them from?
- How long does this stage last? Do customers sometimes skip it (because they already know)?
- What makes the customer get stuck at this stage and stall?

### Stage 3: Requirements building
- Where does the customer look for detailed information? (vendor websites, comparison sites, YouTube, webinars, trade fairs)
- Does the customer meet with salespeople at this stage? How many?
- What questions does the customer ask at this stage?
- What do they read / watch / whom do they talk to?
- Which roles at the customer's company get involved at this stage?
- What makes the customer move on to the Supplier selection stage rather than loop back to Solution exploration?

### Stage 4: Supplier selection
- Who at the customer's company makes the "what we're buying and for how much" decision?
- How do the requirements / specification take shape? (RFP, an internal meeting, a criteria spreadsheet)
- Where does the budget come from? Who approves it?
- What criteria matter most at this stage? (price, parameters, references, implementation time)
- How long does it take to get from "we know what we want" to "we have a budget"?

### Stage 5: Validation / Purchase
- How many suppliers does the customer compare at this stage?
- What decides the choice of supplier? (price, relationship, speed, references, value proposition)
- Who signs the contract / order?
- What do the negotiations look like? (tender, one-on-one talks, auction)
- What can block the purchase at this final stage? (a shift in priorities, a change of management, no budget)

---

## Common mistakes in describing the buying process

### Describing the SELLING process instead of the BUYING process
WRONG: "The salesperson calls, books a meeting, runs a presentation, sends an offer"
RIGHT: "After losing a key customer, the customer searches Google for 'how to improve B2B sales', lands on a podcast, listens to 3 episodes, and fills out a form on the website"

### Assuming linearity
WRONG: "The customer moves through the 5 stages in order"
RIGHT: "The customer typically starts with problem identification, spends 2-3 months at the Solution exploration stage, loops back to Problem identification (because the problem temporarily eased), then jumps to Requirements building"

### Generalities instead of specifics
WRONG: "The customer looks for information online"
RIGHT: "The production manager types 'MES systems comparison 2026' into Google, reads the ranking on Capterra, and asks the 'Manufacturing and Lean' LinkedIn group for recommendations"

### Skipping what the customer does WITHOUT the company
The customer runs most of the buying process on their own, with no contact with a salesperson. Describe what the customer does before they ever reach out.

---

## Generating recommendations

### Recommendations for the salesperson (per stage)

Recommendation structure:
- **Whom:** which role from the buyer persona
- **Why now:** what trigger/signal shows that the customer is at this stage
- **Through which channel:** cold email, LinkedIn, phone, trade fairs, referral
- **With what message:** a specific message built on a value proposition from the PSO (Problem · Solution · Outcome), citing that value by its ID
- **What NOT to do:** the salesperson's typical mistake at this stage

Example:
> **Stage 2 (Solution exploration) — Salesperson:**
> Whom: Person running the company
> Why now: The company posted a job opening for a sales director (a signal that they're looking for a change)
> Channel: LinkedIn — personalized message
> Message: "I see you're hiring a sales director. Before you decide, it's worth knowing that 60% of our clients first organized their sales process and only then looked for someone to run it. I can show you how that works in practice." (value PV-03)
> What NOT to do: Don't send an offer at this stage: the customer doesn't yet know WHAT they want to buy.

### Suggestions for marketing (per stage)

Suggestion structure:
- **What material:** an article, webinar, comparison tool, calculator, case study, checklist
- **On what topic:** matched to what the customer is looking for at this stage
- **In what channel:** blog, YouTube, LinkedIn, Google Ads, newsletter
- **What goal:** building awareness, education, conversion to contact, decision support

Example:
> **Stage 3 (Requirements building) — Marketing:**
> Material: A comparison tool "CRM for manufacturing companies — 10 systems in one overview"
> Channel: Blog + SEO for the phrase "CRM for manufacturing comparison"
> Goal: A customer at the Requirements building stage is looking for comparisons. If ours is the best one out there, the customer reaches us before they ever contact the competition.

---

## Output file format

### File 1: `buying-process.md` (Markdown)

```markdown
# Buying Process — [Segment name] — [Company name]
Date: [date]
Model: Ananas-Agency Buying Process

> **Note:** The buying process is non-linear. The customer doesn't always go 1->2->3->4->5.
> They go back, jump ahead, pause, give up. The description below presents
> a typical path, not the only possible one.

## Stage 1: Problem identification

### What the customer does
[specific actions]

### Where they do it
[channels and places]

### Who is involved
[roles from the buyer persona]

### How long it lasts
[estimated duration]

### What can stop the process
[blockers and risks]

### Recommendation for the salesperson
- **Whom:** [role]
- **Why now:** [signal]
- **Channel:** [way to reach them]
- **Message:** [based on a value proposition — cite its ID]
- **What NOT to do:** [typical mistake]

### Suggestion for marketing
- **Material:** [type]
- **Topic:** [description]
- **Channel:** [distribution]
- **Goal:** [what effect]

---

## Stage 2: Solution exploration
[same format]

## Stage 3: Requirements building
[same format]

## Stage 4: Supplier selection
[same format]

## Stage 5: Validation / Purchase
[same format]

---

## Drop-off risk map
[per stage — what causes the customer to drop off and how to prevent it]

## Summary
- Estimated length of the full process: [time]
- Stage with the highest drop-off risk: [which]
- Most important marketing material to create: [what]
- Key moment for the salesperson: [when and how to step in]
```

### File 2: `buying-process.html` (styled, share-ready)

A single **self-contained** `.html` file (all CSS inline in one `<style>` block, **no external assets and no JavaScript**), so it opens in any browser, prints cleanly to PDF, and can be emailed as one file. Render the **same content** as the Markdown version. Keep the `<style>` block **identical to the shared design system** used across this suite (full CSS reproduced below).

- The non-linear note goes in a `<blockquote>` near the top.
- One `.card` per stage (1–5), numbered in the card header.
- Within a stage, the salesperson recommendation and the marketing suggestion are `.row`s; cite value IDs as `.id` chips.
- Render the drop-off risk map as a `<table>`; close with a Summary block.


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
<title>Buying Process — [Segment name] — [Company name]</title>
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
    <a class="pkgname" href="https://b2b-gtm-suite.ananas-agency.com/?utm_source=ananas-sales-skills&amp;utm_medium=deliverable&amp;utm_campaign=b2b-gtm-suite&amp;utm_content=buying-process" target="_blank" rel="noopener">B2B Go-to-Market Suite</a>
    <a class="brandlink" href="https://ananas-agency.com/?utm_source=ananas-sales-skills&amp;utm_medium=deliverable&amp;utm_campaign=b2b-gtm-suite&amp;utm_content=buying-process" target="_blank" rel="noopener">
      <span class="byline">by</span>
      <img class="brandlogo" src="https://ananas-agency.com/wp-content/uploads/2025/05/ananas-agency-logo-no-background-for-black.png" alt="Ananas Agency">
    </a>
  </div>
</div>

<div class="wrap">
  <header class="doc">
    <h1>Buying Process — [Segment name] — [Company name]</h1>
    <div class="meta"><b>Date:</b> [date] &nbsp;·&nbsp; <b>Model:</b> Ananas-Agency Buying Process</div>
  </header>

  <section class="block">
    <blockquote>The buying process is non-linear. The customer doesn't always go 1→2→3→4→5 — they go back, jump ahead, pause, give up. The path below is typical, not the only one.</blockquote>

    <article class="card">
      <h3>Stage 1 — Problem identification</h3>
      <div class="row"><span class="k">What the customer does</span>[actions]</div>
      <div class="row"><span class="k">Where</span>[channels]</div>
      <div class="row"><span class="k">Who is involved</span>[roles]</div>
      <div class="row"><span class="k">How long</span>[time]</div>
      <div class="row"><span class="k">What can stop it</span>[blockers]</div>
      <div class="row"><span class="k">Salesperson</span>Whom: [role] · Why now: [signal] · Channel: [way] · Message: [content + <span class="id">PV-03</span>] · Avoid: [mistake]</div>
      <div class="row"><span class="k">Marketing</span>Material: [type] · Topic: [desc] · Channel: [distribution] · Goal: [effect]</div>
    </article>
    <!-- Stages 2–5 as further .card blocks -->
  </section>

  <section class="block">
    <h2 class="section">Drop-off risk map</h2>
    <table>
      <tr><th>Stage</th><th>What causes drop-off</th><th>How to prevent it</th></tr>
      <tr><td>[stage]</td><td>[cause]</td><td>[prevention]</td></tr>
    </table>
  </section>

  <section class="block">
    <h2 class="section">Summary</h2>
    <div class="row"><span class="k">Full process length</span>[time]</div>
    <div class="row"><span class="k">Highest drop-off risk</span>[which stage]</div>
    <div class="row"><span class="k">Most important material</span>[what]</div>
    <div class="row"><span class="k">Key sales moment</span>[when and how]</div>
  </section>
  <p class="printhint">🖨 Print / Save as PDF — press <kbd>Ctrl</kbd>+<kbd>P</kbd> (<kbd>⌘</kbd>+<kbd>P</kbd> on Mac)</p>
</div>

<footer class="doc">
  <div class="fwrap">
    <a class="brandlink" href="https://ananas-agency.com/?utm_source=ananas-sales-skills&amp;utm_medium=deliverable&amp;utm_campaign=b2b-gtm-suite&amp;utm_content=buying-process" target="_blank" rel="noopener">
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
