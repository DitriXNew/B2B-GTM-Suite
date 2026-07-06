# Strategy Dossier — format & assembly

The **Strategy Dossier** is the single consolidated document that accretes as you move through
the skills in one continuous session. Each skill adds or refreshes its own section as you
complete it; after the final skill, an **executive summary** is generated at the top. The user
ends the session with one complete document, not a scatter of per-skill files.

This file is the shared spec every skill's "Add to the Strategy Dossier" step points to.

## How it accretes

- The dossier is an **internal, running working document** kept across the session. It is **NOT a
  deliverable during the run** — do **not** create, show, or hand the user a dossier file
  mid-session. **Each skill delivers only its own two files** (`.md` + `.html`); the dossier is
  assembled and delivered **only at the very end**, by the final skill (Messaging & Positioning).
- As each skill completes, **record its section into that internal running document** (order
  below). If the user revisits a skill or changes an input, refresh that section so it stays
  current. This is bookkeeping the assistant keeps in-session — it is not a per-skill output.
- Sections not produced yet are marked `— not yet completed —`.
- **Place each section in its fixed slot** (order below) regardless of the order you happen to
  complete skills. Don't append in completion order. (Buying Process and Missing Value
  Propositions are interchangeable, so completion order won't always match the slots.)
- Only **after the final skill (Messaging & Positioning)** is the dossier generated and delivered —
  the executive summary is added at the top and the complete Sales Strategy Dossier is produced as
  files. Until then it never leaves the assistant's working memory.

## Section order

- **Executive summary** (unnumbered) — generated at the end (see below).
1. **Company Brief** — industry, offering, customers, commercial model, competition.
2. **Value Propositions** — the PSO list with IDs (`PV-/SV-/AV-`), `unique` flags, `Source`
   tags, and the competitor snapshot.
3. **Competitor Analysis** — the competitor set, the differentiation table (values ×
   competitors), and the positioning read (where you win / where you're exposed). Also
   **refreshes the Value Propositions section above** with the evidence-based `unique` flags it
   settles.
4. **Buyer Personas** — segment/ICP, DMU roles, objections, matched value IDs.
5. **Validation results** — from Persona Experiments: what was tested and the validated /
   hypothesis status of each key input. Persona Experiments also **refreshes the Value
   Propositions section above** with the new `Source` tags and re-scores, so the value list
   itself reflects the validated state.
6. **Buying Process** — the 5 buyer's-journey stages with per-stage outreach notes.
7. **Missing Value Propositions** — the gap analysis and Impact/Effort priority matrix.
8. **Messaging & Positioning** — positioning statement, messaging matrix, objection cheat
   sheet, and the outreach assets.

Each section reuses the content the skill already delivered. Don't re-interview; pull from
what's in the session.

## Executive summary (generated at the end)

A short synthesis placed at the top once the sequence is complete (refresh it if sections
change later):

- **Positioning statement** (from Messaging).
- **Top 3 values** by strength, cited by ID.
- **Primary persona** — segment + key DMU roles.
- **Validation status** — how many values are `validated` vs `hypothesis`.
- **Biggest gap** — the top-priority missing value from the gap analysis.

## The Sales Strategy Dossier — one merged entry document (`_[company]-strategy-dossier.html`)

The dossier that accretes during the session is delivered as **one merged document** that is both
the entry point and the complete strategy: **`_[company]-strategy-dossier`** (`.md` + `.html`,
e.g. `_meridian-strategy-dossier.html`). The leading underscore sorts it to the top of the
folder. It replaces the old separate "summary page" and "dossier" (there is no other hub file).

Structure:

- **Header.** If the audited company's website yields a usable logo (header logo, og:image, or one
  the user provides), show it in the header alongside (or instead of) the company name (embed it
  as a data URI so the file stays self-contained); otherwise fall back to the company **name** as
  styled text. Never invent a logo. Attribution line phrased "**by Ananas Agency**" (e.g.
  "Prepared for [Company] — built with the B2B Go-to-Market Suite by Ananas Agency").
