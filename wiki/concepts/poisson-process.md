---
title: Poisson Process
type: concept
tags: [stochastic-processes, poisson-process, independent-increments]
sources: ["stochastics-1.pdf p.3", "stochastics-1.pdf p.10", "stochastics-1.pdf p.48", "stochastics_formulas.pdf p.1"]
updated: 2026-10-15
---

# Poisson Process
> A Poisson process counts arrivals whose waiting times are independent exponential random variables.

## Formal definition from the source

For $\lambda>0$, let $(W_i)_{i\in\mathbb{N}}$ be i.i.d. [[exponential-distribution|exponential]]$(\lambda)$ random variables and define arrival times
$$
X_n=\sum_{i=1}^n W_i.
$$
For $t\ge0$, define the counting process
$$
N_t=\sum_{n=1}^{\infty}\mathbf{1}_{\{X_n\le t\}}.
$$
Then $(N_t)_{t\ge0}$ is called a Poisson process with intensity $\lambda$.

## Properties recorded in the notes

- $N_t\sim[[poisson-distribution|\mathrm{Poisson}]](\lambda t)$.
- For $0\le s\le t$, $N_t-N_s\sim\mathrm{Poisson}(\lambda(t-s))$.
- $(N_t)_{t\ge0}$ has independent increments.
- $\mathbb{P}(N_0=0)=1$.

```mermaid
flowchart LR
  W1[waiting time W1] --> X1[arrival X1]
  W2[waiting time W2] --> X2[arrival X2]
  X1 --> Count[N_t counts arrivals up to t]
  X2 --> Count
  Count --> Increments[independent Poisson increments]
```

## Conditional binomial splitting

For $0<s<t$ and $0\le k\le n$, the source derives
$$
\mathbb{P}(N_s=k\mid N_t=n)
=\binom{n}{k}\left(\frac{s}{t}\right)^k\left(1-\frac{s}{t}\right)^{n-k}.
$$
The calculation uses independent increments and Poisson probabilities for $N_s$ and $N_t-N_s$.

## Independent-increment exercise from p.48

For intensity $1$, the source computes
$$
\mathbb{P}(N_2=4,N_{\log16}=4)
=\mathbb{P}(N_2=4)\mathbb{P}(N_{\log16}-N_2=0)
=\frac{2^4}{4!}e^{-2}e^{-(\log16-2)}
=\frac1{24}.
$$
The key step is that $N_{\log16}-N_2$ is independent of $N_2$.

## Relation to other ideas

- The Poisson process extends the [[poisson-distribution]] to time-indexed counting.
- Its construction uses sums of [[exponential-distribution|exponential]] waiting times, relating it to the [[erlang-distribution]].
- Like [[brownian-motion]], it has independent increments; unlike Brownian motion, its paths jump.

## Pitfalls

- $N_t$ is a count, while $X_n$ is an arrival time.
- The parameter of $N_t$ is $\lambda t$, not just $\lambda$.

## Appears in

[[stochastics-1]], [[stochastic-process]], [[poisson-distribution]], [[exponential-distribution]]

