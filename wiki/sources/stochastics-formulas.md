---
title: Stochastics Formulas Source
type: source
tags: [formula-summary, exam-relevant, verification]
sources: ["stochastics_formulas.pdf p.1-2"]
updated: 2026-10-15
---

# stochastics_formulas.pdf ? condensed formula summary

This two-page source is the student's handwritten exam-style formula summary. Unlike the lecture-block scans, it is not a derivation source: it is a dense grid of formulas spanning [[discrete-probability-space|probability basics]], [[combinatorial-counting]], [[conditional-probability]], named [[probability-distribution|distributions]], [[expectation]], [[variance-covariance-correlation]], [[moment-generating-function|MGFs]], inequalities, convergence, [[stochastic-process|stochastic processes]], and statistics.

## Layout / topic map

| Page / region | Content |
|---|---|
| p.1 top-left | Discrete and Laplace probability spaces, complement/monotonicity, Dirac law, binomial/Poisson/geometric starts. |
| p.1 top-middle | Inclusion-exclusion, product spaces, conditional probability, total probability, Bayes formula, hypergeometric law. |
| p.1 top-right | Combinatorial identities, four urn-counting cases, independence, sigma-algebra and probability-space axioms. |
| p.1 middle-left | Indicator, Bernoulli, uniform, Pareto, exponential, normal distribution formulas. |
| p.1 middle | Expectation, variance, covariance, correlation, sums, convolutions, conditional expectation, MGFs. |
| p.1 middle-right | Random-variable distribution, CDF interval rules, density conditions, independence of random variables, Markov/Chebyshev. |
| p.1 bottom | Weak law, convergence in probability/distribution, Poisson process, CLT/De Moivre-Laplace, Brownian motion and independent increments. |
| p.2 top-left/middle | Process mean/covariance functions, Markov chains, one-sided and two-sided Gaussian tests, Gaussian confidence interval derivation. |
| p.2 top-right | Sample mean, sample variance, sample median, statistical model, consistency, MLE, confidence intervals, quantiles, tests, one-sided binomial test. |

## Formula extraction checklist

### Probability basics and combinatorics

1. Discrete probability space $(\Omega,\mathbb{P})$ with $\mathbb{P}(\Omega)=1$ and countable additivity over disjoint events ? corroborates [[discrete-probability-space]].
2. Laplace rule $\mathbb{P}(A)=|A|/|\Omega|$ ? corroborates [[laplace-probability-space]].
3. Complement rule $\mathbb{P}(A^c)=1-\mathbb{P}(A)$ ? corroborates [[probability-rules]].
4. Monotonicity $A\subseteq B\Rightarrow\mathbb{P}(A)\le\mathbb{P}(B)$ ? corroborates [[probability-rules]].
5. Inclusion-exclusion for $n$ events ? corroborates [[inclusion-exclusion-principle]].
6. Product space $\Omega=\prod_i\Omega_i$ and event probability as a sum over event tuples ? corroborates [[product-probability-space]].
7. Pascal identity $\binom{m}{k}=\binom{m-1}{k-1}+\binom{m-1}{k}$ ? corroborates [[combinatorial-counting]].
8. Binomial theorem $(a+b)^m=\sum_i\binom{m}{i}a^ib^{m-i}$ ? corroborates [[combinatorial-counting]].
9. Ordered samples with replacement: $M^n$ ? corroborates [[combinatorial-counting]].
10. Ordered samples without replacement: $M!/(M-n)!$ ? corroborates [[combinatorial-counting]].
11. Unordered samples with replacement: $\binom{M+n-1}{n}$ ? corroborates [[combinatorial-counting]].
12. Unordered samples without replacement: $\binom{M}{n}$ ? corroborates [[combinatorial-counting]].
13. Factorial binomial coefficient formula $\binom{M}{n}=M!/(n!(M-n)!)$ ? corroborates [[combinatorial-counting]].

### Conditional probability and independence

