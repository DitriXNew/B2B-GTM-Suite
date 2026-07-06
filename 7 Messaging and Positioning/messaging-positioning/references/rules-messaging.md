# Messaging & Positioning Rules — Detailed Reference

This is the detailed reference for the `messaging-positioning` skill: the templates,
patterns, and output-file format for every deliverable. The main skill links here.

---

## 1. Positioning statement

**Formula:**

> For **[ICP / segment]** who **[priority problem]**, we are the **[category]** that **[core value / outcome]**, unlike **[alternative]**, because **[reason to believe]**.

Rules:
- `[core value / outcome]` = the **strongest value by Score**, cited by ID (prefer a `validated` one). It does **not** need to be `unique`; lead with what's most compelling.
- `[alternative]` is a real option from the competitor snapshot: a named competitor, the status quo, or "doing it in-house / in a spreadsheet". Where you have a `unique` value, use it to sharpen this contrast. If the user ran **Competitor Analysis**, take the named alternative per value from its positioning read.
- `[reason to believe]` is proof: a number from an Outcome, a certification, a track record.

**Example:**
> For mid-size ceramic-tile manufacturers who lose deals when a single SKU is out of stock (**problem**), we are the distributor that keeps 4500 SKUs in one place so you fulfil a full order in one PO (**core value, SV-02**), unlike single-line suppliers, because we hold €1–2M of regional stock on hand (**reason to believe**).

Draft 2–3 variants; let the user choose and sharpen.

---

## 2. Message house (core message + 3 pillars)

The reusable hierarchy everything else hangs on. One roof line, three pillars, proof under each.

```
ROOF (core message, one sentence — usually a sharpened positioning statement)
├── PILLAR 1: [theme, e.g. "Fast to live"]      ├── PILLAR 2: [theme]        ├── PILLAR 3: [theme]
│   · value [ID] + Outcome number               │   · value [ID] + number    │   · value [ID] + number
│   · value [ID] + Outcome number               │   · proof point            │   · proof point
```

Rules: each pillar is a **theme that clusters 2–3 values** (by ID); every pillar carries at least one **number** from an Outcome. Pillars must be distinct: if two pillars could share a headline, merge them and find a third.

## 3. Boilerplates & pitches

- **Boilerplate 25 / 50 / 100 words** — the standard company descriptions for press, directories, proposals, LinkedIn "About". All three derive from the positioning statement; the 100-word version cites the three pillars. Write all three in full.
- **Elevator pitch 10s (~30 words)** — problem + what you do + the sharpest number.
- **Elevator pitch 30s (~80 words)** — adds for-whom, the "unlike", and one proof point.
- **Taglines** — 3–5 options, each ≤6 words, at least one derived from a `unique` value.

---

## 4. Messaging matrix

A table of **DMU role × buying stage**, each cell one line citing the value ID it draws on.
Fill the decisive cells first; leave low-value cells blank rather than padding.

| DMU role | Problem identification | Solution exploration | Requirements building | Supplier selection | Validation / Purchase |
|----------|------------------------|----------------------|-----------------------|--------------------|-----------------------|
| Economic buyer | [line · ID] | [line · ID] | | [line · ID] | [line · ID] |
| Technical evaluator | | [line · ID] | [line · ID] | [line · ID] | |
| End user | [line · ID] | | [line · ID] | | |

If the buying process (Skill 5) wasn't built, drop the stage columns and keep **role × value ID** only, noting that the stage axis is missing.

---

## 5. Objection-handling cheat sheet

One row per persona objection. Keep the raw phrasing; anchor the rebuttal to a value ID.

| Objection (raw) | What's really behind it | Rebuttal | Value ID |
|-----------------|-------------------------|----------|----------|
| "Too expensive" | Comparing unit price, not total cost | "Per order you place one PO instead of three — that's 3–4h/week back." | SV-02 |
| "Not now" | No urgent trigger | "Every stockout is a lost order today, not next quarter." | PV-01 |
| "I have to check with someone" | Not the sole decider | "Happy to send a one-pager your [role] can skim in two minutes." | — |

