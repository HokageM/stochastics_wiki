---
title: Wald Identity
type: theorem
tags: [expectation, random-sums, conditional-expectation]
sources: ["stochastics.pdf p.13-14"]
updated: 2026-10-15
---

# Wald Identity

## Statement

Let $N$ be an $\mathbb{N}_0$-valued [[random-variable]] with $\mathbb{E}[N]<\infty$. Let $X_1,X_2,\ldots$ be independent and identically distributed random variables, independent of $N$, with finite expectation. Define
$$
Z=\sum_{k=1}^{N}X_k.
$$
Then
$$
\mathbb{E}[Z]=\mathbb{E}[N]\mathbb{E}[X_1].
$$

## Assumptions

- $N$ is $\mathbb{N}_0$-valued and $\mathbb{E}[N]<\infty$.
- $X_1,X_2,\ldots$ are i.i.d. and have finite expectation.
- The sequence $(X_k)$ is independent of $N$.

## Proof sketch

```mermaid
flowchart TD
  An --> Fixed
  Fixed --> CondMean = n E
  CondMean --> Total
  Total --> Sum
  Sum --> Result
```

## When to use it

Use it when the number of summands is random but independent of the i.i.d. summands.

## Worked example pattern

The source proves the identity generally:
$$
\mathbb{E}[Z\mid A_n]=\mathbb{E}\left[\sum_{k=1}^{n}X_k\right]=n\mathbb{E}[X_1],
$$
then
$$
\mathbb{E}[Z]=\sum_{n=0}^{\infty}\mathbb{P}(A_n)\mathbb{E}[Z\mid A_n]
=\mathbb{E}[X_1]\sum_{n=0}^{\infty}n\mathbb{P}(N=n).
$$

## See also

[[conditional-expectation]], [[expectation]], [[independence]], [[lecture-block-8-9-exercises]]

