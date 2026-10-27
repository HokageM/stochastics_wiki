---
title: Variance, Covariance, and Correlation
type: concept
tags: [variance, covariance, correlation, second-moment]
sources: ["stochastics_6_7.pdf p.24-34", "stochastics.pdf p.15", "p.25-26", "stochastics-1.pdf p.4", "p.8-9", "p.17", "stochastics_formulas.pdf p.1"]
updated: 2026-10-15
---

# Variance, Covariance, and Correlation
> Variance measures spread, covariance measures joint linear movement, and correlation normalizes covariance to a scale-free coefficient.

## Formal definitions

For a random variable $X$ with $\mathbb{E}[X^2]<\infty$,
$$
\mathrm{Var}(X)=\mathbb{E}\left[(X-\mathbb{E}[X])^2\right].
$$
The lecture gives
$$
\mathrm{Var}(X)=\mathbb{E}[X^2]-\mathbb{E}[X]^2.
$$
The standard deviation is $\sqrt{\mathrm{Var}(X)}$.

For $X,Y$ with finite second moments,
$$
\mathrm{cov}(X,Y)=\mathbb{E}\left[(X-\mathbb{E}[X])(Y-\mathbb{E}[Y])\right]
=\mathbb{E}[XY]-\mathbb{E}[X]\mathbb{E}[Y].
$$
If $\mathrm{Var}(X)>0$ and $\mathrm{Var}(Y)>0$, the correlation coefficient is
$$
\rho_{X,Y}=\frac{\mathrm{cov}(X,Y)}{\sqrt{\mathrm{Var}(X)}\sqrt{\mathrm{Var}(Y)}}.
$$
The notes call $X$ and $Y$ uncorrelated if $\rho_{X,Y}=0$.

## Properties from the lecture

- If $X$ and $Y$ are [[independence|independent]], then $\mathrm{cov}(X,Y)=0$.
- $\mathrm{Var}(aX)=a^2\mathrm{Var}(X)$ and $\mathrm{Var}(X+c)=\mathrm{Var}(X)$.
- For $X_1,\ldots,X_n$ with finite second moments,
  $$
  \mathrm{Var}\left(\sum_{i=1}^n X_i\right)=\sum_{i=1}^n\mathrm{Var}(X_i)+2\sum_{1\le i<j\le n}\mathrm{cov}(X_i,X_j).
  $$

```mermaid
flowchart LR
  EX --> EX2
  EX2 --> Var-E^2
  Var --> SD
  EXY --> Cov-EE
  Cov --> Rho
```

## Procedure: variance and covariance calculations

```text
1. Compute all needed means: \mathbb{E}[X], \mathbb{E}[Y].
2. Compute second moments: \mathbb{E}[X^2] and \mathbb{E}[Y^2].
3. Use \mathrm{Var}(X) = \mathbb{E}[X^2] - \mathbb{E}[X]^2.
4. For covariance, compute \mathbb{E}[XY] or use a given correlation to recover \mathrm{Cov}(X,Y).
5. For linear combinations, expand with bilinearity of covariance.
6. For sums of independent variables, drop covariance terms because they are zero.
```

## Key examples from the source

| Case | Result |
|---|---|
| Fair die $X\in\{1,\ldots,6\}$ | $\mathrm{Var}(X)=35/12$ |
| [[poisson-distribution]]$(\lambda)$ | $\mathrm{Var}(X)=\lambda$ |
| [[uniform-distribution]]$([a,b])$ | $\mathrm{Var}(X)=(b-a)^2/12$ |
| [[binomial-distribution]]$(n,p)$ | $\mathrm{Var}(X)=np(1-p)$ |
| Triangular density on $[0,2]$ from [[lecture-block-6-7-exercises]] | $\mathrm{Var}(X)=1/6$ |
| [[pareto-distribution]]$(\alpha)$ | finite variance for $\alpha>2$ |

## Inequality use from stochastics.pdf

The later source uses second moments in [[chebyshev-inequality]]:
$$
\mathbb{P}(|X-\mathbb{E}[X]|\ge u)\le \frac{\mathrm{Var}(X)}{u^2}.
$$
For $X\sim\mathrm{Bin}(900,1/6)$, it computes $\mathrm{Var}(X)=125$ and obtains the bound $\mathbb{P}(X\ge200)\le0.05$.

## Covariance functions for stochastic processes

For a [[stochastic-process]] $(X_t)_{t\in T}$ with finite second moments, stochastics-1.pdf defines the mean and covariance functions
$$
\mu(t)=\mathbb{E}[X_t],
\qquad
\rho(s,t)=\mathrm{cov}(X_s,X_t).
$$
In the moving-average exercise with i.i.d. $(Z_t)_{t\in\mathbb{Z}}$, $\mathbb{E}[Z_t]=\mu$, $\mathrm{Var}(Z_t)=\sigma^2$, and
$$
X_t=\frac{Z_{t-1}+Z_t+Z_{t+1}}{3},
$$
the covariance is nonzero only when the underlying triples overlap:
$$
\rho(s,t)=
\begin{cases}
\frac13\sigma^2,&s=t,\\
\frac29\sigma^2,&s\in\{t-1,t+1\},\\
\frac19\sigma^2,&s\in\{t-2,t+2\},\\
0,&\text{otherwise.}
\end{cases}
$$

## Relation to other ideas

- Variance builds on [[expectation]].
- Zero covariance follows from [[independence]], but independence is stronger than being uncorrelated.
- The binomial variance proof writes a binomial variable as a sum of [[bernoulli-distribution|Bernoulli indicators]].

## Pitfalls

- Variance uses $\mathbb{E}[X^2]$, not $\mathbb{E}[X]^2$ alone.
- Translation does not change variance; scaling by $a$ multiplies variance by $a^2$.
- A correlation coefficient is defined only when both variances are positive.

## Appears in

[[stochastics-6-7]], [[lecture-block-6-7-exercises]], [[expectation]], [[binomial-distribution]], [[poisson-distribution]], [[uniform-distribution]]

