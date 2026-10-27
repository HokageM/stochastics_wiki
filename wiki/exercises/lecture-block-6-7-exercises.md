---
title: Lecture Block 6-7 Exercises
type: exercise
tags: [exercises, random-variables, expectation, variance, covariance]
sources: ["stochastics_6_7.pdf p.8-12", "stochastics_6_7.pdf p.18-24", "stochastics_6_7.pdf p.29-34"]
updated: 2026-10-15
---

# Lecture Block 6-7 Exercises

Worked patterns from lecture blocks 6-7. These exercises use [[cumulative-distribution-function|CDFs]], [[probability-density|densities]], [[expectation]], [[tail-sum-formula]], [[variance-covariance-correlation]], and named distributions.

## Poisson thinning by a binomial conditional law

Problem: Let $X\sim\mathrm{Poisson}(\lambda)$. Given $X=x$, let $Y\mid X=x\sim\mathrm{Binomial}(x,p)$. Show that $Y$ is Poisson distributed.

For $y=0,1,2,\ldots$,
$$
\mathbb{P}(Y=y)=\sum_{x=y}^{\infty}\binom{x}{y}p^y(1-p)^{x-y}e^{-\lambda}\frac{\lambda^x}{x!}
=e^{-\lambda}\frac{(\lambda p)^y}{y!}\sum_{s=0}^{\infty}\frac{((1-p)\lambda)^s}{s!}
=e^{-\lambda p}\frac{(\lambda p)^y}{y!}.
$$
Thus $Y\sim\mathrm{Poisson}(\lambda p)$.

```mermaid
flowchart LR
  X --> Thin
  Thin --> Y
  Y --> Pois
```

## Dependent joint table

The notes give $X\in\{1,2,3\}$ with probabilities $0.5,0.3,0.2$ and $Y\in\{1,2\}$ with probabilities $0.7,0.3$. The completed table is:

| $Y\backslash X$ | $1$ | $2$ | $3$ | row sum |
|---|---:|---:|---:|---:|
| $1$ | $0.35$ | $0.15$ | $0.20$ | $0.70$ |
| $2$ | $0.15$ | $0.15$ | $0$ | $0.30$ |
| column sum | $0.50$ | $0.30$ | $0.20$ | $1$ |

They are not independent because $\mathbb{P}(X=3,Y=2)=0\ne0.2\cdot0.3$.

## Triangular density on $[0,2]$

Problem: determine $a$ so that
$$
f(x)=\begin{cases}
ax,&x\in[0,1],\\
a(2-x),&x\in(1,2],\\
0,&\text{otherwise}
\end{cases}
$$
is a density, and compute its CDF.

Normalization gives $a=1$. Then
$$
F_X(y)=\begin{cases}
0,&y<0,\\
y^2/2,&0\le y<1,\\
-y^2/2+2y-1,&1\le y\le2,\\
1,&y>2.
\end{cases}
$$
The notes later compute $\mathbb{E}[X]=1$, $\mathbb{E}[X^2]=7/6$, and $\mathrm{Var}(X)=1/6$.

## Transforming a uniform variable

For $X\sim U([2,4])$, the density is $f_X(x)=1/2$ on $[2,4]$. The CDF is
$$
F_X(y)=\begin{cases}
0,&y<2,\\
(y-2)/2,&2\le y\le4,\\
1,&y>4.
\end{cases}
$$
For $Y=2X$, $F_Y(y)=F_X(y/2)$, so $Y$ has density $f_Y(y)=1/4$ on $[4,8]$ and $0$ otherwise.

## Expectation identities and named laws

- Indicator: $\mathbb{E}[\mathbf{1}_A]=\mathbb{P}(A)$.
- Poisson mean: $\mathbb{E}[X]=\lambda$.
- Binomial mean: write $X=\sum_{i=1}^n\mathbf{1}_{A_i}$ to get $\mathbb{E}[X]=np$.
- Continuous uniform mean: $\mathbb{E}[X]=(a+b)/2$.
- Exponential mean: $\mathbb{E}[X]=1/\lambda$.
- Standard normal mean: $\mathbb{E}[X]=0$ by symmetry/oddness.
- Discrete uniform mean: $\mathbb{E}[X]=(n+1)/2$.

## Tail-sum and geometric mean