## 6. Discovery questions

8–10 questions a rep asks in a first call, derived from the persona: each question targets a **problem, trigger, or objection** from the persona and sets up a specific value (note the ID it opens the door for). Mix: 3–4 problem questions, 2–3 trigger/urgency questions, 2–3 qualification questions (budget, DMU, timeline).

```
Q: "How do you handle [persona problem] today?"                 → opens [PV-xx]
Q: "What happened the last time [trigger event]?"               → urgency
Q: "Who besides you feels this when it goes wrong?"             → maps the DMU
```

---

## 7. Competitor battlecards

**One card per competitor** from the Competitor Analysis (fall back to the Skill-1 snapshot if the analysis wasn't run; then keep cards shorter and flag them as snapshot-based). Format:

```
BATTLECARD: [Competitor] ([direct / indirect / status quo])
- Their pitch (fair, one line): how they win deals
- They win when: [honest — from the analysis's "where we're exposed"]
- We win when:  [scenarios mapped to our unique/strong values, by ID]
- Kill questions: 2–3 questions the buyer should ask them (which surface their weakness
  without naming it) — e.g. "Ask any vendor: what's the guaranteed go-live date?"
- Landmines — never say: claims the evidence doesn't support (from the differentiation table)
- Proof: the number / reference that settles it
```

Rules: battlecards must stay **honest**; "they win when" is mandatory, and every "we win" claim traces to the differentiation table. A battlecard that only praises us is useless to a rep mid-deal.

---

## 8. Outreach assets

### Cold-email sequences — one per key role
Write a **separate 3–4-touch sequence for each of the two most important DMU roles** (typically the champion and the economic buyer): different pains, different values, different language. Each email ~90 words, one CTA, tied to a value ID and mapped to a buying stage. Where useful, give **two subject-line variants** (A/B) per email.

```
Sequence A — [Champion role, e.g. AP Manager]
  Email 1 (Problem identification) — Subject A/B: [their daily pain]
    Hook: the operational pain, in their words. Bridge: value [ID]. CTA: a reply, not a meeting.
  Email 2 (Solution exploration) — proof number from an Outcome [ID]; offer the one-pager.
  Email 3 (Requirements building) — the unlike/unique value [ID]; suggest a short call.
  Email 4 (break-up) — short, no guilt, easy re-open.

Sequence B — [Economic buyer, e.g. CFO]
  Same shape, but: cost/ROI language, budget-cycle timing, risk framing; values that
  speak to money and control [IDs].
```

### The forwardable email
A short note written **for the champion to forward to their boss**: 3–4 sentences, no salesiness, states the problem cost, the expected outcome (with the number, ID), and the small next step. Write it so the champion only has to add "thoughts?".

### LinkedIn
- **Connection / opener:** one line naming the shared context or the problem (no pitch).
- **Follow-up 1:** the differentiator (cite value ID).
- **Follow-up 2:** a proof point + soft CTA.

### Call opener
Two sentences: the reason for the call (persona trigger) + a permission-based question.

---

## 9. Marketing assets

### One-pager — full copy, not an outline
Write the actual text: headline (= positioning), 3 value blocks (title + 1–2 sentences + Outcome number + ID), proof strip (logos / certifications / case number), CTA line. The user should be able to paste it into a design tool unchanged.

### Landing page — hero copy + section copy
- **Hero:** 3 headline variants (one problem-led, one outcome-led, one unlike-led) + subhead + CTA button text.
- **Sections, with real copy:** Problem (persona pain, 2–3 sentences) → Solution (top values by ID, one short paragraph each) → Proof (numbers, references) → CTA. Not a skeleton: write the sentences.

### LinkedIn ads
3 variants, each: headline (≤70 chars) + body (≤150 chars) + CTA, tied to a different value ID / pillar. Vary the angle: pain / outcome-number / unlike.

### Content topics
5–7 content-marketing topics derived from persona problems and buying-stage questions (each: working title + which stage it serves + the value ID it sets up). These feed a content calendar.

---

## Output file format

Deliver TWO files with the same content, mirroring the other skills in the suite.

### File 1: `messaging-playbook.md`
```markdown
# Messaging & Positioning Playbook — [Company name]
Date: [date]
Model: Ananas-Agency

## Positioning statement
> For [ICP] who [problem], we [category] that [value], unlike [alternative], because [proof].

## Message house
[roof + 3 pillars with value IDs and numbers]

## Boilerplates & pitches
[25w / 50w / 100w · 10s pitch · 30s pitch · taglines]

## Messaging matrix
[role × stage table, cells cite value IDs]

## Objection-handling cheat sheet
[objection table]

## Discovery questions
[8–10 questions, each noting the value ID it opens]

## Competitor battlecards
[one card per competitor]

## Outreach assets
### Cold-email sequence — [Champion role]
### Cold-email sequence — [Economic buyer role]
### Forwardable email
### LinkedIn
### Call opener

## Marketing assets
### One-pager (full copy)
### Landing page (hero variants + section copy)
### LinkedIn ads (3 variants)
### Content topics

## Source note
Built on [validated / hypothesis] inputs (from Persona Experiments, Skill 4); battlecards from
[Competitor Analysis / Skill-1 snapshot].
```

### File 2: `messaging-playbook.html` (styled, share-ready)
A single **self-contained** `.html` file: all CSS inline in one `<style>` block, **no
external assets and no JavaScript**. Render the **same content** as the Markdown version.
Keep the `<style>` block **identical to the shared design system** used across this suite
(reuse the exact block from `rules-pso.md` / `rules-buyer-persona.md`; do not restyle), and
reproduce the same **page frame**: the black brand band — the **suite name as a link** (to
`b2b-gtm-suite.ananas-agency.com`) on the **left**, and **"by" + the Ananas Agency logo** (linking
to ananas-agency.com) on the **right** — at the
top, the bordered gold-top header card, and the black footer band (logo, juicy@ananas-agency.com,
license line) at the bottom, so every deliverable in the suite shares one look. Map the sections onto the shared components:
positioning and the message house as lead `.card`s, the matrix / objection sheet / discovery
questions as tables, **one `.card` per battlecard**, each outreach and marketing asset as its own
`.block`, and value IDs shown as `.id` chips.

**Navigation & hints (required in every generated `.html`):**
- **Cross-link every reference to another deliverable.** Any mention of another document (the value list, a persona, the buying process, the dossier…) becomes a relative link to its canonical file (`value-propositions.html`, `buyer-persona.html`, …; see dossier-format.md for the full list). Any value ID cited here links back to the value list with a tooltip carrying the value's full title, e.g. `<a href="value-propositions.html" title="PV-01 — AI invoice auto-coding">PV-01</a>`; `MV-` IDs link to `missing-pso.html`, `H#` hypotheses to `experiments-plan.html`, personas to `buyer-persona.html`, competitors to `competitor-analysis.html`.
- **Hover hints on short terms — every occurrence.** Give a `title` tooltip to **every** appearance (not just the first) of the fixed set — PSO, DMU, ICP, the ID prefixes (PV/SV/AV/MV), and the `validated`/`hypothesis` statuses: `<abbr title="Problem · Solution · Outcome — the value-proposition format">PSO</abbr>`. No bare ID codes anywhere.
- **Print hint; no nav mid-session.** End the page (after the last section, inside the content column) with the no-JavaScript Print hint `<p class="printhint">🖨 Print / Save as PDF — press <kbd>Ctrl</kbd>+<kbd>P</kbd> (<kbd>⌘</kbd>+<kbd>P</kbd> on Mac)</p>`. Do **not** add a `pagenav` when first generating this file; the prev/next walk is wired for every page in the **final regeneration** step (see the Finalize steps and dossier-format.md).

---

## License

Copyright (c) 2026 Kostiantyn Ivanov (Ananas-Agency, ananas-agency.com).

Released under the MIT License — keeping the copyright notice is all that is required, and a credit to the author is warmly appreciated. Full license text: [LICENSE.md](../LICENSE.md)
