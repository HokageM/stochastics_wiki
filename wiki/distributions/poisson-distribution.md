---
title: Poisson Distribution
type: distribution
tags: [poisson-distribution, discrete-distribution, exponential-series]
sources: ["Stochastics_1_2.pdf p.15", "stochastics_4_5.pdf p.14", "stochastics_6_7.pdf p.8", "stochastics_6_7.pdf p.13", "stochastics_6_7.pdf p.24", "stochastics_6_7.pdf p.26", "stochastics_6_7.pdf p.31", "stochastics.pdf p.2", "p.4-5", "stochastics_formulas.pdf p.1"]
updated: 2026-10-15
---

# Poisson Distribution

| Item | Value from source |
|---|---|
| Support | $\mathbb{N}_0$ |
| PMF/PDF | $\mathbb{P}(X=k)=\frac{\lambda^k}{k!}e^{-\lambda}$ |
| CDF | Not given in this source |
| $\mathbb{E}[X]$ | $\lambda$ |
| $\mathrm{Var}(X)$ | $\lambda$ |
| MGF | $e^{\lambda(e^t-1)}$ |
| Parameters | $\lambda\in(0,\infty)$ |

## Story / when it arises

The notes introduce the Poisson distribution as a point-mass family on $\mathbb{N}_0$. Its total mass is checked by the exponential series.

Block 6-7 derives $\mathbb{E}[X]=\lambda$, $\mathbb{E}[X(X-1)]=\lambda^2$, and therefore $\mathrm{Var}(X)=\lambda$. It also shows that if a Poisson count is independently thinned with probability $p$, the resulting count is $\mathrm{Poisson}(\lambda p)$.

## Relationships

```mermaid
graph TD
  P --> ES
  P --> Mean
  P --> Var
  P --> Factorial=lambda^2
  P --> Thin
  Thin --> P2
```

## Typical exercise patterns

- Use the exponential series to show total mass $1$.
- Shift summation indices to compute mean and factorial moments.
- Use $\mathbb{E}[X^2]=\mathbb{E}[X(X-1)]+\mathbb{E}[X]$ for variance.
- For $\mathbb{E}[\lambda^{-X}]$, cancel the powers of $\lambda$ and use $\sum 1/k!=e$.

## Additional results from stochastics.pdf

The later source proves that independent Poisson variables add:
$$
X\sim\mathrm{Poi}(\lambda),\quad Y\sim\mathrm{Poi}(\mu),\quad X\perp Y
\quad\Rightarrow\quad X+Y\sim\mathrm{Poi}(\lambda+\mu).
$$
It also records the MGF $M_X(t)=e^{\lambda(e^t-1)}$.

## See also

[[probability-distribution]], [[random-variable]], [[expectation]], [[variance-covariance-correlation]], [[binomial-distribution]], [[lecture-block-6-7-exercises]], [[stochastics]]

