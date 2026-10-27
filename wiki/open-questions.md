---
title: Open Questions
type: meta
tags: [meta, gaps]
sources: []
updated: 2026-10-15
---

# Open Questions

Unreadable handwriting, contradictions between sources, and gaps to resolve. See [[index]] and [[log]] for coverage context.

| # | Question / issue | Source ref | Status |
|---|---|---|---|
| 1 | > WARNING: Unreadable in source: parts of the formulas for later five-digit counting subcases are scribbled over; verify against the original exercise sheet before relying on those counts. | Stochastics_1_2.pdf p.12 | open |
| 2 | > WARNING: Unreadable in source: stochastics_4_5.pdf p.16-17 gives the dot/dash channel exercise with inconsistent handwriting/arithmetic. The text says dots received as dashes $4\%$ and dashes received as dots $2\%$, but the worked Bayes denominator appears to use a $4\%$ false-dot rate and later totals $0.3725/0.6275$ that do not match the preceding numbers. Verify before using the numerical posterior values. | stochastics_4_5.pdf p.16-17 | open |
| 3 | > WARNING: Unreadable in source: stochastics_6_7.pdf p.20 contains a rectangle diagram and a final expectation expression whose exact target quantity/result are not fully legible. The visible content says $X$ and $Y$ are independent for a uniform point in a rectangle, but the final line is ambiguous. | stochastics_6_7.pdf p.20 | open |
| 4 | RESOLVED: `stochastics_formulas.pdf` ingested and used to verify/rebuild the cheatsheet. | stochastics_formulas.pdf p.1-2; [[stochastics-formulas]] | resolved |
| 5 | RESOLVED: Later-course statistics is covered by `stochastics-1.pdf` p.26-50 and formula-sheet consolidation is complete. | stochastics-1.pdf p.26-50; stochastics_formulas.pdf p.1-2 | resolved |
| 6 | RESOLVED: Geometric convention standardized to the TUHH primary form $\mathbb{P}(X=k)=p^k(1-p)$ on $\mathbb{N}_0$; the $q(1-q)^k$ success-parameter form is documented as an alternative with $q=1-p$. | Stochastics_1_2.pdf p.14; stochastics-1.pdf p.25-26; [[geometric-distribution]] | resolved |
| 7 | > WARNING: Unreadable in source: stochastics-1.pdf p.40 has partially unclear handwriting in the application story; the statistical values $n=457$, observed count $35$, $p_0=0.11$, and error level $0.05$ are readable. | stochastics-1.pdf p.40; [[statistical-inference-exercises]] | open |

| 8 | Geometric formula-summary moments conflict with its own displayed PMF: p.1 writes $\mathbb{P}(X=k)=p^k(1-p)$ on $\mathbb{N}_0$ but gives moments from another convention. Correct moments are $\mathbb{E}[X]=p/(1-p)$ and $\mathrm{Var}(X)=p/(1-p)^2$. | stochastics_formulas.pdf p.1; [[geometric-distribution]] | open - source correction needed |
| 9 | > WARNING: Unreadable in source: p.2 lower-right one-sided binomial-test rejection rule is partly obscured by a punched hole; use the clean version from `stochastics-1.pdf` p.30-34 in [[hypothesis-testing]]. | stochastics_formulas.pdf p.2 | open |
