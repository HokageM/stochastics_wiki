---
title: Inclusion-Exclusion Principle
type: theorem
tags: [inclusion-exclusion, counting, unions]
sources: ["Stochastics_1_2.pdf p.3", "Stochastics_1_2.pdf p.10", "Stochastics_1_2.pdf p.18-20", "stochastics_formulas.pdf p.1"]
updated: 2026-10-15
---

# Inclusion-Exclusion Principle

## Statement

For events $A_1,
\ldots,A_n\subseteq\Omega$, $n\ge 2$,
$$\mathbb{P}\left(\bigcup_{i=1}^{n}A_i\right)
=
\sum_{k=1}^{n}(-1)^{k-1}
\sum_{1\le i_1<\cdots<i_k\le n}
\mathbb{P}(A_{i_1}\cap\cdots\cap A_{i_k}).
$$

For three events:
$$\mathbb{P}(A\cup B\cup C)=\mathbb{P}(A)+\mathbb{P}(B)+\mathbb{P}(C)
-\mathbb{P}(A\cap B)-\mathbb{P}(A\cap C)-\mathbb{P}(B\cap C)
+\mathbb{P}(A\cap B\cap C).
$$

## Assumptions

- $A_i$ are events in the same [[discrete-probability-space]].
- Intersections must be counted with the same probability model.

## Proof sketch

```mermaid
flowchart LR
  Add --> Over
  Over --> Sub
  Sub --> Under
  Under --> AddBack
  AddBack --> Continue
```

## When to use it

Use it for "at least one of these events occurs," divisibility by several numbers, occupancy problems, or complements of "all boxes/stops are nonempty."

## Worked example

For a number chosen uniformly from $\{1,\ldots,1{,}000{,}000\}$, the notes define events
$A_1=\{a:2\mid a\}$, $A_2=\{a:3\mid a\}$, and $A_{19}=\{a:19\mid a\}$, then use inclusion-exclusion to compute the probability that the number is divisible by $2$, $3$, or $19$.

For the bus exercise with seven passengers and four stops, the notes compute the probability that every stop receives at least one passenger as approximately $0.513$ by applying inclusion-exclusion to the complements of "stop $i$ is nonempty."

## See also

[[probability-rules]], [[combinatorial-counting]], [[lecture-block-1-2-exercises]]

