---
title: Normal Distribution
type: distribution
tags: [normal-distribution, gaussian, continuous-distribution]
sources: ["stochastics_6_7.pdf p.5", "stochastics_6_7.pdf p.17", "stochastics.pdf p.3", "p.17-18", "p.24", "p.27", "stochastics-1.pdf p.4", "p.7", "p.11-13", "stochastics-1.pdf p.28-39", "p.49", "stochastics_formulas.pdf p.1", "stochastics_formulas.pdf p.2"]
updated: 2026-10-15
---

# Normal Distribution

| Item | Value from source |
|---|---|
| Support | $\mathbb{R}$ |
| PMF/PDF | Standard density $\varphi(x)=\frac{1}{\sqrt{2\pi}}e^{-x^2/2}$; general density $f_X(x)=\frac{1}{\sqrt{2\pi}\sigma}e^{-(x-\mu)^2/(2\sigma^2)}$ |
| CDF | Standard $\Phi(y)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^y e^{-x^2/2}\,dx$; general $F_X(y)=\Phi((y-\mu)/\sigma)$ |
| $\mathbb{E}[X]$ | $0$ for standard normal in the source |
| $\mathrm{Var}(X)$ | $1$ for standard normal in the later source's $\mathcal{N}(0,1)$ notation; generally $\sigma^2$ by the source's standard-deviation parameter |
| MGF | Not given in this source |
| Parameters | $\mu\in\mathbb{R}$, $\sigma>0$ |

## Story / when it arises

The lecture defines the standard normal density and CDF, then obtains the general Gaussian by the affine transformation $X=\mu+\sigma U$, where $U$ is standard normal. Therefore
$$
F_X(y)=\mathbb{P}(X\le y)=\Phi\left(\frac{y-\mu}{\sigma}\right).
$$

## Relationships

```mermaid
graph TD
  U --> Affine
  Affine --> General
  U --> Symmetry=0
  General --> Sigma
```

## Typical exercise patterns

- Standardize by subtracting $\mu$ and dividing by $\sigma$.
- Use symmetry of the standard density to see $\mathbb{E}[U]=0$.
- Recognize $\Phi$ as an integral, not an elementary closed form in the notes.

## Additional results from stochastics.pdf

The later source uses convolution to show that two independent standard normal variables sum to $\mathcal{N}(0,2)$. It also introduces [[central-limit-theorem]] and [[de-moivre-laplace-theorem]], both using the standard normal CDF $\Phi$ as the limit distribution.

## Three-sigma and Brownian increment uses from stochastics-1.pdf

The p.7 exercise standardizes $X\sim\mathcal{N}(\mu,\sigma^2)$ by $(X-\mu)/\sigma\sim\mathcal{N}(0,1)$ and computes
$$
\mathbb{P}(\mu-3\sigma<X<\mu+3\sigma)=\Phi(3)-\Phi(-3)\approx0.9974.
$$
Pages 4 and 11-13 use normal increments to define and rescale [[brownian-motion]]: for $0\le s<t$, $B_t-B_s\sim\mathcal{N}(0,t-s)$.

## Statistics uses from stochastics-1.pdf p.28-39 and p.49

For independent $X_i\sim\mathcal{N}(\mu,\sigma_0^2)$ with known $\sigma_0$, the sample mean satisfies
$$
\bar{X}_n\sim\mathcal{N}\left(\mu,\frac{\sigma_0^2}{n}\right).
$$
This drives the Gaussian [[confidence-intervals]] and [[hypothesis-testing]] formulas. In the p.49 measurement exercise with $n=25$, $\sigma_0=0.25$, $\alpha=0.05$, and $\bar{x}=5.1$, the one-sided critical value for $H_0:\mu\le5$ is about $5.0822$, so the source rejects $H_0$.

## See also

[[probability-density]], [[cumulative-distribution-function]], [[expectation]], [[variance-covariance-correlation]], [[central-limit-theorem]], [[stochastics-6-7]], [[stochastics]]

