---
layout: post
author: viridi
title: multiple linear regression
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: math
tags: ["regression", "linear", "multiple"]
date: 2021-02-25 03:54:00 +07
permalink: /math/multiple-linear-regression
---
A linear approach in statistics to model the relationship between a scalar response (dependent variable) and more than many explanatory variables (independent variables) is known as multiple linear regression [[1](#ref1)].


## data set
Supposed that there is a data set [[2](#ref2),[3](#ref3)] of $N$ statistical unit [[4](#ref4)]

\begin{equation}
\label{eqn:mlr-data-set}
\\{y_i, x_{i1}, x_{i2}, \dots, x_{iM}\\}_{i = 1}^N,
\end{equation}

where the relation between dependent variable $y$ and regressor $\mathbf{x}$ is linear, where $x$ is a $M$- dimensional vector [[5](#ref5)].


## linear equation
From a linear equation of $M$ unknown variables [[6](#ref6)] we can write

\begin{equation}
\label{eqn:mlr-linear-equation}
y_i = \sum_{j = 1}^M x_{ij} c_j,
\end{equation}

for the each data set $i$ with $\\{c_j\\}_{j = 1}^M$ are coefficients to be found. 


## least square
For a linear regression line in the form of $y = c_0 + c_1 x$ we can use least square, where the example data [[7](#ref7)] and code [[8](#ref8)] are available. And the coefficients are

\begin{equation}
\label{eqn:mlr-linear-equation-2-c0}
c_0 = \bar{y} - c_1 \bar{x}
\end{equation}

and

\begin{equation}
\label{eqn:mlr-linear-equation-2-c1}
c_1 = \frac{\displaystyle \sum_{i = 1}^N (x_i - \bar{x})(y_i - \bar{y})}{\displaystyle \sum_{i = 1}^N (x_i - \bar{x})^2}
\end{equation}

for $N$ data sets, where $\bar{x}$ and $\bar{y}$ are average of $x$ and $y$, respectively.


## references
1. <a href="#ref1"></a> Wikipedia contributors, "Linear regression", Wikipedia, The Free Encyclopedia, 16 Feb 2021, 07:19 UTC, <https://en.wikipedia.org/w/index.php?oldid=1007058436> [20210225].
2. <a href="#ref2"></a>Adam Ross Nelson, "What Is A Data Set?", Towards Data Science,
27 Jan 2020, url <https://towardsdatascience.com/what-is-a-data-set-9c6e38d33198> [20210225].
3. <a href="#ref3"></a>U.S. Geological Survey, "https://www.usgs.gov/faqs/what-are-differences-between-data-a-dataset-and-a-database", USGS, url <> [20210225].
4. <a href="#ref4"></a>-, "Definition Statistical unit", Statista, url <https://www.statista.com/statistics-glossary/definition/372/statistical_unit/> [20210225].
5. <a href="#ref5"></a>Christopher Stover, Eric W. Weisstein, "n-Vector", from MathWorld--A Wolfram Web Resource, url <https://mathworld.wolfram.com/n-Vector.html> [20210225].
6. <a href="#ref6"></a>Wikipedia contributors, "Linear equation", Wikipedia, The Free Encyclopedia, 24 Feb 2021, 14:22 UTC, <https://en.wikipedia.org/w/index.php?oldid=1008679832> [20210225].
7. <a href="#ref7"></a>Andrew Lee, "Calculating a Least Squares Regression Line: Equation, Example, Explanation", Technology Networks, 21 Aug 2020, url <https://www.technologynetworks.com/informatics/articles/calculating-a-least-squares-regression-line-equation-example-explanation-310265> [20210225].
8. <a href="#ref8"></a>Adarsh Menon, "Linear Regression Using Least Squares", Towards Data Science, 8 Sep 2018, url <https://towardsdatascience.com/linear-regression-using-least-squares-a4c3456e8570> [20210225].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/math/2021-02-25-multiple-linear-regression.md)