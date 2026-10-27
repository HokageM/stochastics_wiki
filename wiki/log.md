---
title: Log
type: meta
tags: [meta, log]
sources: []
updated: 2026-10-15
---

# Log

Append-only. Newest entries at the bottom.
`grep "^## \[" wiki/log.md | tail -5`

## [2026-10-15] refactor | wiki scaffolding created
- Created: CLAUDE.md schema, wiki/ directory structure
- Raw sources present but not yet ingested: stochastics-1.pdf, stochastics.pdf,
  Stochastics_1_2.pdf, stochastics_4_5.pdf, stochastics_6_7.pdf, stochastics_formulas.pdf

## [2026-10-15] ingest | Stochastics_1_2.pdf p.1-22
- Read: pages 1-22 (lecture blocks 1-2)
- Created: sources/stochastics-1-2.md, concepts/discrete-probability-space.md, concepts/laplace-probability-space.md, concepts/probability-distribution.md, concepts/product-probability-space.md, theorems/probability-rules.md, theorems/inclusion-exclusion-principle.md, methods/combinatorial-counting.md, methods/simulation-by-random-sampling.md, distributions/dirac-distribution.md, distributions/geometric-distribution.md, distributions/binomial-distribution.md, distributions/poisson-distribution.md, exercises/lecture-block-1-2-exercises.md
- Updated: index.md, overview.md, open-questions.md, cheatsheet.md
- Open questions: 1 (see [[open-questions]])


## [2026-10-15] ingest | stochastics_4_5.pdf p.1-20
- Read: pages 1-20 (lecture blocks 4-5)
- Created: sources/stochastics-4-5.md, concepts/conditional-probability.md, concepts/independence.md, concepts/sigma-algebra.md, concepts/probability-space.md, concepts/random-variable.md, theorems/law-of-total-probability.md, theorems/bayes-formula.md, methods/diagnostic-testing-bayes.md, distributions/hypergeometric-distribution.md, exercises/lecture-block-4-5-exercises.md
- Updated: concepts/probability-distribution.md, concepts/product-probability-space.md, distributions/binomial-distribution.md, distributions/poisson-distribution.md, index.md, overview.md, open-questions.md
- Open questions: 2 total, 1 newly added (see [[open-questions]])

## [2026-10-15] ingest | stochastics_6_7.pdf p.1-34
- Read: pages 1-34 (lecture blocks 6-7)
- Created: sources/stochastics-6-7.md, concepts/cumulative-distribution-function.md, concepts/probability-density.md, concepts/expectation.md, concepts/variance-covariance-correlation.md, theorems/tail-sum-formula.md, distributions/bernoulli-distribution.md, distributions/uniform-distribution.md, distributions/discrete-uniform-distribution.md, distributions/exponential-distribution.md, distributions/normal-distribution.md, distributions/pareto-distribution.md, exercises/lecture-block-6-7-exercises.md
- Updated: concepts/random-variable.md, concepts/probability-distribution.md, concepts/independence.md, distributions/geometric-distribution.md, distributions/binomial-distribution.md, distributions/poisson-distribution.md, index.md, overview.md, open-questions.md
- Open questions: 3 total, 1 newly added (see [[open-questions]])

## [2026-10-15] ingest | stochastics.pdf p.1-28
- Read: pages 1-28 (later KVB notes and exercises 8-9)
- Created: sources/stochastics.md, concepts/conditional-expectation.md, concepts/convolution-of-distributions.md, concepts/moment-generating-function.md, concepts/convergence-of-random-variables.md, theorems/markov-inequality.md, theorems/chebyshev-inequality.md, theorems/weak-law-large-numbers.md, theorems/central-limit-theorem.md, theorems/de-moivre-laplace-theorem.md, theorems/wald-identity.md, distributions/erlang-distribution.md, methods/normal-approximation.md, exercises/lecture-block-8-9-exercises.md
- Updated: concepts/expectation.md, concepts/variance-covariance-correlation.md, distributions/bernoulli-distribution.md, distributions/binomial-distribution.md, distributions/poisson-distribution.md, distributions/exponential-distribution.md, distributions/normal-distribution.md, distributions/uniform-distribution.md, index.md, overview.md, cheatsheet.md
- Open questions: 3 total, 0 newly added (see [[open-questions]])