14. Conditional probability $\mathbb{P}(A\mid B)=\mathbb{P}(A\cap B)/\mathbb{P}(B)$ ? corroborates [[conditional-probability]].
15. Conditional complement $\mathbb{P}(A\mid B)+\mathbb{P}(A^c\mid B)=1$ ? corroborates [[conditional-probability]].
16. Law of total probability $\mathbb{P}(A)=\sum_i\mathbb{P}(A\mid B_i)\mathbb{P}(B_i)$ ? corroborates [[law-of-total-probability]].
17. Bayes formula $\mathbb{P}(B_i\mid A)=\mathbb{P}(B_i)\mathbb{P}(A\mid B_i)/\sum_j\mathbb{P}(B_j)\mathbb{P}(A\mid B_j)$ ? corroborates [[bayes-formula]].
18. Event independence $\mathbb{P}(A\cap B)=\mathbb{P}(A)\mathbb{P}(B)$ ? corroborates [[independence]].
19. Finite-family independence product criterion ? corroborates [[independence]].
20. Sigma-algebra closure under complement and countable unions ? corroborates [[sigma-algebra]].
21. Probability space axioms $(\Omega,\mathcal{F},\mathbb{P})$ ? corroborates [[probability-space]].

### Random variables, distributions, CDFs, densities

22. Random-variable distribution $\mathbb{P}_X(A)=\mathbb{P}(X\in A)$ ? corroborates [[random-variable]].
23. CDF $F_X(y)=\mathbb{P}(X\le y)$ ? corroborates [[cumulative-distribution-function]].
24. Point mass $\mathbb{P}(X=y)=F_X(y)-F_X(y^-)$ ? corroborates [[cumulative-distribution-function]].
25. Interval probability $\mathbb{P}(a\le X\le b)=F_X(b)-F_X(a^-)$ ? corroborates [[cumulative-distribution-function]].
26. Density criteria $f\ge0$ and $\int f=1$ ? corroborates [[probability-density]].
27. CDF from density $F_X(y)=\int_{-\infty}^y f(x)\,dx$ ? corroborates [[probability-density]].
28. Independence criterion for random variables by products of event probabilities ? corroborates [[independence]].

### Named distributions

29. Dirac distribution $\mathbb{P}(\omega_0)=1$ ? corroborates [[dirac-distribution]].
30. Bernoulli$(p)$ point masses and CDF ? corroborates [[bernoulli-distribution]].
31. Binomial$(n,p)$ PMF, mean $np$, variance $np(1-p)$ ? corroborates [[binomial-distribution]].
32. Poisson$(\lambda)$ PMF, mean $\lambda$, variance $\lambda$ ? corroborates [[poisson-distribution]].
33. Geometric displayed PMF $\mathbb{P}(X=k)=p^k(1-p)$ ? corroborates the wiki PMF on [[geometric-distribution]].
34. Geometric moments written on the sheet ? conflict; see verification outcome below and [[geometric-distribution]].
35. Hypergeometric urn PMF $\binom{b}{k}\binom{r}{n-k}/\binom{b+r}{n}$ ? corroborates [[hypergeometric-distribution]].
36. Uniform$([a,b])$ CDF, mean $(a+b)/2$, variance $(b-a)^2/12$ ? corroborates [[uniform-distribution]].
37. Pareto CDF $0$ for $y<1$, $1-y^{-\alpha}$ for $y\ge1$ ? corroborates [[pareto-distribution]].
38. Exponential$(\lambda)$ CDF $1-e^{-\lambda y}$ for $y\ge0$, mean $1/\lambda$, variance $1/\lambda^2$ ? corroborates [[exponential-distribution]].
39. Standard normal density, mean $0$, variance $1$, symmetry $\Phi(-t)=1-\Phi(t)$ ? corroborates [[normal-distribution]].
40. Affine normal standardization and sums/averages of normals ? corroborates [[normal-distribution]].

### Expectation, variance, covariance, sums, MGFs

