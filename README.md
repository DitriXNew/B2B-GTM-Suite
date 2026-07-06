# Ananas-Agency — B2B Go-to-Market Suite

A suite of **AI agent skills** that turn an assistant (Claude, or any skill-compatible agent) into a guided B2B sales strategist. Each skill walks you through a structured, step-by-step interview and delivers a concrete sales-strategy asset: value propositions, buyer personas, buying-process maps, validation experiments, and gap analyses.

The skills are written in plain Markdown with YAML frontmatter, so they are version-controllable, diffable, and editable outside any tool. They also ship as importable `.skill` packages.

> **License:** [MIT](LICENSE) — free to use, adapt, and redistribute (including commercially); just keep the copyright notice, and a credit to the author is kindly appreciated. Author: **Kostiantyn Ivanov** (Ananas-Agency, [ananas-agency.com](https://ananas-agency.com)).

---

## ⚡ Quick start

**Two steps — install once, then paste one prompt. Nothing to prepare; the first skill interviews you for everything.**

**1. Install (easiest path — Claude app, no coding).** In [claude.ai](https://claude.ai) or Claude Desktop, open **Settings → Capabilities → Skills** and turn Skills on. Then, for each numbered folder, **Upload skill** its `.skill` package (e.g. `0 Company Brief/company-brief.skill`). Repeat for all eight (0–7).
> *Other ways to install (Claude Code, or copy & paste for any/local model) are in [How to use](#how-to-use).*

**2. Start — open a new chat and paste this:**

> **Run the Ananas-Agency B2B go-to-market sequence with me from the start. Begin with the Company Brief to gather everything about my company, then carry me through every skill in order — value propositions, competitor analysis, buyer persona, experiments, buying process, gap analysis, and messaging — as one continuous session, interviewing me step by step. I have nothing prepared; just ask me what you need.**

That's it. Answer the questions as they come; say **"continue"** if it ever pauses between skills. → Full details in **[How to use](#how-to-use)**.

---

## Contents

- [What's inside](#whats-inside)
  - [Recommended order](#recommended-order)
  - [The Sales Strategy Dossier](#the-sales-strategy-dossier)
- [The PSO (Problem · Solution · Outcome) format](#the-pso-problem--solution--outcome-format)
- [Repository structure](#repository-structure)
  - [File types](#file-types)
- [Which AI to use](#which-ai-to-use)
- [Using with other or local models](#using-with-other-or-local-models)
- [How to use](#how-to-use)
  - [Step 1 — Install](#step-1--install-pick-one-path)
  - [Step 2 — Start the sequence](#step-2--start-the-sequence)
- [Editing & repacking](#editing--repacking) *(scripts — for editors/contributors)*
- [License & attribution](#license--attribution)

---

## What's inside

Eight skills (a one-time Company Brief intake, a value-proposition builder, a competitor analysis, and the rest of the strategy line up through a messaging & positioning capstone), each in its own numbered folder, plus a single compiled handbook.

| # | Skill | What it produces | Needs first |
|---|-------|------------------|-------------|
| 0 | **Company Brief** | A reusable one-page company profile (industry, offering, customers, competition) that the other skills consume instead of re-asking the basics | — (optional, run first) |
| 1 | **Value Proposition** | A ranked list of 20–30+ value propositions in **PSO (Problem · Solution · Outcome)** format, grouped into 3 categories, scored by strength, and given stable IDs (PV-/SV-/AV-) | Skill 0 (optional) |
| 2 | **Competitor Analysis** | Competitor profiles, a differentiation table (your values × competitors), and a win/exposed positioning read — sets the evidence-based `unique` flags and the "unlike [alternative]" for messaging | Skill 1 |
| 3 | **Buyer Persona** | 1–2 B2B buyer personas covering market segment, decision-making roles, problems, challenges, objections, and matched value propositions | Skill 1 |
| 4 | **Persona Experiments** | A one-week plan (5 × 2h) to validate the persona and value propositions with real customers, complete with success criteria | Skills 1 + 3 |
| 5 | **Buying Process** | How a segment buys across 5 non-linear stages, with stage-by-stage outreach recommendations for sales and marketing | Skills 1 + 3 (run 4 first to validate) |
| 6 | **Missing Value Propositions** | A gap analysis that pinpoints where personas have problems your value propositions don't cover, scored on a 3×3 priority matrix | Skills 1 + 3 (run 4 first to validate) |
| 7 | **Messaging & Positioning** | The capstone: a positioning statement, a messaging matrix (role × value × stage), an objection cheat sheet, and send-ready outreach copy (cold email, LinkedIn, one-pager, landing page) | Skills 1 + 3 (5 recommended) |

### Recommended order

```
        +-------------------------+
        | 0. Company Brief         |  <- optional one-time intake (feeds every skill)
        +-----------+-------------+
                    v
        +-------------------------+
        | 1. Value Proposition     |  <- always first (everything depends on it)
        +-----------+-------------+
                    v
        +-------------------------+
        | 2. Competitor Analysis   |  <- optional; needs the value list, refines `unique` flags
        +-----------+-------------+
                    v
        +-------------------------+
        | 3. Buyer Persona         |  <- needs the value list
        +-----------+-------------+
                    v
        +-------------------------+
        | 4. Persona Experiments   |  <- VALIDATE before building further
        +-----------+-------------+
                    |  (feed the validated PSO/persona back into 1 & 3)
           +--------+--------+
           v                 v
   +--------------+   +------------------+
   | 5. Buying     |   | 6. Missing Value  |
   |   Process     |   |   Propositions    |
   +------+-------+   +--------+---------+
          +--------+--------+
                   v
        +-------------------------+
        | 7. Messaging & Positioning|  <- capstone: strategy -> send-ready copy
        +-------------------------+
```

Run **4 (Persona Experiments) before 5 and 6**: validating the persona and value
propositions first means the Buying Process and Gap Analysis build on tested inputs, not
guesses. This is a recommendation, not a hard gate: 5 and 6 still run on hypotheses if you
skip validation (they'll flag that the inputs are untested), and 5 and 6 are interchangeable
with each other. Skill **7 (Messaging & Positioning)** is the capstone: it turns the whole
strategy into a positioning statement, a messaging matrix, an objection cheat sheet, and
send-ready outreach copy.

### The Sales Strategy Dossier

The suite is designed to run as **one continuous session**: you start with the first skill
and flow through the sequence to the end. As you go, the skills maintain a single **Strategy
Dossier**: each skill adds or refreshes its own section, so the document grows with you. After
the final skill, an **executive summary** is generated at the top and the complete dossier is
delivered as the Sales Strategy Dossier (`.md`/`.html`), so you finish the session with a single
consolidated strategy document, not just a scatter of per-skill outputs, delivered as the
**Sales Strategy Dossier** (`_[company]-strategy-dossier.html`): one merged entry document
that opens with the executive summary, then carries every section in full, each linking to its
complete deliverable (the leading `_` sorts it to the top of the folder, so a reader has one
obvious file to open first). Finally, everything is packed
into a single **`[company]-sales-strategy.zip`** so the whole pack travels as one unit and the
summary's links resolve after unzip. Format and section order: [dossier-format.md](dossier-format.md).

---

## The PSO (Problem · Solution · Outcome) format

Everything is built on **PSO (Problem · Solution · Outcome)**, the core unit of the methodology. Every value proposition is a triple:

- **P — Problem / Challenge:** a specific, painful customer problem.
- **S — Solution:** what the company does to solve it (concrete, not vague).
- **O — Outcome:** the measurable business result for the customer (quantified wherever possible).

> *Example:* "Many contractors order the same material from 3 suppliers because no one carries the full range (**P**). We stock 4500 SKUs in one place (**S**), so a contractor places one order instead of three and saves 3–4h a week on logistics (**O**)."

Each value is also assigned a **stable ID** by category — `PV-` (Product value), `SV-` (Service value), `AV-` (Added value) — so the Buyer Persona, Buying Process, and Gap Analysis skills can reference a specific value precisely.

---

## Repository structure

```
.
+-- README.md
+-- LICENSE
+-- B2B Go-to-Market Suite - Handbook by Ananas Agency.md  <- all skills compiled into one document
+-- dossier-format.md                         <- spec for the accreting Strategy Dossier
+-- repack-all-skills.py                      <- rebuilds the .skill archives after editing
+-- build-handbook.py                         <- rebuilds the compiled handbook from the skill sources
|
+-- 0 Company Brief/                          <- one-time intake (unpacked slug: company-brief)
+-- 1 Value Proposition/
|   +-- value-proposition.skill              <- installable package (zip) — import this into an agent
|   +-- value-proposition/                   <- unpacked source (the single source of truth; readable)
|       +-- SKILL.md                         <- the skill definition
|       +-- references/rules-pso.md          <- detailed reference the skill links to
|
+-- 2 Competitor Analysis/                   <- same layout (slug: competitor-analysis)
+-- 3 Buyer Persona/                         <- same layout (slug: buyer-persona)
+-- 4 Persona Experiments/                   <- (slug: persona-experiments)
+-- 5 Buying Process/                        <- (slug: buying-process)
+-- 6 Missing Value Propositions/            <- (slug: missing-value-propositions)
+-- 7 Messaging and Positioning/             <- (slug: messaging-positioning)
```

Each numbered folder holds just the installable **`<slug>.skill`** package and its **unpacked
`<slug>/` source folder** — the single source of truth you read and edit. (There are no separate
flat `-SKILL.md` / `rules-*.md` copies at the folder root; the unpacked `SKILL.md` and
`references/<rules>.md` are the readable source, and the `.skill` is rebuilt from them.)

### File types

| File | What it is |
|------|------------|
| **`<skill>.skill`** | The installable package — a ZIP containing `SKILL.md` plus `references/`. This is what you import into an agent. Rebuilt from the unpacked folder; don't hand-edit. |
| **`<skill>/`** (unpacked source) | The single source of truth — and the readable copy. Contains **`SKILL.md`** (the skill definition: YAML frontmatter plus goal, definitions, step-by-step flow, and critical rules) and **`references/<rules>.md`** (the detailed reference the skill links to: patterns, examples, checklists, output-file templates). Edit here, then rebuild the `.skill` and handbook. |
| **`B2B Go-to-Market Suite - Handbook by Ananas Agency.md`** | A single human-readable handbook that brings all the skills and their references together. Read this to understand the whole system without installing anything. |

---

## Which AI to use

These are **Agent Skills for Claude**, the AI assistant by Anthropic. Skills are a native Claude feature, so Claude is the recommended, and best-supported, way to run them. You can use any of the following:

- **Claude apps — [claude.ai](https://claude.ai) (web) or the Claude Desktop app.** The easiest option, with no coding required. The Skills feature is available on paid plans (Pro, Max, Team, Enterprise).
- **Claude Code** — Anthropic's command-line/IDE tool, for developers who want the skills inside their projects.
- **Claude API / Agent SDK** — for building the skills into your own application.

For the best results, run them on a top-tier model: **Claude Opus** (highest quality) or **Claude Sonnet** (faster, still excellent). The skills also work with other skill-compatible agents (e.g. Codex, OpenCode), but Claude is the reference platform.

> **New to "skills"?** A skill is simply a set of expert instructions you hand the AI so it knows exactly how to run a task. There's nothing to program: you either install the skills once (Path A or B below) or just paste the instructions into a chat (Path C). From there, you talk to the AI in plain language and it does the rest.

---

## Using with other or local models

The skills are plain-text instructions, so they also run on **non-Claude models, including local, self-hosted ones**. Setups known to work well include:

- **Local runners:** Ollama, LM Studio, llama.cpp, Jan, GPT4All, Open WebUI
- **Self-hosted serving:** vLLM or TGI (anything exposing an OpenAI-compatible API)
- **Open models:** Llama 3.x, Qwen2.5, Mistral, DeepSeek, Gemma, and similar

**How:** use **Path C (copy & paste)** below. Paste one skill's `SKILL.md` into the chat and let the model interview you. The one-click `.skill` packages rely on Claude's Agent Skills system and generally **won't be auto-detected** by a local chat app.

> **Expect different (and sometimes lower-quality) output on other or local models.**
> These skills were written and tuned for Claude. On other models, and **especially smaller local ones**, results can vary noticeably. Common differences:
>
> - The model **skips or reorders the step-by-step flow**, or stops asking questions and makes up the answers itself.
> - **Shallower output** — generic value propositions or personas, weak or missing numeric "Outcomes," or the PSO (Problem · Solution · Outcome) structure not followed.
> - **Dependency rules ignored** (e.g. it starts a buyer persona without first having a value list).
> - **No files saved** — a plain chat model just prints the `.md`/`.html` content, so you copy it out manually.
> - **No URL analysis** — a model without browsing can't open links, so paste the relevant text in yourself.
>
> **Always review the output before you use it.** For the most reliable results, use a capable model with a large context window (roughly **30B+**, or a strong 70B-class / frontier model), and feed it **one skill at a time** (its `SKILL.md` plus the single `rules-*.md` it links to) rather than the whole handbook at once.

---

## How to use

It's two steps: **install once**, then **paste the start prompt**. You don't prepare anything in advance — the first skill interviews you for everything it needs.

### Step 1 — Install (pick one path)

**Path A — Claude app (recommended, no coding).**
1. In Claude (web or desktop), open **Settings → Capabilities** and turn on **Skills** (and code execution if prompted). *Available on paid plans.*
2. For each numbered folder, grab its `.skill` package (e.g. `0 Company Brief/company-brief.skill`). **A `.skill` file is a ZIP**: if the uploader only accepts `.zip`, just rename it (e.g. `company-brief.zip`).
3. Click **Upload skill** (or "Add skill") and select the file. **Repeat for all eight skills (0–7)** so the whole sequence is available.

**Path B — Claude Code (for developers).**
1. Install Claude Code (`npm install -g @anthropic-ai/claude-code`) and open your project.
2. Copy each skill's **unpacked folder** into your skills directory — for all projects `~/.claude/skills/`, or for one project `<your-project>/.claude/skills/`. Each folder already contains `SKILL.md` and `references/`, so copy it in as-is (e.g. `~/.claude/skills/company-brief/`). Do this for all eight.
3. Run `claude` in your project — it auto-discovers the skills on startup.

**Path C — Copy & paste (any plan, zero setup).**
No Skills feature required. Open one skill's source file (e.g. [0 Company Brief/company-brief/SKILL.md](0%20Company%20Brief/company-brief/SKILL.md)), copy **everything from the first `#` heading down** (ignore the small `---` metadata block at the very top), paste it into a new chat, and send *"Follow these instructions and guide me through it step by step."* Work through the skills in order (0 → 7), pasting the next one when the current is done.

### Step 2 — Start the sequence

Open a new chat and paste this:

> **Run the Ananas-Agency B2B go-to-market sequence with me from the start. Begin with the Company Brief to gather everything about my company, then carry me through every skill in order — value propositions, competitor analysis, buyer persona, experiments, buying process, gap analysis, and messaging — as one continuous session, interviewing me step by step. I have nothing prepared; just ask me what you need.**

**That's the whole start — no company name, website, or details to fill in first.** The first skill, **0. Company Brief**, collects all of that by interviewing you, and everything you tell it flows into every skill that follows. Just answer the questions as they come. If Claude ever pauses between skills, say **"continue"** to move to the next one.

### What happens as it runs

- It **interviews you** in small steps (usually 2–3 questions at a time), so there is no need to know the framework in advance.
- It runs the skills in **dependency order**, reusing what you already told it instead of re-asking — the Company Brief facts carry through the whole sequence.
- It delivers **two files** per skill: a `.md` (full documentation) and a styled, self-contained `.html` (share-ready: opens in any browser and prints cleanly to PDF). The `.html` files cross-link to each other, explain short terms on hover, and each ends with a **Next** button so the whole pack reads like one small site.
- At the end of the run, the final skill bundles every deliverable into one **`[company]-sales-strategy.zip`**, with the top-sorted **`_[company]-strategy-dossier.html`** to open first, so all the cross-links between files work.

### Just want to read the method?

Open [B2B Go-to-Market Suite - Handbook by Ananas Agency.md](B2B%20Go-to-Market%20Suite%20-%20Handbook%20by%20Ananas%20Agency.md): every skill and reference compiled into one document. No AI or installation required.

---

## Editing & repacking

*This section is only for people **editing** the skills. If you just want to use them, you can ignore the two scripts below.*

The repo ships two small helper scripts at the root:

- **`repack-all-skills.py`** — rezips each unpacked `<slug>/` folder into its installable `<slug>.skill` package (with the correct internal paths).
- **`build-handbook.py`** — regenerates the compiled `B2B Go-to-Market Suite - Handbook by Ananas Agency.md` from the skill sources.

The unpacked `<slug>/` folders are the single source of truth; the `.skill` archives and the compiled handbook are built from them by those scripts. The agent reads the `.skill`, so **after editing the source you must rebuild the archives** (and the handbook):

1. Edit the source files inside each `<skill>/` folder (`SKILL.md` and `references/<rules>.md`).
2. From the repository root, run:

   ```bash
   python repack-all-skills.py
   ```

   This rezips all `<skill>/` folders into their `.skill` packages (with the correct internal paths).
3. If you changed any skill content, also rebuild the compiled handbook so it stays in sync:

   ```bash
   python build-handbook.py
   ```

---

## License & attribution

This work is released under the **MIT License** — you may use, adapt, and redistribute it freely, including commercially. The only requirement is to keep the copyright notice; beyond that, a credit to the author is warmly appreciated (a courtesy, not a condition).

**A credit like this is appreciated:**

> "Ananas-Agency B2B Go-to-Market Suite" by **Kostiantyn Ivanov** (Ananas-Agency, ananas-agency.com).

Full terms: [LICENSE](LICENSE)