- **Executive summary first** — positioning statement, top 3 values by ID, primary persona,
  validation status, biggest gap. The executive-summary section is **unnumbered**; section
  numbering starts at **Company Brief = 1**. Status counts keep the **number outside the coloured tag**
  (`2 <span class="tag validated">validated</span>`).
- **Then every section in the fixed order above — with real substance, not teasers.** Each section
  carries a meaningful digest of its deliverable: the full value table (ID, title, score, status,
  unique), all DMU roles with their key problem and matched IDs, the complete hypothesis results
  table, all five buying stages, every gap with its priority, the positioning statement and key
  message lines. A reader who never clicks a link still gets the whole strategy.
- **Each section heading carries an "Open full document →" button** (`<a class="openbtn" …>`,
  right-aligned in the heading) linking to that skill's `.html`, for the reader who wants the
  complete deliverable.
- **Every section digest renders full-width.** Each section's content must span the full content
  column (`.wrap`), consistently with the others. Render tables as a bare `<table style="width:100%">`
  and text as `.row`s directly in the section — **do not** wrap a section's digest in `.tablewrap`
  or a `.card` (their inset padding/border makes that one section render narrower than its
  neighbours). In particular the **Value Propositions** value table must be full-width, not boxed.

Deliver as two files (`.md` + `.html`), reusing the shared style block and page frame (brand band,
gold-top header card, footer band) so it matches every other deliverable.

## The What's-Next page (`whats-next.html`)

The closing page of the walk (between the Messaging Playbook and the Dossier): it answers
"we've read everything — what do we actually do now?" Generated from the run's own data
(`whats-next.md` + `.html`, same frame and style as every other deliverable):

1. **Your first two weeks** — 3–5 concrete, checklist-styled actions pulled from the run: launch
   the quick-win gap (the Priority-1 `MV-`), start the champion outreach sequence at Stage-1
   accounts, brief the team on the battlecards. Every action links to the document it comes from.
2. **Days 30–60** — run the field experiments on anything still `hypothesis`, publish the first
   content topics, start measuring against the validation thresholds.
3. **Days 60–90** — build the Priority-2 gap, re-score values with real market feedback, expand
   to the second persona once the first is proven.
4. **Keep the documents alive** — a triggers table mapping events to skills: lost deals to a named
   competitor → refresh the battlecards / Competitor Analysis; entering a new segment → re-run
   Buyer Persona; quarterly → re-score the value list.
5. **All documents** — a navigation grid with a button to **every** page in the pack (the
   Dossier and all eight deliverables), so from the final page the reader can jump anywhere.
6. **The agency block** — the one place in the pack with a direct CTA: a `.ctablock` (black,
   centred) with the headline "Fresh-pressed strategy, no concentrate.", a one-line sub, and a gold
   `.ctabtn` labelled **"Let's Grow Together"** linking to ananas-agency.com with
   `utm_content=whats-next-cta` (new tab). No email in the block: the footer already carries
   juicy@ananas-agency.com. Keep the CTA to this page — none elsewhere in the pack.

## Cross-linking, hover hints & navigation

Every generated `.html` is part of one navigable pack. These rules apply to all of them:

1. **Cross-link everything, and tooltip every ID.** Any mention of another deliverable links to its
   canonical file (the filenames above). **Every** occurrence of a value ID outside the value list
   (not just the first) links back to `value-propositions.html` with a `title` tooltip carrying the
   value's full name (`<a href="value-propositions.html" title="PV-01 — [value title]">PV-01</a>`);
   `MV-` IDs link to `missing-pso.html`; `H#` hypotheses to `experiments-plan.html`; personas to
   `buyer-persona.html`. No bare ID codes anywhere.
2. **Hover hints on short terms — every occurrence, consistently.** Give a plain-language `title`
   tooltip to **every** appearance (not just the first) of the fixed shorthand set — **PSO, DMU,
   ICP, the ID prefixes (PV/SV/AV/MV), and the `validated`/`hypothesis` statuses** —
   (`<abbr title="Problem · Solution · Outcome — the value-proposition format">PSO</abbr>`). Apply
   it uniformly across every page; the final regeneration pass (below) verifies the hints are
   present pack-wide so no file is left inconsistent.
