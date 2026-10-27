---
title: Maximum Likelihood Estimation
type: method
tags: [statistics, estimators, likelihood]
sources: ["stochastics-1.pdf p.19", "stochastics-1.pdf p.25-26", "stochastics_formulas.pdf p.2"]
updated: 2026-10-15
---

# Maximum Likelihood Estimation

## Goal / when to use

Use maximum likelihood estimation when a statistical model gives the probability or density of the observed sample as a function of an unknown parameter, and the desired estimate is the parameter value that makes the observed sample most likely.

## Assumptions

- A model $(X,\mathcal{F}_X,(\mathbb{P}_\theta)_{\theta\in\Theta})$ is specified.
- $X$ is at most countable in the source's definition on p.19, so likelihoods are probabilities of the observed sample.
- A sample point $x\in X$ is observed.

## Procedure

```text
1. Write the likelihood L_x(theta) = P_theta({x}) for the observed sample x.
2. Drop factors that do not depend on theta, if this does not change the maximizer.
3. Maximize L_x(theta) over theta in Theta.
4. If the maximizer is unique, report it as the maximum likelihood estimator T(x).
5. If several maximizers exist, record the non-uniqueness instead of guessing one.
```

## Definition from the notes

The source calls $T:X\to\Theta$ a maximum likelihood estimator for $\theta$ if for every $x\in X$, $T(x)$ is a maximizer of
$$
L_x(\theta)=\mathbb{P}_\theta(\{x\}).
$$

```mermaid
flowchart LR
  Model --> Likelihood[likelihood]
  Likelihood --> Maximize
  Maximize --> Estimator[estimator]
```

## Worked examples from p.1-25

### Degenerate uniform-on-prefix model

Let $\mathbb{P}_m$ be defined on $\mathbb{N}$ by
$$
\mathbb{P}_m(\{x\})=
\begin{cases}
1/m,& x\le m,\\
0,& x>m.
\end{cases}
$$
For one observed value $x$, $\mathbb{P}_m(\{x\})$ is maximal when $m=x$, so the maximum likelihood estimator is $T(x)=x$.

### Geometric likelihood completed on p.26

For a sample $x=(x_1,\ldots,x_n)\in\mathbb{N}_0^n$ from i.i.d. [[geometric-distribution|geometric]] variables, p.26 continues the handwritten derivation with
$$
L_x(p)=\prod_{i=1}^n p^{x_i}(1-p),
$$
so
$$
\log L_x(p)=\sum_{i=1}^n x_i\log p+n\log(1-p)
=n\bar{X}_n\log p+n\log(1-p).
$$
The score equation is
$$
\frac{d}{dp}\log L_x(p)=\frac{n\bar{X}_n}{p}-\frac{n}{1-p}=0,
$$
hence
$$
\hat p=\frac{\bar{X}_n}{1+\bar{X}_n}.
$$
This uses the wiki primary convention $\mathbb{P}(X=k)=p^k(1-p)$ from [[geometric-distribution]]; the success-parameter alternative is handled there by converting $q=1-p$.

## Common mistakes

- The likelihood is a function of the parameter after the data are fixed.
- Check which geometric parameter convention is being used before differentiating the likelihood.

## See also

[[point-estimation]], [[geometric-distribution]], [[stochastics-1]]

