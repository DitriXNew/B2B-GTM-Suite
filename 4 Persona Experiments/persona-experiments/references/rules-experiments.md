# Experiment Rules — Detailed Reference

## Catalog of experiment methods

### Direct methods (highest value)

**1. Phone interview with a current customer**
- Description: A 15-20 min conversation with a customer who represents the segment
- Cost: €0
- Time: 30 min (preparation + conversation)
- What it tests: problems, value, buying process, roles
- How to do it: Call 3-5 current customers from the segment. Be upfront: "I want to better understand how you bought and what mattered most to you. The conversation will take 15 minutes."
- Note: Current customers carry a bias: they've already bought, so they'll tend to confirm the value. That's why you should also ask what was MISSING and what ALMOST stopped them.

**2. Interview with a prospect (cold)**
- Description: A 15-20 min conversation with someone from the segment who is NOT a customer
- Cost: €0
- Time: 45 min (sourcing the person + conversation)
- What it tests: problems, value, segment
- How to do it: Find 5-10 people on LinkedIn in a role from the buyer persona. Reach out: "I'm running research among [segment]. I'd like to talk for 15 minutes about the challenges in [area]. In return, I can share the findings."
- Note: The response rate will be low (10-20%). Reach out to at least 10 people to book 2-3 conversations.

**3. Micro-survey on LinkedIn**
- Description: A post with a question or a poll on LinkedIn targeting the segment
- Cost: €0
- Time: 20 min (writing the post)
- What it tests: problems, segment (whether the topic resonates)
- How to do it: Write a post describing a problem from the buyer persona and ask "Who here faces a similar situation?". Use a LinkedIn poll (max 4 options).
- Note: Engagement on a post ≠ readiness to buy. Treat it as a signal, not as proof.

### Indirect methods (supplementary)

**4. Value proposition sheet in PDF**
- Description: A one-page document with the 5-7 strongest value propositions, sent to customers/prospects for rating
- Cost: €0
- Time: 45 min (preparing the sheet)
- What it tests: value (whether it resonates, which points are strongest)
- How to do it: Prepare a PDF listing the value propositions in the format: Problem -> Our value -> Outcome. Send it to 5-10 people from the segment with the request: "Rate from 1 to 10 which of these points matter most to you."
- Note: It gives you a ranking of value propositions, but it doesn't replace a conversation.