## [2026-10-15] lint | full wiki health check
- Checked: all `wiki/**/*.md` links, filenames, YAML frontmatter, index coverage, orphan inbound links, notation conventions, Mermaid/pseudocode presence, English-only leakage, overview/cheatsheet accuracy, and repeated mentioned concepts without pages.
- Fixed: 0 broken links; 0 orphan pages; normalized probability/expectation/variance notation; added missing meta frontmatter fields; added pages for Borel sigma-algebra, Lebesgue measure, and joint/marginal distributions; repaired Mermaid blocks for parser-safe syntax; updated index, overview, cheatsheet, and open questions.
- Remaining issues: source ambiguities already tracked in `open-questions.md`; `stochastics-1.pdf` and `stochastics_formulas.pdf` remain not ingested.

## [2026-10-15] ingest | stochastics-1.pdf p.1-25
- Read: pages 1-25 (KVB notes: stochastic processes, Markov chains, Poisson process, Brownian motion, and start of statistics/estimation)
- Created: sources/stochastics-1.md, concepts/stochastic-process.md, concepts/markov-chain.md, concepts/poisson-process.md, concepts/brownian-motion.md, methods/point-estimation.md, methods/maximum-likelihood-estimation.md, exercises/stochastic-processes-and-statistics-exercises.md
- Updated: index.md, overview.md, open-questions.md, theorems/chebyshev-inequality.md, theorems/weak-law-large-numbers.md, concepts/variance-covariance-correlation.md, concepts/convergence-of-random-variables.md, concepts/probability-space.md, distributions/normal-distribution.md, distributions/uniform-distribution.md, distributions/geometric-distribution.md
- Open questions: 6 total, 1 newly added (geometric parameter convention; see [[open-questions]])


## [2026-10-15] ingest | stochastics-1.pdf p.26-50
- Read: pages 26-50 (statistics: geometric MLE continuation, mark-recapture, confidence intervals, quantiles, hypothesis tests, and review exercises)
- Created: concepts/quantile.md, methods/confidence-intervals.md, methods/hypothesis-testing.md, methods/mark-recapture-estimation.md, exercises/statistical-inference-exercises.md
- Updated: sources/stochastics-1.md, methods/maximum-likelihood-estimation.md, methods/point-estimation.md, distributions/geometric-distribution.md, distributions/binomial-distribution.md, distributions/normal-distribution.md, distributions/exponential-distribution.md, distributions/pareto-distribution.md, theorems/weak-law-large-numbers.md, theorems/central-limit-theorem.md, concepts/markov-chain.md, concepts/poisson-process.md, index.md, overview.md, cheatsheet.md, open-questions.md
- Open questions: 7 total, 1 newly added (p.40 story handwriting; see [[open-questions]])

## [2026-10-15] lint | post stochastics-1 health check
- Checked: broken links across `wiki\**\*.md`, duplicate concepts across the split ingest boundary, orphan pages, schema/frontmatter, method pseudocode, Mermaid labels, geometric-distribution convention, index completeness, overview, cheatsheet, and `sources/stochastics-1.md` coherence.
- Fixed: standardized the geometric distribution to the TUHH primary $\mathbb{P}(X=k)=p^k(1-p)$ convention, documented the alternative convention, resolved the open question, rewrote `sources/stochastics-1.md`, repaired Mermaid labels, refreshed overview/cheatsheet wording, and added stochastic-process formulas to the cheatsheet.
- Remaining: no broken links or orphan pages found; no duplicate pages required merging; open source gaps remain for unreadable source fragments and the un-ingested `stochastics_formulas.pdf`.


## [2026-10-15] ingest | stochastics_formulas.pdf p.1-2
- Read: pages 1-2 (2-page handwritten formula summary), viewed whole pages and enlarged region crops column-by-column.
- Created: sources/stochastics-formulas.md
- Updated: cheatsheet.md, index.md, overview.md, open-questions.md, geometric-distribution.md, point-estimation.md, stochastic-process.md, hypothesis-testing.md, and corroborating source lists across probability, distribution, limit-theorem, process, and statistics pages.
- Open questions: 2 newly added from this source (geometric formula-sheet moment error; obscured binomial-test threshold detail).

## [2026-10-15] lint | encoding and LaTeX escaping repair
- Checked: all 74 pages for UTF-8 mojibake and double-escaped LaTeX
- Fixed: mojibake in 17 pages (em dashes rendered as `â€”`); doubled backslashes in cheatsheet.md (87 occurrences) that would have broken math rendering
- Remaining: none; 1269 wiki-links resolve, 0 broken