41. Discrete expectation $\sum_\omega X(\omega)\mathbb{P}(\{\omega\})=\sum_y y\mathbb{P}(X=y)$ ? corroborates [[expectation]].
42. Continuous expectation $\int x f(x)\,dx$ ? corroborates [[expectation]].
43. Expectation of $h(X)$ by sum or integral ? corroborates [[expectation]].
44. Linearity $\mathbb{E}[X+Y]=\mathbb{E}[X]+\mathbb{E}[Y]$, $\mathbb{E}[aX]=a\mathbb{E}[X]$ ? corroborates [[expectation]].
45. Indicator expectation $\mathbb{E}[\mathbf{1}_A]=\mathbb{P}(A)$ ? corroborates [[expectation]].
46. Variance identity $\mathrm{Var}(X)=\mathbb{E}[X^2]-\mathbb{E}[X]^2$ ? corroborates [[variance-covariance-correlation]].
47. Variance scale/shift rules ? corroborates [[variance-covariance-correlation]].
48. Covariance identity ? corroborates [[variance-covariance-correlation]].
49. Covariance bilinearity ? corroborates [[variance-covariance-correlation]].
50. Correlation coefficient ? corroborates [[variance-covariance-correlation]].
51. Variance of a finite sum with covariance terms ? corroborates [[variance-covariance-correlation]].
52. If $X,Y$ independent, $\mathbb{E}[XY]=\mathbb{E}[X]\mathbb{E}[Y]$ ? corroborates [[independence]].
53. Distribution of a maximum of i.i.d. uniforms via $\mathbb{P}(Y\le x)=\mathbb{P}(U_1\le x)^n$ ? corroborates [[lecture-block-6-7-exercises]].
54. Conditional expectation on an event and total expectation over a partition ? corroborates [[conditional-expectation]].
55. Discrete convolution for integer-valued sums ? corroborates [[convolution-of-distributions]].
56. Density convolution $f_{X+Y}=f_X*f_Y$ ? corroborates [[convolution-of-distributions]].
57. MGF definition $M_X(t)=\mathbb{E}[e^{tX}]$ ? corroborates [[moment-generating-function]].
58. Moment recovery $\mathbb{E}[X^m]=M_X^{(m)}(0)$ ? corroborates [[moment-generating-function]].
59. Independent-sum MGF product and same-distribution MGF criterion ? corroborates [[moment-generating-function]].

### Inequalities, convergence, limit theorems

60. Markov inequality ? corroborates [[markov-inequality]].
61. Chebyshev inequality ? corroborates [[chebyshev-inequality]].
62. Weak law of large numbers for i.i.d. variables with finite second moment ? corroborates [[weak-law-large-numbers]].
63. Convergence in probability definition ? corroborates [[convergence-of-random-variables]].
64. Convergence in distribution definition via CDF convergence ? corroborates [[convergence-of-random-variables]].
65. Central limit theorem ? corroborates [[central-limit-theorem]].
66. De Moivre-Laplace / binomial normal approximation ? corroborates [[de-moivre-laplace-theorem]] and [[normal-approximation]].

### Stochastic processes

67. Stochastic process as a collection $(X_t)_{t\in T}$ and paths $t\mapsto X_t(\omega)$ ? corroborates [[stochastic-process]].
68. Mean function $\mu(t)=\mathbb{E}[X_t]$ ? added to [[stochastic-process]].
69. Covariance function $\rho(s,t)=\mathrm{Cov}(X_s,X_t)$ ? added to [[stochastic-process]].
70. Markov property and transition probabilities $p_{ij}$ ? corroborates [[markov-chain]].
71. Transition matrix $P$ and update $p(t+1)=p(t)P$ ? corroborates [[markov-chain]].
72. Poisson process independent increments and $N_t-N_s\sim\mathrm{Poisson}(\lambda(t-s))$ ? corroborates [[poisson-process]].
73. Brownian motion conditions, Gaussian increments, marginal $B_t\sim\mathcal{N}(0,t)$ ? corroborates [[brownian-motion]].
74. Independent-increments definition ? corroborates [[stochastic-process]].

### Statistics

