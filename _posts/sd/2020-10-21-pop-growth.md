---
layout: post
author: viridi
title: population growth
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: true
category: system dynamics
tags: [""]
date: 2020-10-21 13:11:00 +07
permalink: /sd/pop-growth
---
Population dynamics can be studied using growth model through generalized logistic function in the form of differential equation
[[1](#ref1)], difference equation for population with synchronized generations [[2](#ref2)], or density-dependent matrix accomodating age structure [[3](#ref3)]. As consequence, there will be impacts due to the population growth, which could depend on technology and behaviour shifts for human [[4](#ref4)] and conservation, wildlife management
and ecotoxicology for the others [[5](#ref5)]. System dynamics (SD) will be used to discuss it using causal loop diagram [[6](#ref6)]. 


## Growth model
Three different approach are mentioned in brief as follow.

### Differential function
A generalized logistic function in the form of [[1](#ref1)]

\begin{equation}
\label{eqn:sdpg-differential-equation}
\frac{dN}{dt} = r N^\alpha \left[ 1 - \left( \frac{N}{K} \right)^\beta \right]^\gamma,
\end{equation}

where $\alpha$, $\beta$, $\gamma$ are positive real numbers, $K$ is carrying capacity, and $N$ is population size.

### Difference equation
A difference equation for population with synchronized generations is [[2](#ref2)]

\begin{equation}
\label{eqn:sdpg-difference-equation}
N_{t+1} = N_t \ f(N_t) 
\end{equation}

with $N_t$ is the population density at generation $t$ and $f(N_t)$ is population per-capita growth rate.

### Matrix equation
Model proposed by Leslie

\begin{equation}
\label{eqn:sdpg-matrix-equation}
\mathbf{N_{t+1}} = \mathbf{M} \mathbf{N_t} 
\end{equation}

where $N_t$ is vector of age structure at time $t$ and $M$ is population projection matrix, where it has been further developed [[3](#ref3)].


## Causal loop diagrams
Relation between population with births and deaths can be illustrated using a causal loop diagram [[6](#ref6)],

{:refdef: style="text-align: center;"}
![an object moves along a frictionless semicircular track](/assets/img/sd/cau-loop-pop.png)
<br />
Figure <a name="fig:sdpg-pop-cld">1</a> Relation between .. and ...
{: refdef}

where $P$ stands for population, $D$ for death, and $B$ for birth. The left loop is a reinforcing loop (R), while right loop is a balancing loop.


## Proposed model
Using SD and causal loop diagram in Fig. <a href="#fig:sdpg-pop-cld">1</a> we can have the birth rate

\begin{equation}
\label{eqn:sdpg-birth-rate}
B = \mu_{BP} P
\end{equation}

and the death rate

\begin{equation}
\label{eqn:sdpg-death-rate}
D = \mu_{DP} P,
\end{equation}

with $\mu_{BP}$ and $\mu_{DP}$ are the coefficients relating the birt and death rates to population. Using Eqns. \eqref{eqn:sdpg-birth-rate} and \eqref{eqn:sdpg-death-rate} we will have

\begin{equation}
\label{eqn:sdpg-pop-change}
\frac{dP}{dt} = B - D.
\end{equation}

Notice that the relation between $B$ and $P$ in Eqn. \eqref{eqn:sdpg-birth-rate} and $D$ and $P$ in Eqn. \eqref{eqn:sdpg-death-rate} is different than between $P$ and $B$ and $P$ and $D$ in Eqn. \eqref{eqn:sdpg-pop-change}. The firt two is a proportional relation, while the last two is accumulation (integral). There could be another in the form of difference (differential).


## References
1. <a name="ref1"></a>A. Tsoularis, J. Wallace, "Analysis of logistic growth models", Mathematical Biosciences [Math. Biosci.], vol. 179, no. 1, pp. 21-55, Jul-Aug 2002, url <https://doi.org/10.1016/S0025-5564(02)00096-2>
2. <a name="ref2"></a>Sebastian J. Schreiber, "Allee effects, extinctions, and chaotic transients in simple population models", Theoretical Population Biology [Theor. Popul. Biol.], vol. 64, no. 2, pp. 201-209, Sep 2003, url <https://doi.org/10.1016/s0040-5809(03)00072-8>
3. <a name="ref3"></a>A. L. Jensen, "Simple density-dependent matrix model for population projection", Ecological Modelling [Ecol Modell.], vol. 77, no. 1, pp. 43-48, Jan 1995, url <https://doi.org/10.1016/0304-3800(93)E0081-D>
4. <a name="ref4"></a>Paul R. Ehrlich, John P. Holdren, "Impact of Population Growth", Science, New Series [Science], vol. 171, no. 3977, pp. 1212-1217, Mar. 1971, url <https://www.jstor.org/stable/1731166>
5. <a name="ref5"></a>Richard M. Sibly, Jim Hone, "Population growth rate and its determinants: an overview", Philosophical Transactions B: Biological Sciences [Phil. Trans. R. Soc. Lond. B Biol. Sci.], vol. 357, no. 1425, pp. 1153-1170, Sep  2002, url <https://dx.doi.org/10.1098%2Frstb.2002.1117>
6. <a name="ref6"></a>Bilash Kanti Bala, Fatimah Mohamed Arshad, Kusairi Mohd Noh, "System Dynamics: Modelling and Simulation", Springer, Singapore, 2017, p. 38, url <http://doi.org/10.1007/978-981-10-2045-2>

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/sd/2020-10-21-pop-growth.md)
