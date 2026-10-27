---
title: Central Limit Theorem
type: theorem
tags: [limit-theorems, normal-distribution, iid]
sources: ["stochastics.pdf p.17", "stochastics.pdf p.24", "stochastics-1.pdf p.46", "stochastics_formulas.pdf p.1"]
updated: 2026-10-15
---

# Central Limit Theorem

## Statement

Let $(X_i)_{i\in\mathbb{N}}$ be i.i.d. [[random-variable|random variables]] with
$$
\mathbb{E}[X_1^2]<\infty,\qquad \mathrm{Var}(X_1)>0,
$$
and define $S_n=\sum_{i=1}^nX_i$. If $N\sim\mathcal{N}(0,1)$ and $\Phi$ is the standard [[normal-distribution]] function, then for all $t\in\mathbb{R}$,
$$
\lim_{n\to\infty}\mathbb{P}\left(
\frac{S_n-n\mathbb{E}[X_1]}{\sqrt{\mathrm{Var}(X_1)}\sqrt{n}}\le t
\right)=\Phi(t).
$$
Equivalently,
$$
\frac{S_n-n\mathbb{E}[X_1]}{\sqrt{\mathrm{Var}(X_1)}\sqrt{n}}
\xrightarrow{d}N.
$$

## Assumptions

- The variables are independent and identically distributed.
- $\mathbb{E}[X_1^2]<\infty$.
- $\mathrm{Var}(X_1)>0$.

## Proof sketch

The source states and uses the theorem; it does not give a full proof.

```mermaid
flowchart LR
  Sum --> Center
  Center --> Scale
  Scale --> Normal
```

## When to use it

Use the CLT for large-$n$ approximations of sums of many i.i.d. variables after centering and scaling. The source applies it to [[erlang-distribution|Erlang]] sums of exponentials.

## Worked example

If $X_i\sim\mathrm{Exp}(\lambda)$ are i.i.d., then $\mathbb{E}[X_i]=1/\lambda$ and $\mathrm{Var}(X_i)=1/\lambda^2$. Since $Y_n=\sum_{i=1}^nX_i\sim\mathrm{Erl}(\lambda,n)$,
$$
\frac{Y_n-n/\lambda}{\sqrt n/\lambda}\xrightarrow{d}\mathcal{N}(0,1).
$$

## Poisson-series limit from stochastics-1.pdf p.46

The source applies the theorem to $S_n\sim\mathrm{Poisson}(n)$, where $\mathbb{E}[S_n]=n$ and $\mathrm{Var}(S_n)=n$, to obtain
$$
\lim_{n\to\infty}e^{-n}\sum_{k=0}^n\frac{n^k}{k!}
=\lim_{n\to\infty}\mathbb{P}(S_n\le n)
=\Phi(0)=\frac12.
$$

## See also

[[convergence-of-random-variables]], [[weak-law-large-numbers]], [[de-moivre-laplace-theorem]], [[normal-approximation]], [[erlang-distribution]]