75. Statistical model $(X,\mathcal{F}_X,(\mathbb{P}_\theta)_{\theta\in\Theta})$ ? corroborates [[point-estimation]].
76. Sample mean $\bar{X}_n=n^{-1}\sum_iX_i$ ? corroborates [[point-estimation]].
77. Sample variance $S_X^2=(n-1)^{-1}\sum_i(X_i-\bar{X}_n)^2$ ? corroborates [[point-estimation]].
78. Sample median formula for odd/even $n$ ? added to [[point-estimation]].
79. Unbiased estimator definition and bias ? corroborates [[point-estimation]].
80. Consistency definition ? corroborates [[point-estimation]].
81. Likelihood for i.i.d. samples as product of probabilities ? corroborates [[maximum-likelihood-estimation]].
82. MLE as an argmax of the likelihood ? corroborates [[maximum-likelihood-estimation]].
83. Gaussian two-sided confidence interval derivation ? corroborates [[confidence-intervals]].
84. Confidence interval definition and error level $\alpha$ ? corroborates [[confidence-intervals]].
85. Quantile definition ? corroborates [[quantile]].
86. General test setup $H_0,H_1$, decision function $\varphi$, level, and power ? corroborates [[hypothesis-testing]].
87. One-sided Gaussian mean test ? corroborates [[hypothesis-testing]].
88. Two-sided Gaussian mean test ? corroborates [[hypothesis-testing]].
89. One-sided binomial test idea ? corroborates [[hypothesis-testing]], with one obscured handwritten threshold detail flagged below.

## Verification outcome

- Extracted readable formulas/items: 89.
- Corroborated existing wiki content: 84 items.
- Added or clarified in the wiki: 4 items ? sample median in [[point-estimation]], process mean/covariance functions in [[stochastic-process]], and a formula-sheet cross-check note in [[hypothesis-testing]].
- Conflicted with the existing, internally consistent wiki: 1 item ? the geometric-distribution moments on p.1.

### Conflict / likely formula-sheet error

> ?? Note: `stochastics_formulas.pdf` p.1 states the geometric PMF as $\mathbb{P}(X=k)=p^k(1-p)$ on $\mathbb{N}_0$ but then gives moments compatible with a different convention. For the displayed PMF,
> $$
> \mathbb{E}[X]=\frac{p}{1-p},\qquad \mathrm{Var}(X)=\frac{p}{(1-p)^2}.
> $$
> The value $1/p$ would belong to a different parameterization only when $p$ is the success probability and the variable counts the first successful trial in $\{1,2,\ldots\}$.

### Unreadable / obscured source detail

> WARNING: Unreadable in source: `stochastics_formulas.pdf` p.2 lower-right one-sided binomial-test rejection rule is partly obscured by a punched hole; the surrounding hypothesis and the large-sum rejection pattern are readable, and the clean threshold formula is already sourced from `stochastics-1.pdf` p.30-34.

## Key takeaways

- The formula summary is a high-value checklist rather than a source of new theory.
- It strongly confirms that the exam backbone is: probability rules and counting; conditioning/Bayes; named distributions and moments; expectation/variance/covariance; convolutions/MGFs; Markov/Chebyshev/WLLN/CLT; stochastic processes; and basic inference.
- The only substantive contradiction found is the geometric-moment convention error.
- [[cheatsheet]] has been rebuilt as the navigable revision sheet based on this source.

## Pages touched

- [[cheatsheet]], [[overview]], [[index]], [[open-questions]], [[log]]
- [[discrete-probability-space]], [[laplace-probability-space]], [[probability-rules]], [[inclusion-exclusion-principle]], [[combinatorial-counting]], [[product-probability-space]]
- [[conditional-probability]], [[law-of-total-probability]], [[bayes-formula]], [[independence]], [[sigma-algebra]], [[probability-space]]
- [[random-variable]], [[cumulative-distribution-function]], [[probability-density]], [[expectation]], [[conditional-expectation]], [[variance-covariance-correlation]], [[convolution-of-distributions]], [[moment-generating-function]]
- [[dirac-distribution]], [[bernoulli-distribution]], [[binomial-distribution]], [[poisson-distribution]], [[geometric-distribution]], [[hypergeometric-distribution]], [[uniform-distribution]], [[discrete-uniform-distribution]], [[pareto-distribution]], [[exponential-distribution]], [[normal-distribution]]
- [[markov-inequality]], [[chebyshev-inequality]], [[weak-law-large-numbers]], [[convergence-of-random-variables]], [[central-limit-theorem]], [[de-moivre-laplace-theorem]], [[normal-approximation]]
- [[stochastic-process]], [[markov-chain]], [[poisson-process]], [[brownian-motion]]
- [[point-estimation]], [[maximum-likelihood-estimation]], [[confidence-intervals]], [[quantile]], [[hypothesis-testing]]
