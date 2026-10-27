---
title: Uniform Distribution
type: distribution
tags: [uniform-distribution, continuous-distribution, density]
sources: ["stochastics_6_7.pdf p.2", "stochastics_6_7.pdf p.12", "stochastics_6_7.pdf p.16", "stochastics_6_7.pdf p.24", "stochastics_6_7.pdf p.26", "stochastics.pdf p.11-12", "p.19-20", "stochastics-1.pdf p.22-24", "stochastics_formulas.pdf p.1"]
updated: 2026-10-15
---

# Uniform Distribution

| Item | Value from source |
|---|---|
| Support | $[a,b]$ with $a<b$ |
| PMF/PDF | $f(x)=\frac{1}{b-a}$ for $x\in[a,b]$, $0$ otherwise |
| CDF | $0$ for $y<a$; $(y-a)/(b-a)$ for $a\le y\le b$; $1$ for $y>b$ |
| $\mathbb{E}[X]$ | $(a+b)/2$ |
| $\mathrm{Var}(X)$ | $(b-a)^2/12$ |
| MGF | For $U(0,1)$, $(e^t-1)/t$ for $t\ne0$ and $1$ at $t=0$ |
| Parameters | $a,b\in\mathbb{R}$, $a<b$ |

## Story / when it arises

The source introduces the continuous uniform law as the density that is constant on an interval. A separate exercise uses $X\sim U([2,4])$ with density $1/2$ and transforms it by $Y=2X$, giving density $1/4$ on $[4,8]$.

## Relationships

```mermaid
graph TD
  Constant --> Uniform
  Uniform --> CDF
  Uniform --> Mean
  Uniform --> Var
  IIDn independent U --> Max
```

## Typical exercise patterns

- Normalize a constant density on an interval.
- Integrate to compute a linear [[cumulative-distribution-function]].
- Use symmetry/midpoint for the expectation.
- Transform intervals by scaling, as in $Y=2X$.

## Additional results from stochastics.pdf

The later source computes the triangular density of $X+Y$ for independent $X,Y\sim U(0,1)$ and the MGF $M_X(t)=(e^t-1)/t$ for $t\ne0$. It also shows that discrete uniform variables on $\{1/n,2/n,\ldots,n/n\}$ converge in distribution to $U(0,1)$.

## Endpoint estimation from stochastics-1.pdf

For i.i.d. $U_1,\ldots,U_n\sim U([0,a])$, p.22-p.24 use the sample for [[point-estimation]] of the unknown endpoint $a$. Since $\mathbb{E}_a[U_1]=a/2$, $2\bar U$ is unbiased.

For the maximum $U_{(n)}=\max_iU_i$,
$$
F_{U_{(n)}}(t)=
\begin{cases}
0,&t\le0,\\
(t/a)^n,&0<t<a,\\
1,&t\ge a,
\end{cases}
\qquad
f_{U_{(n)}}(t)=\frac{n}{a^n}t^{n-1}.
$$
Thus $\mathbb{E}_a[U_{(n)}]=an/(n+1)$ and $(n+1)U_{(n)}/n$ is unbiased.

## See also

[[probability-density]], [[cumulative-distribution-function]], [[expectation]], [[variance-covariance-correlation]], [[lecture-block-6-7-exercises]], [[stochastics]]

