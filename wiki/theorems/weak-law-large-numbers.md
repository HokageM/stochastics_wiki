---
title: Weak Law of Large Numbers
type: theorem
tags: [limit-theorems, convergence, iid]
sources: ["stochastics.pdf p.15", "stochastics-1.pdf p.17", "p.21", "stochastics-1.pdf p.46", "stochastics_formulas.pdf p.1", "stochastics_formulas.pdf p.2"]
updated: 2026-10-15
---

# Weak Law of Large Numbers

## Statement

Let $(X_i)_{i\in\mathbb{N}}$ be i.i.d. [[random-variable|random variables]] with $\mathbb{E}[X_1^2]<\infty$. Define $S_n=\sum_{i=1}^n X_i$. Then
$$
\frac{S_n}{n}\xrightarrow{P}\mathbb{E}[X_1]
\qquad\text{as }n\to\infty.
$$
The source also records
$$
\mathbb{P}\left(\left|\frac{S_n}{n}-\mathbb{E}[X_1]\right|\ge\varepsilon\right)
\le\frac{\mathrm{Var}(X_1)}{\varepsilon^2 n}.
$$

## Assumptions

- The variables are independent and identically distributed.
- $\mathbb{E}[X_1^2]<\infty$.
- $S_n=\sum_{i=1}^nX_i$.

## Proof sketch

```mermaid
flowchart TD
  IID --> Mean = E
  IID --> Var
  Var --> Cheb
  Cheb --> Bound
  Bound --> Zero
  Zero --> Convergence
```

## When to use it

Use it to justify that empirical averages or relative frequencies stabilize near their mean/probability.

## Worked example

For i.i.d. [[bernoulli-distribution|Bernoulli]]$(p)$ variables, the average is the relative frequency of an event $A$ with $\mathbb{P}(A)=p$, and
$$
\frac1n\sum_{i=1}^nX_i\xrightarrow{P}p.
$$

## Estimation use from stochastics-1.pdf

In the statistics notes, the [[weak-law-large-numbers]] is used to prove consistency of estimators. If $\mathbb{E}_m[X_1]=m$ and
$$
\hat m_n=\frac{1}{n-1}\sum_{i=1}^nX_i,
$$
then
$$
\hat m_n=\frac{n}{n-1}\left(\frac1n\sum_{i=1}^nX_i\right)\xrightarrow{P}m,
$$
even though $\hat m_n$ is biased for finite $n$.

## Restatement from stochastics-1.pdf p.46

The second half of [[stochastics-1]] repeats the weak law in the form: if $(X_i)$ are i.i.d., $\mathbb{E}[X_i^2]<\infty$, and $S_n=\sum_{i=1}^nX_i$, then
$$
\frac{S_n}{n}\xrightarrow{P}\mathbb{E}[X_1].
$$

## See also

[[convergence-of-random-variables]], [[chebyshev-inequality]], [[central-limit-theorem]], [[bernoulli-distribution]]

