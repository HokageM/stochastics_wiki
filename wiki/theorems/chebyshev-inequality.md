---
title: Chebyshev Inequality
type: theorem
tags: [inequality, variance, convergence]
sources: ["stochastics.pdf p.15", "stochastics.pdf p.26", "stochastics-1.pdf p.6-7", "stochastics_formulas.pdf p.1", "stochastics_formulas.pdf p.2"]
updated: 2026-10-15
---

# Chebyshev Inequality

## Statement

For a [[random-variable]] $X$ with $\mathbb{E}[X^2]<\infty$ and every $u>0$,
$$
\mathbb{P}(|X-\mathbb{E}[X]|\ge u)\le\frac{\mathrm{Var}(X)}{u^2}.
$$

## Assumptions

- $X$ has finite second moment.
- $u>0$.

## Proof sketch

Chebyshev is the source's variance-centered special case of [[markov-inequality]], using $h(x)=x^2$ on $X-\mathbb{E}[X]$.

```mermaid
flowchart LR
  Center --> Square
  Square --> Markov
  Markov --> Bound
```

## When to use it

Use Chebyshev when an exercise gives or permits computing a mean and variance but not the full distribution, or when proving [[weak-law-large-numbers]].

## Worked example

For $X\sim\mathrm{Bin}(900,1/6)$,
$$
\mathbb{E}[X]=150,\qquad \mathrm{Var}(X)=900\cdot\frac16\cdot\frac56=125.
$$
Thus
$$
\mathbb{P}(X\ge200)
\le \mathbb{P}(|X-150|\ge50)
\le\frac{125}{50^2}=0.05.
$$

## Additional standard-deviation bounds from stochastics-1.pdf

With $\mu=\mathbb{E}[X]$ and $\sigma=\sqrt{\mathrm{Var}(X)}$, p.6 rewrites Chebyshev as
$$
\mathbb{P}(|X-\mu|\ge t\sigma)\le\frac1{t^2}.
$$
The worked bounds are $1$ for $t=1$, $1/2$ for $t=\sqrt2$, $1/4$ for $t=2$, and $1/25$ for $t=5$. Therefore Chebyshev alone guarantees at least $0.96$ probability in $(\mu-5\sigma,\mu+5\sigma)$.

For comparison, p.7 notes that if $X\sim\mathcal{N}(\mu,\sigma^2)$, then
$$
\mathbb{P}(\mu-3\sigma<X<\mu+3\sigma)=\Phi(3)-\Phi(-3)\approx0.9974.
$$

## See also

[[markov-inequality]], [[variance-covariance-correlation]], [[weak-law-large-numbers]], [[lecture-block-8-9-exercises]]