For nonnegative integer-valued $X$,
$$
\mathbb{E}[X]=\sum_{k=1}^{\infty}\mathbb{P}(X\ge k).
$$
For the geometric convention $\mathbb{P}(X=k)=p^k(1-p)$ on $\mathbb{N}_0$,
$$
\mathbb{P}(X\ge a)=p^a,
\qquad
\mathbb{E}[X]=\sum_{a=1}^{\infty}p^a=\frac{p}{1-p}.
$$

## Maximum of independent uniforms

For independent $U_1,\ldots,U_n\sim U([0,1])$ and $Y=\max(U_1,\ldots,U_n)$,
$$
F_Y(x)=\mathbb{P}(U_1\le x,\ldots,U_n\le x)=x^n\quad(0\le x\le1).
$$
Thus $f_Y(y)=ny^{n-1}$ on $[0,1]$, and $\mathbb{E}[Y]=n/(n+1)\to1$.

## Second moments and variance

The notes compute:

- $\mathbb{E}[X(X-1)]=\lambda^2$ for $X\sim\mathrm{Poisson}(\lambda)$.
- For $X\sim U([a,b])$, $\mathbb{E}[X^2]=(b^2+ab+a^2)/3$ and $\mathrm{Var}(X)=(b-a)^2/12$.
- For a fair die, $\mathrm{Var}(X)=35/12$.
- For $X\sim\mathrm{Poisson}(\lambda)$, $\mathrm{Var}(X)=\lambda$.
- For $X\sim\mathrm{Binomial}(n,p)$, $\mathrm{Var}(X)=np(1-p)$.

## Poisson transform

For $\lambda>0$ and $X\sim\mathrm{Poisson}(\lambda)$,
$$
\mathbb{E}[\lambda^{-X}]=\sum_{k=0}^{\infty}\lambda^{-k}\frac{\lambda^k}{k!}e^{-\lambda}=e^{-\lambda}\sum_{k=0}^{\infty}\frac1{k!}=e^{1-\lambda}.
$$

## Covariance and variance of linear combinations

Given $\mathrm{Var}(X)=2$, $\mathrm{Var}(Y)=3$, and $\rho_{X,Y}=0.5$, the covariance is $\mathrm{cov}(X,Y)=\sqrt6/2$. Then
$$
\mathrm{cov}(3X+Y,2X-5Y)=12-15+(-15+2)\frac{\sqrt6}{2}\approx -18.9,
$$
and
$$
\mathrm{Var}(3X-2Y)=9\cdot2-12\frac{\sqrt6}{2}+4\cdot3\approx15.3.
$$

## Pareto moments and symmetric Pareto-type variable

For [[pareto-distribution]]$(\alpha)$,
$$
\mathbb{E}[X]=\frac{\alpha}{\alpha-1}\quad(\alpha>1),
\qquad
\mathbb{E}[X^2]=\frac{\alpha}{\alpha-2}\quad(\alpha>2).
$$
The final exercise defines a symmetric density
$$
f_Y(y)=\begin{cases}\frac12\alpha |y|^{-\alpha-1},&|y|\ge1,\\0,&\text{otherwise},\end{cases}
$$
and splits the expectation over negative and positive halves. For $\alpha>1$, the two halves cancel, giving $\mathbb{E}[Y]=0$.

## Generalizable procedures

```text
1. For a piecewise density, normalize first and only then compute CDF or moments.
2. For a transformed variable Y=h(X), compute F_Y(y)=\mathbb{P}(h(X)<=y) or integrate h(x)f_X(x).
3. For sums of indicators, use linearity for means and covariance terms for variances.
4. For tail-heavy distributions, compute moments by checking the limiting boundary term.
5. For linear combinations, expand covariance bilinearly and substitute known variances/covariances.
```

## Source warning

> WARNING: Unreadable in source: stochastics_6_7.pdf p.20 contains a rectangle diagram and a final expectation expression whose exact target quantity/result are not fully legible. The visible content says $X$ and $Y$ are independent for a uniform point in a rectangle, but the final line is ambiguous.

## See also

[[stochastics-6-7]], [[expectation]], [[variance-covariance-correlation]], [[poisson-distribution]], [[binomial-distribution]], [[geometric-distribution]], [[uniform-distribution]], [[pareto-distribution]]

