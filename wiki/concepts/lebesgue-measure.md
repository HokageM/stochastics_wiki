---
title: Lebesgue Measure
type: concept
tags: [measure-theory, continuous-probability, density]
sources: ["stochastics_4_5.pdf p.10-12", "stochastics_6_7.pdf p.8-17"]
updated: 2026-10-15
---

# Lebesgue Measure
> Lebesgue measure is the length, area, or volume reference measure used to define continuous probabilities and [[probability-density|densities]].

## Formal definition
For boxes in $\mathbb{R}^d$, the lecture notes introduce
$$
\lambda_d\bigl((a_1,b_1]	imes\cdots	imes(a_d,b_d]\bigr)=\prod_{i=1}^{d}(b_i-a_i),
$$
and extend this consistently on the [[borel-sigma-algebra]]. The symbol $\lambda_d$ denotes $d$-dimensional Lebesgue measure.

## Intuition
```mermaid
flowchart LR
  Interval --> Box
  Box --> Measure
  Measure --> Density
```

## Relation to other ideas
- A [[probability-density]] $f$ assigns probabilities by integrating $f$ with respect to Lebesgue measure.
- [[uniform-distribution]] and [[exponential-distribution]] are continuous laws described by densities.
- [[probability-space]] separates the event system $\mathcal{F}$ from the probability measure $\mathbb{P}$.

## Pitfalls
- Lebesgue measure itself is not usually a probability measure on all of $\mathbb{R}$ because $\lambda_1(\mathbb{R})=\infty$.
- A density must integrate to $1$ before it defines a probability distribution.

## Appears in
- [[stochastics-4-5]] p.10-p.12
- [[stochastics-6-7]] p.8-p.17