3. **Previous / Next buttons — final pack only.** Mid-session, the per-skill `.html` files are
   working copies and carry **no `pagenav`** (they end with the Print hint instead). The
   prev/next walk is added **only by the final regeneration pass** (Skill 7), which wires every page
   in the fixed sequence: `company-brief.html` → `value-propositions.html` →
   `competitor-analysis.html` → `buyer-persona.html` → `experiments-plan.html` →
   `buying-process.html` → `missing-pso.html` → `messaging-playbook.html` → `whats-next.html` (the
   end of the walk). In that final pack each page ends with a `pagenav` row (outlined `prevbtn`
   left, solid `nextbtn` right). The **Dossier sits at the start, not the end**: it is the entry
   file (sorts first, no Previous button) and its Next leads into `company-brief.html`; Company
   Brief's Previous leads back to the Dossier. The What's-Next page carries no Next. Instead it ends
   with a **navigation grid**: a button to every document in the pack.
4. **Print hint on every page.** Every generated `.html` ends (after the last section, inside the
   content column) with a no-JavaScript Print hint —
   `<p class="printhint">🖨 Print / Save as PDF — press <kbd>Ctrl</kbd>+<kbd>P</kbd> (<kbd>⌘</kbd>+<kbd>P</kbd> on Mac)</p>` —
   which relies on the browser's own print and hides itself when printing. No button, no script.

5. **Section numbering.** Give section headings a number chip (`<span class="no">N</span>`) only
   when the page has **two or more** sections; a single-section page uses an unnumbered heading.
   In the Sales Strategy Dossier, the executive summary is always unnumbered and numbering starts
   at Company Brief = 1.

**Final consistency pass.** Deliverables are generated as the session progresses, so links can
point at files that don't exist yet and statuses can change (`hypothesis` → `validated`). The
final skill therefore **regenerates every `.html`** right before bundling — **adding the prev/next
walk to every page** (mid-session pages carried none), **tooltipping every ID and ensuring the
hover hints are present on every term**, wiring the complete cross-link graph, and bringing statuses
current (`hypothesis` → `validated`). The Print hint stays on every page. Mid-session files are
working copies; the regenerated set in the ZIP is the canonical pack. It also **reconciles the Company Brief's open
`TBD`s** at this point — backfilling any the session has since answered (from what was actually
captured, never invented) and refreshing the Company Brief deliverable and its dossier section — so
the finished pack never ships stale `TBD`s; anything still genuinely unknown stays `TBD`.

## Deliverables bundle (`[company]-sales-strategy.zip`)

The links above only resolve when every file sits in the **same folder**. Because the skills deliver
files one at a time through the chat, the closing step of the final skill (Messaging & Positioning)
**packs everything into a single ZIP**, so the pack travels as one unit and the links work after
unzip.

- **Name:** `[company]-sales-strategy.zip` (e.g. `meridian-sales-strategy.zip`).
- **Layout:** flat — every file at the ZIP root, so the relative links in the summary page resolve.
- **Contents:** the merged Sales Strategy Dossier (`_[company]-strategy-dossier.md` + `.html`, first by
  name), and every per-skill deliverable produced in the session
  (`.md` and `.html` each: the suite ships no `.txt`): `company-brief`, `value-propositions`, `competitor-analysis`,
  `buyer-persona`, `experiments-plan`, `buying-process`, `missing-pso`, `messaging-playbook`,
  `whats-next`.
- **How:** build it with code execution (the same capability used to write the files). If code
  execution isn't available, list the files instead and tell the user to drop them into one folder
  so the summary's links work.
- **Partial runs:** bundle only the deliverables that were actually produced, and say which are
  missing.

Offer the ZIP as the primary download: "Open `_[company]-strategy-dossier.html` inside the
zip first."

---

## License

Copyright (c) 2026 Kostiantyn Ivanov (Ananas-Agency, ananas-agency.com).

Released under the MIT License — keeping the copyright notice is all that is required, and a credit to the author is warmly appreciated. Full license text: [LICENSE](LICENSE)
