---
title: Tail-Sum Formula
type: theorem
tags: [expectation, discrete-random-variable, tail-probabilities]
sources: ["stochastics_6_7.pdf p.21-22"]
updated: 2026-10-15
---

# Tail-Sum Formula

## Statement

If $X$ is an $\mathbb{N}_0$-valued [[random-variable]] with finite [[expectation]], then
$$
\mathbb{E}[X]=\sum_{k=1}^{\infty}\mathbb{P}(X\ge k).
$$

## Assumptions

- $X$ takes values in $\mathbb{N}_0=\{0,1,2,\ldots\}$.
- The expectation is finite in the lecture statement.

## Proof sketch

The handwritten proof rewrites the tail probabilities as a double sum and counts how often each atom appears:
$$
\sum_{k=1}^{\infty}\mathbb{P}(X\ge k)
=\sum_{k=1}^{\infty}\sum_{\ell=k}^{\infty}\mathbb{P}(X=\ell)
=\sum_{\ell=1}^{\infty}\ell\,\mathbb{P}(X=\ell)
=\mathbb{E}[X].
$$

```mermaid
flowchart LR
  Tail --> Double
  Double --> Swap
  Swap --> Count
  Count --> Mean
```

## When to use it

Use it when tail probabilities are easier than individual masses, as in the source's [[geometric-distribution]] exercise.

## Worked example

For the convention $\mathbb{P}(X=k)=p^k(1-p)$ on $\mathbb{N}_0$ with $0<p<1$, the notes show
$$
\mathbb{P}(X\ge a)=p^a.
$$
Therefore
$$
\mathbb{E}[X]=\sum_{a=1}^{\infty}p^a=\frac{p}{1-p}.
$$

## See also

[[expectation]], [[geometric-distribution]], [[lecture-block-6-7-exercises]], [[stochastics-6-7]]

