---
title: Independence
type: concept
tags: [independence, conditional-probability, events, random-variables]
sources: ["stochastics_4_5.pdf p.4", "stochastics_4_5.pdf p.8-9", "stochastics_6_7.pdf p.6-9", "stochastics_6_7.pdf p.15", "stochastics_6_7.pdf p.27-28", "stochastics_formulas.pdf p.1"]
updated: 2026-10-15
---

# Independence (*Unabhängigkeit*)
> Events or random variables are independent when joint probabilities factor into products of marginal probabilities.

## Formal definition: events

In a [[discrete-probability-space]] $(\Omega,\mathbb{P})$, two events $A,B\subseteq\Omega$ are independent if
$$
\mathbb{P}(A\cap B)=\mathbb{P}(A)\mathbb{P}(B).
$$
For $n\ge2$, events $A_1,\ldots,A_n$ are mutually independent if every subfamily intersection factors.

## Formal definition: random variables

Random variables $X_1,\ldots,X_n$ are independent if
$$
\mathbb{P}(X_1\in A_1,\ldots,X_n\in A_n)=\prod_{i=1}^n\mathbb{P}(X_i\in A_i)
$$
for all Borel sets $A_i\in\mathcal{B}(\mathbb{R})$.

The notes state two useful criteria:

1. CDF criterion:
   $$
   \mathbb{P}(X_1\le y_1,\ldots,X_n\le y_n)=\prod_{i=1}^n\mathbb{P}(X_i\le y_i).
   $$
2. Discrete point-mass criterion:
   $$
   \mathbb{P}(X_1=y_1,\ldots,X_n=y_n)=\prod_{i=1}^n\mathbb{P}(X_i=y_i).
   $$

## Consequences

If $X$ and $Y$ are independent and integrable, then $\mathbb{E}[XY]=\mathbb{E}[X]\mathbb{E}[Y]$. With finite second moments, independence implies $\mathrm{cov}(X,Y)=0$.

## Intuition

```mermaid
flowchart TD
  Joint --> Factor
  Factor -- yes --> Indep
  Factor -- no --> Dep
  Indep --> ProductMean=EE
  Indep --> ZeroCov
  ZeroCov -. converse not stated .-> Indep
```

## Examples from the sources

- For two die coordinates $X_1(\omega_1,\omega_2)=\omega_1$ and $X_2(\omega_1,\omega_2)=\omega_2$, the point-mass criterion gives independence because $1/36=(1/6)(1/6)$.
- In [[lecture-block-6-7-exercises]], the [[joint-and-marginal-distributions|joint table]] with $\mathbb{P}(X=3,Y=2)=0$ is not independent because the marginal product is $0.2\cdot0.3$.

## Pitfalls

- Pairwise independence is not enough for mutual independence.
- Disjoint nonempty events with positive probabilities are generally not independent.
- Uncorrelated variables have zero covariance, but the lecture only proves independence implies zero covariance, not the converse.

## Appears in

[[stochastics-4-5]], [[stochastics-6-7]], [[lecture-block-4-5-exercises]], [[lecture-block-6-7-exercises]], [[conditional-probability]], [[variance-covariance-correlation]]