**5. Cold email / cold LinkedIn message test**
- Description: Sending 20-30 outreach messages built around a problem and a value from the persona
- Cost: €0
- Time: 60 min (writing + sending)
- What it tests: problems (whether they resonate), segment (whether it's reachable), roles (whether the right person responds)
- How to do it: Write 2 message variants, each built around a DIFFERENT problem from the buyer persona. Send 15 of each variant. Compare the response rates.
- Note: A response rate <5% doesn't automatically mean the problem doesn't exist; it could be the wrong channel or the wrong timing. But >10% is a strong signal.

**6. Google Trends / Google Keyword Planner analysis**
- Description: Checking the search volume for phrases tied to the problems in the persona
- Cost: €0
- Time: 20 min
- What it tests: problems (whether people are actively searching for a solution), buying process (what phrases they use)
- How to do it: Enter phrases describing a problem from the persona into Google Trends. Check the trend (rising/falling) and the volume.
- Note: No searches ≠ no problem. Some B2B problems simply aren't googled.

**7. Analysis of industry groups and forums**
- Description: Reviewing discussions in LinkedIn groups, Facebook, and industry forums
- Cost: €0
- Time: 30 min
- What it tests: problems (whether people talk about them), language (how they describe the problem)
- How to do it: Find 2-3 groups where your segment is active. Search using phrases from the persona's problems. Check whether the topic surfaces and how people describe it.
- Note: It gives you the customer's language: how they REALLY talk about the problem (versus how we describe it).

**8. Mini landing page + paid advertising**
- Description: A simple page describing the problem and value + an ad on LinkedIn/Google on a minimal budget
- Cost: €50–120
- Time: 90 min (building the LP + setting up the ad)
- What it tests: problems, value, segment (whether it converts)
- How to do it: Create a simple page (even a Google Form) with a headline targeting the problem, a description of the value, and a CTA "Book a call". Drive traffic with an ad on LinkedIn targeting the segment.
- Note: Requires a minimal budget. The best method for testing conversion, but not always available.

### In-session methods (the assistant runs these now, in the chat)

These give **fast, directional signal during the session itself**: the assistant runs them from public information and reasoning, so you get a first read on the hypotheses before anyone leaves the chat. They **do not replace** talking to real customers (methods 1–2 stay the gold standard for problems and value); treat them as triangulation and as a way to sharpen the field experiments. Where the assistant has no web access, methods 10–12 fall back to reasoning from what the user has already provided.

**9. Offer / website teardown (in-session)**
- Cost: €0 · Time: in-chat · Tests: value (clarity, credibility)
- How: the assistant reviews the company's site and the value list and critiques each value from the buyer's point of view: is it clear, believable and specific, or vague? Flags values that won't survive a customer's "so what?".
- Note: tests how the value is *expressed*, not whether the customer needs it. A weak teardown means fix the wording; it doesn't refute the underlying value.

**10. Desk market-sizing & reachability (in-session)**
- Cost: €0 · Time: in-chat · Tests: segment
- How: the assistant estimates how many companies fit the segment and how reachable they are, from public data (industry statistics, company directories, LinkedIn filter counts).
- Note: a rough order-of-magnitude check: enough to catch a segment that's far too small or unreachable, not a precise market size.

**11. Search & language scan (in-session)**
- Cost: €0 · Time: in-chat · Tests: problems, language
- How: the assistant checks whether and how the segment searches for / discusses the problem (search interest, industry forums, LinkedIn) and reports back the customer's own wording.
- Note: same caveat as Google Trends: silence ≠ no problem; some B2B problems aren't searched. Use it for language and a directional read.

**12. Competitor desk research (in-session)**
- Cost: €0 · Time: in-chat · Tests: value (uniqueness), segment
- How: the assistant reviews competitors' sites and positioning to see which problems and values they already claim, sharpening the `unique` flag and surfacing gaps.
- Note: confirms what competitors *say*, not what they deliver. Feeds the competitor snapshot in Skill 1.

**13. AI persona role-play / red-team (in-session)**
- Cost: €0 · Time: in-chat · Tests: problems, value, roles, objections
- How: the assistant role-plays a person from the buyer persona and is pressure-tested on the problems, the value and the objections: either the user probes the "buyer", or the assistant argues the skeptical buyer's case against each value. Surfaces weak spots, missing objections and values that don't land.
- Note: a simulation, not evidence from a real customer (only as good as the persona). Its best use is to *find* what to test in the field and to rehearse objection handling. Never mark a value `validated` on role-play alone.

---

## Validation thresholds

### Interviews (methods 1-2)
- **Confirmed:** ≥7 out of 10 interviewees confirm the problem/value unprompted
- **Probable:** 5-6 out of 10 confirm — more data needed
- **Refuted:** ≤4 out of 10 confirm — the hypothesis needs to change

With a smaller sample (3-5 conversations):
- **Confirmed:** Everyone, or nearly everyone, confirms and offers their own examples
- **Probable:** Most confirm, but without enthusiasm
- **Refuted:** Most don't recognize the problem or say "it's not relevant to us"

### Cold outreach (method 5)
- **Strong signal:** Response rate >10% — the problem resonates
- **Moderate signal:** Response rate 5-10% — worth digging deeper
- **Weak signal:** Response rate <5% — revise the message or re-verify the hypothesis

### Value sheet (method 4)
- **Confirmed:** Value rated 8-10/10 by ≥70% of respondents
- **Probable:** Rated 6-7/10 — the value is there, but it's not a priority
- **Refuted:** Rated ≤5/10 — the value doesn't resonate

### Landing page (method 8)
- **Strong signal:** Ad CTR >2% + LP conversion >5%
- **Moderate:** CTR 1-2% — the message partly lands
- **Weak:** CTR <1% — the problem or segment doesn't resonate with the message

### Google Trends / groups (methods 6-7)
- These methods have no hard thresholds; they serve as supplementary signals, not as proof. Use them to triangulate with the other methods.

### In-session methods (methods 9-13)
- **Directional only — never conclusive.** No hard thresholds. A clean pass in-session raises confidence and can be recorded as `Source: hypothesis (in-session signal: positive)`, but a value only becomes `validated` after a **field** method (1–2, 4, 5 or 8) confirms it. A negative in-session read (the teardown shows the value is vague, the role-play buyer shrugs, the search scan finds nothing) is a strong prompt to sharpen or re-test: treat it as "needs work", not a final refutation.

---

## Results intake & write-back

The plan is only half the value; the other half is turning results into an updated strategy. Use this whether the results come from the **in-session** methods (now) or the **field** methods (when the user returns after the week).

### Paste-in format (give this to the user)
Ask the user to report results one hypothesis at a time, in this shape:

```
H# | method used | what you heard / measured (evidence) | confirmed / refuted / unclear
```

Example: `H3 | 6 customer interviews | 5/6 named onboarding time as their #1 pain and rated the value 9/10 | confirmed`

### How to interpret
1. Match the evidence to the **Validation thresholds** above for that method.
2. Settle the status: **confirmed / refuted / unclear**.

### Write-back (apply immediately — don't just log it)
For each result, update the **source of truth** (the value list and persona), not only the experiment file:
- **Confirmed by a field method (1–8):** set the value's `Source: validated`. If the evidence changed its strength, re-score (Problem weight + Outcome magnitude, max 20). **Keep the `PV-/SV-/AV-` ID unchanged.**
- **Confirmed in-session only (9–13):** keep `Source: hypothesis` but annotate `(in-session signal: positive)`; it is not yet validated.
- **Refuted:** set/keep `Source: hypothesis` and record the change needed (sharper problem, re-worded value, wrong segment or role). Flag it for a re-test.
- **Unclear:** leave as `hypothesis`; note what extra evidence is needed.
- **Persona:** apply the same reality-checks — corrected segment, new objections, roles that don't actually decide.
- **Then propagate:** write the re-scores and `Source` flips into the Value Proposition deliverable (`value-propositions.md`) and the dossier's Value Propositions section. Later skills read `Source` and Score from there, not from the experiment log.

---

## Interview question patterns

### Questions about problems (DON'T lead)
- "What are your 3 biggest frustrations in [area]?"
- "What eats up the most of your time that really shouldn't?"
- "If you could magically solve one problem in the company, what would it be?"
- "What has changed over the past year that makes your work harder?"

### Questions about value (after discussing problems)
- "If someone offered [value], how useful would that be to you? Scale 1-10."
- "What would have to happen for you to decide to pay for it?"
- "How much would you be willing to pay for it?"
- "Have you tried to solve it another way? How?"

### Questions about the buying process
- "What did the decision process look like the last time you bought [a similar service/product]?"
- "Who else was involved in the decision?"
- "How long did it take from the first thought to signing the contract?"
- "What almost stopped you from buying?"

### IMPORTANT: Don't lead
WRONG: "Do you have a problem with salesperson turnover?"
RIGHT: "What challenges do you have in the sales department?"

A leading question produces a falsely positive answer. The customer will say "yes" just to be polite.

---

## Weekly plan pattern

### Day 1 (2h): Preparation
- 30 min: Review the hypotheses, decide which to test
- 30 min: Write the interview questions
- 30 min: Prepare the value sheet (PDF) or the cold email variants
- 30 min: Send out call invitations / cold emails / a LinkedIn post

### Day 2 (2h): First conversations + analysis
- 60 min: 2-3 phone interviews (20 min each)
- 30 min: Write up the key takeaways from the conversations
- 30 min: Google Trends / industry group analysis

### Day 3 (2h): More conversations + cold outreach
- 60 min: 2-3 more interviews
- 60 min: Send cold emails/LinkedIn messages (if not done on day 1) + monitor responses

### Day 4 (2h): Filling gaps + going deeper
- 60 min: Additional conversations or follow-up with those who replied to the cold outreach
- 30 min: Collect responses to the value sheet
- 30 min: Preliminary analysis of the results

### Day 5 (2h): Analysis and conclusions
- 60 min: Gather all the results, compare them with the hypotheses, fill in the results table
- 60 min: Refine the buyer persona and value propositions based on the results + decide on next steps

---

## Output file format

### File 1: `experiments-plan.md` (Markdown)

```markdown
# Experiments Plan — [Segment name] — [Company name]
Date: [date]
Model: Ananas-Agency Experiments

## Hypotheses to test

*IDs: `H1`, `H2`, … = Hypothesis (assigned in Step 2, reused across the plan).*

### Priority 1: Problems and challenges
| # | Hypothesis | Confidence | Test methods |
|---|----------|---------|-------------|
| H1 | [Segment has problem X] | Risky | Interview, cold email |
| H2 | [Segment has challenge Y] | Probable | Interview, LinkedIn |

### Priority 2: Value propositions
| # | Hypothesis | Confidence | Test methods |
|---|----------|---------|-------------|
| H3 | [Value PV-03 resonates with the segment] | Risky | PDF sheet, interview |

### Priority 3: Segment, roles, process
| # | Hypothesis | Confidence | Test methods |
|---|----------|---------|-------------|
| H4 | [Segment is reachable] | Probable | Google Trends, cold outreach |

---

## Weekly plan

### Day 1 — Monday (2h)
**Goal of the day:** [goal]

| Time | Task | Tests hypothesis | Materials |
|------|---------|-----------------|-----------|
| 30 min | [task] | H1, H2 | [what to prepare] |
| 30 min | [task] | H3 | [what to prepare] |
| 60 min | [task] | H1-H4 | [what to prepare] |

[repeat for days 2-5]

---

## Materials to prepare

### Interview questions
[list of questions matched to the hypotheses]

### Value sheet (to send to customers)
[description + content of the sheet]

### Cold email variants
**Variant A (tests problem X):**
[content]

**Variant B (tests problem Y):**
[content]

---

## Success criteria

| # | Hypothesis (full statement) | Confirmed when | Refuted when |
|---|-----------------------------|-----------------|-------------|
| H1 | [full hypothesis statement, not just "H1"] | [criterion] | [criterion] |
| H2 | [full hypothesis statement] | [criterion] | [criterion] |

---

## In-session findings (Step 6 — done during the session)

| # | Hypothesis (full statement) | Method | Signal | Directional status | What it means |
|---|-----------------------------|--------|--------|--------------------|---------------|
| H1 | [full hypothesis statement, not just "H1"] | Persona role-play | [what surfaced] | positive / negative / mixed | [sharpen / proceed to field test] |

*In-session signals are directional, not validation — a value becomes `validated` only after a field method confirms it.*

---

## Results table (to fill in after the week — field methods)

*Print this page and write in the blanks, or copy this table straight into Excel / Word to fill it in.* Spell each hypothesis out **in full** in the Hypothesis column — repeat the wording from the hypotheses list, not just its `H#` — so every row makes sense on its own. Leave the Result / Evidence / Status / Action cells blank for the user to complete.

| # | Hypothesis (full statement) | Result | Evidence | Status | Action |
|---|-----------------------------|--------|----------|--------|--------|
| H1 | [full hypothesis statement, e.g. "SME manufacturers lose 3–4h/week reconciling orders across 3 suppliers"] |  |  | confirmed / refuted / unclear |  |
| H2 | [full hypothesis statement] |  |  | confirmed / refuted / unclear |  |
```

### File 2: `experiments-plan.html` (styled, share-ready)

A single **self-contained** `.html` file (all CSS inline in one `<style>` block, **no external assets and no JavaScript**), so it opens in any browser, prints cleanly to PDF, and can be emailed as one file. Render the **same content** as the Markdown version. Keep the `<style>` block **identical to the shared design system** used across this suite (full CSS reproduced below).

- This deliverable is table-heavy: render hypotheses, the weekly plan, success criteria, and the (blank) results table as `<table>`s, each inside its own `<section class="block">`.
- **Make the results table fillable.** Every H-row must spell out the hypothesis in full in the Hypothesis column (not just `H1`). Give the Result / Evidence / Status / Action cells **visible empty cells** (`&nbsp;` with a light cell border) so the table prints as a clean fill-in grid and pastes cleanly into Excel or Word. Put a one-line caption directly above it: *"Print this page or paste this table into Excel to fill it in."* Don't use `<input>`/`<textarea>` or any script — keep it a plain, printable `<table>`.
- Render the cold-email variants as `.card` blocks; interview questions as `<ul class="clean">`.


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
<title>Experiments Plan — [Segment name] — [Company name]</title>
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
    <a class="pkgname" href="https://b2b-gtm-suite.ananas-agency.com/?utm_source=ananas-sales-skills&amp;utm_medium=deliverable&amp;utm_campaign=b2b-gtm-suite&amp;utm_content=persona-experiments" target="_blank" rel="noopener">B2B Go-to-Market Suite</a>
    <a class="brandlink" href="https://ananas-agency.com/?utm_source=ananas-sales-skills&amp;utm_medium=deliverable&amp;utm_campaign=b2b-gtm-suite&amp;utm_content=persona-experiments" target="_blank" rel="noopener">
      <span class="byline">by</span>
      <img class="brandlogo" src="https://ananas-agency.com/wp-content/uploads/2025/05/ananas-agency-logo-no-background-for-black.png" alt="Ananas Agency">
    </a>
  </div>
</div>

<div class="wrap">
  <header class="doc">
    <h1>Experiments Plan — [Segment name] — [Company name]</h1>
    <div class="meta"><b>Date:</b> [date] &nbsp;·&nbsp; <b>Model:</b> Ananas-Agency Experiments</div>
  </header>

  <section class="block">
    <h2 class="section">Hypotheses to test</h2>
    <p style="color:var(--muted);font-size:13px;margin:0 0 8px">H1, H2, … = Hypothesis (assigned in Step 2).</p>
    <table>
      <tr><th>#</th><th>Hypothesis</th><th>Confidence</th><th>Test methods</th></tr>
      <tr><td>H1</td><td>[hypothesis]</td><td>Risky</td><td>Interview, cold email</td></tr>
    </table>
  </section>

  <section class="block">
    <h2 class="section">Weekly plan — Day 1 (2h)</h2>
    <table>
      <tr><th>Time</th><th>Task</th><th>Tests</th><th>Materials</th></tr>
      <tr><td>30 min</td><td>[task]</td><td>H1, H2</td><td>[prepare]</td></tr>
    </table>
    <!-- repeat a table per day 2–5 -->
  </section>

  <section class="block">
    <h2 class="section">Materials to prepare</h2>
    <div class="row"><span class="k">Interview questions</span></div>
    <ul class="clean"><li>[question]</li></ul>
    <article class="card"><h3>Cold email — Variant A (tests problem X)</h3><div class="row">[content]</div></article>
    <article class="card"><h3>Cold email — Variant B (tests problem Y)</h3><div class="row">[content]</div></article>
  </section>

  <section class="block">
    <h2 class="section">Success criteria</h2>
    <table>
      <tr><th>#</th><th>Hypothesis</th><th>Confirmed when</th><th>Refuted when</th></tr>
      <tr><td>H1</td><td>[problem X]</td><td>[criterion]</td><td>[criterion]</td></tr>
    </table>
  </section>

  <section class="block">
    <h2 class="section">Results (fill in after the week)</h2>
    <table>
      <tr><th>#</th><th>Result</th><th>Evidence</th><th>Status</th><th>Action</th></tr>
      <tr><td>H1</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
    </table>
  </section>
  <p class="printhint">🖨 Print / Save as PDF — press <kbd>Ctrl</kbd>+<kbd>P</kbd> (<kbd>⌘</kbd>+<kbd>P</kbd> on Mac)</p>
</div>

<footer class="doc">
  <div class="fwrap">
    <a class="brandlink" href="https://ananas-agency.com/?utm_source=ananas-sales-skills&amp;utm_medium=deliverable&amp;utm_campaign=b2b-gtm-suite&amp;utm_content=persona-experiments" target="_blank" rel="noopener">
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
