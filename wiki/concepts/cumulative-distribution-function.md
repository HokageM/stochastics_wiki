---
title: Cumulative Distribution Function
type: concept
tags: [distribution-function, cdf, random-variable]
sources: ["stochastics_6_7.pdf p.1-3", "stochastics_6_7.pdf p.10-12", "stochastics_formulas.pdf p.1"]
updated: 2026-10-15
---

# Cumulative Distribution Function (*Verteilungsfunktion*)
> The cumulative distribution function records the probability that a [[random-variable]] is at most a threshold.

## Formal definition

For a real-valued [[random-variable]] $X$, its cumulative distribution function is
$$
F_X:\mathbb{R}\to[0,1],\qquad F_X(y)=\mathbb{P}(X\le y)=\mathbb{P}(X\in(-\infty,y]).
$$
The notes also state that every function $F:\mathbb{R}\to[0,1]$ satisfying the CDF properties below is the CDF of some random variable.

## Properties from the lecture

If $F_X$ is a CDF, then:

1. $F_X$ is nondecreasing: $y_1\le y_2\Rightarrow F_X(y_1)\le F_X(y_2)$.
2. $\lim_{y\to-\infty}F_X(y)=0$ and $\lim_{y\to\infty}F_X(y)=1$.
3. $F_X$ is right-continuous: $\lim_{z\downarrow y}F_X(z)=F_X(y)$.

For the left limit
$$
F_X(y^-)=\lim_{z\uparrow y}F_X(z)=\mathbb{P}(X<y),
$$
the notes derive $\mathbb{P}(X=y)=F_X(y)-F_X(y^-)$.

For $a<b$:
$$
\mathbb{P}(a<X\le b)=F_X(b)-F_X(a),
$$
$$
\mathbb{P}(a\le X\le b)=F_X(b)-F_X(a^-),
$$
$$
\mathbb{P}(a<X<b)=F_X(b^-)-F_X(a),
$$
$$
\mathbb{P}(a\le X<b)=F_X(b^-)-F_X(a^-).
$$

## Intuition

```mermaid
flowchart LR
  X --> Threshold
  Threshold --> Event
  Event --> Prob
  Prob --> Intervals
```

## Procedure: compute probabilities from a CDF

```text
1. Identify whether each interval endpoint is open or closed.
2. Use F(b) for a closed upper endpoint b and F(b-) for an open upper endpoint b.
3. Use F(a) for an open lower endpoint a and F(a-) for a closed lower endpoint a.
4. Subtract lower contribution from upper contribution.
5. For a point probability at y, compute F(y) - F(y-).
```

## Examples from the source

- For [[bernoulli-distribution]] with success probability $p$: $F_X(y)=0$ for $y<0$, $1-p$ for $0\le y<1$, and $1$ for $y\ge1$.
- For [[uniform-distribution]] on $[a,b]$: $F_X(y)=0$ for $y<a$, $(y-a)/(b-a)$ for $a\le y\le b$, and $1$ for $y>b$.
- The triangular density in [[lecture-block-6-7-exercises]] gives a piecewise CDF on $[0,2]$.

## Relation to other ideas

- A [[probability-density]] generates a CDF by integration.
- Jumps correspond to point masses of a [[probability-distribution]].
- Continuous CDFs are used in [[uniform-distribution]], [[exponential-distribution]], [[normal-distribution]], and [[pareto-distribution]].

## Pitfalls

- Right-continuity uses limits from above, not from below.
- For atoms, $F_X(y)$ and $F_X(y^-)$ differ; do not ignore endpoint type.
- In continuous examples the point mass is $0$, but this is not true for all distributions.

## Appears in

[[stochastics-6-7]], [[probability-density]], [[random-variable]], [[lecture-block-6-7-exercises]]

