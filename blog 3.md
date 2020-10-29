**This part should not be included in the actual blog**

I want to write with a bit more preparation this time. First I will start by some brainstorming and plan out the structure of this blog.

Goals: Introduce Boolean function's Fourier transformation so that a students with basic linear algebra knowledge should be able to comprehend the concept.

Post Structure:

1. What is Fourier transform, what does it mean, how is it used on Boolean functions (make this concise and clear)

2. Provide definition, explain definition, discuss the relationship between the inner product and the vector space, investigate orthonormal basis

3. Give one or two examples of Boolean functions and solve for their Fourier transform.

4. Conclusion

**Actual Blog Starts Here**

## Introduction and Definition
Hello! Today we will be introducing Fourier transform on Boolean functions including its intuition, definition, and computation. A Fourier transform of Boolean functions has a unique expansion as a **multilinear polynomial** (a polynomial where each variable has degree one). This is categorized as a type of discrete Fourier transform, but its underlying motivation are similar to the continuous [Fourier transform](https://en.wikipedia.org/wiki/Fourier_transform).

This is a fairly new topics for most of us. Therefore, I would like to slowly build up the definition by clarifying each supplementary concept along the way and provide some intuition as well.

Let us first introduce the vector space of functions $f: \left\{-1,1\right\}^n\rightarrow \mathbb{R}$.

An inner product associates a pair of vectors to a scalar quantity, a common example would be the Euclidean dot product. An inner product is usually defined as a bilinear map $Dot(u,v)$. We say bilinear, because we need it to be linear in both variables. More formally, we need: $Dot(Ax + By, v) = ADot(x,v) + BDot(y,v)$ and $Dot(u, Ax + By) = ADot(u,x) + BDot(u,y)$.
In here, we define the **inner product** $f, g: \left\{-1,1\right\}^{n}\rightarrow\mathbb{R}$ to be $\langle f,g \rangle=E_{x\sim \left\{-1,1\right\}^{n}}(f(x)g(x))$, where $x$ is a uniformly chosen random string from the set $\left\{-1,1\right\}^{n}$ and $E$ represents the expected value in probability. Since expectation is linear in both $f$ and $g$, we say that the inner product is a bilinear function.

Once we have defined the vector space and inner product, we can define the basis with size $2^n$:

Let $S$ be a subset of the set $\left\{1,2,3...,n\right\}$.
For all variables $x\in S$, we multiply all variables together. We write such construction as $\chi_{S}(x_{1},x_{2},...,x_{n})= \prod_{i\in S}x_{i}$. Those $\chi_S$ functions are extremely important, as they essentially form the **"Fourier Basis"**, which is stated and proven in theorem 3 below.

**Theorem 1**: The formula for **Fourier transform** stated that every function $f: \left\{-1,1\right\}^{n} \rightarrow\mathbb{R}$ can be expressed as $f(x) = \sum_{ S } \hat{f}(S) \chi_S(x)$, where $\hat{f}(S)=\langle f, \chi_{s} \rangle$, which is the inner product between $f$ and $\chi_{s}$, also called **Fourier coefficient**. 

## Exploring Interesting Properties of Basis
The following proofs can be found in Dr. Ryan O'Donnell's book "Analysis of Boolean Functions", specifically [chapter 1.3](http://www.contrib.andrew.cmu.edu/~ryanod/?p=245). He also teaches such course at Carnegie Mellon University and [all lectures](https://www.youtube.com/playlist?list=PLm3J0oaFux3YypJNaF6sRAf2zC1QzMuTA) are available online.

**Theorem 2**: An n-dimensional Boolean function has a vector space with dimension $2^{n}$.

**Proof**: We know that an n-dimensional Boolean function has $2^n$ unique input, since each bit could either be $-1$ or $1$. We could pair up each unique input with an output. In other word, we will be needing equally $2^n$ outputs to describes $2^n$ inputs. Therefore, we can construct a vector by pairing up such outputs to a vector such that $v=\begin{bmatrix}
x_{1} \\ x_{2} \\ x_{3} \\ \vdots \\ x_{2^{n}}
\end{bmatrix}$. Therefore we can describe our vector space as $V = \left\{f:\left\{-1,1\right\}^{n}\rightarrow \mathbb{R} \right\}=\mathbb{R}^{2^{n}}$.
<div style="text-align: right"> $\square$ </div>

**Lemma 1**: The number of functions in $\chi_{S}$ equals the dimension of the Boolean function vector space $2^{n}$

**Proof**: There exist $2^n$ numbers of subsets in the set S, and each subset corresponds to a unique construction of product. Thus we can conclude that $\chi_{S}(x_{1},x_{2},...,x_{n})= \prod_{i\in S}x_{i}$ has $2^n$ functions in it, which is equal to the dimensions of $V$.
<div style="text-align: right"> $\square$ </div>

**Lemma 2**: For $x \in \left\{-1, 1\right\}^{n}$, it holds that $\chi_{S}(x)\chi_{T}(x)=\chi_{S\oplus T}(x)$, where $S\oplus T$ is the [disjunctive union](https://en.wikipedia.org/wiki/Symmetric_difference) of $S$ and $T$.

**Proof**: We proceed by solving $\chi_{S}(x)\chi_{T}(x)=\prod_{i\in S}x_{i}\prod_{i\in T}x_{i}=\prod_{i\in S\oplus T}x_{i}\prod_{i\in S\cap T}x_{i}^{2}=\prod_{i\in S\oplus T}x_{i}=\chi_{S\oplus T}(x)$
<div style="text-align: right"> $\square$ </div>

**Lemma 3**: If $S=\emptyset$, then the expected value $E\left[\chi_{S}(x)\right]=E\left[\prod_{i\in S}x_{i}\right]=1$. If $S \neq \emptyset$, then the expected value $E\left[\chi_{S}(x)\right]=E\left[\prod_{i\in S}x_{i}\right]=0$.

**Proof**: If $S=\emptyset$, $E\left[\chi_{S}(x)\right]=E\left[1\right]=1$. Now we look at the case where if $S\neq \emptyset$, $E\left[\prod_{i\in S}x_{i}\right]=\prod_{i\in S}E\left[x_{i}\right]$ since $x_1,x_2,...,x_n$ are independent, where $E\left[x_{i}\right]=\frac{1}{2}\cdot1+\frac{1}{2}\cdot (-1)=0$ 
<div style="text-align: right"> $\square$ </div>

**Theorem 3**: $\chi_{S}(x_{1},x_{2},...,x_{n})= \prod_{i\in S}x_{i}$ is an orthonormal basis for $V=\mathbb{R}^{2^{n}}$.

**Proof**: We see that every function in the form of $f:\left\{-1,1\right\}^{n}\rightarrow \mathbb{R}$ can be expressed as a linear combination of $\chi_{S}$. In other words, $\chi_{S}$ is a spanning set for $V$. According to Proposition 1, we can conclude that $\chi_{S}$ is a linearly independent basis for V. Now we assume $S \neq T$, by applying Proposition 2 and Proposition 3, we have the inner product $\langle\chi_{S},\chi_{T}\rangle=E\left[\chi_{S}(x)\chi_{T}(x)\right]=\frac{1}{2^{n}}\sum_x\chi_{S\oplus T}(x)=\frac{1}{2^{n}}\sum_x\prod_{i\in S\oplus T}x_{i}=0$. Therefore, we can conclude that $\chi_{S}$ is an orthonormal basis for $V$.
Dr. Ryan O'Donnell went over an identical proof during his [lecture on Computer Science Theory Toolkit.](https://www.youtube.com/watch?v=TIqqO9PsHPg&t=181s)
<div style="text-align: right"> $\square$ </div>

## Compute Fourier Transform for the Majority Function
We will demonstrate the process of computing the Fourier transform of the [majority function](https://404briannotfound.tech/views/MAT388/2020/post1.html#boolean-functions-example-4-are-the-majority-of-the-inputs-one) that we mentioned in the previous post. We will look at a 3-dimensional majority function.

**Step 1**: Calculate $\chi_{\left\{\emptyset \right\}}$, $\chi_{\left\{1\right\}}$, $\chi_{\left\{2\right\}}$, $\chi_{\left\{3\right\}}$, $\chi_{\left\{1,2\right\}}$, $\chi_{\left\{2,3\right\}}$, $\chi_{\left\{1,3\right\}}$, $\chi_{\left\{1,2,3\right\}}$

Recall that $\chi_{\left\{x_{1},x_{2},...,x_{n}\right\}}=x_{1}x_{2}...x_{n}$. To follow convention, we will be using ${-1,1}$ instead of ${0,1}$

| Maj |$x_{1}$|$x_{2}$|$x_{3}$| $x_{\emptyset}$ | $x_{\left\{1\right\}}$ | $x_{\left\{2\right\}}$ | $x_{\left\{3\right\}}$ | $x_{\left\{1,2\right\}}$ | $x_{\left\{1,3\right\}}$ | $x_{\left\{2,3\right\}}$ | $x_{\left\{1,2,3\right\}}$|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| -1 | -1 | -1 | -1 | 1 | -1 | -1 | -1 | 1 | 1 | 1 | -1 |
| -1 | 1 | -1 | -1 | 1 | 1 | -1 | -1 | -1 | -1 | 1 | 1 |
| -1 | -1 | 1 | -1 | 1 | -1 | 1 | -1 | -1 | 1 | -1 | 1 |
| -1 | -1 | -1 | 1 | 1 | -1 | -1 | 1 | 1 | -1 | -1 | 1 |
| 1 | 1 | 1 | -1 | 1 | 1 | 1 | -1 | 1 | -1 | -1 | -1 |
| 1 | -1 | 1 | 1 | 1 | -1 | 1 | 1 | -1 | -1 | 1 | -1 |
| 1 | 1 | -1 | 1 | 1 | 1 | -1 | 1 | -1 | 1 | -1 | -1 |
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

**Step 2**: Compute the **Fourier Coefficient** as follows:

$\widehat{Maj}(\left\{\emptyset \right\})=\langle{Maj, \chi_{\left\{\emptyset \right\}}}\rangle=E\left[Maj\cdot \chi_{\left\{\emptyset \right\}}\right]\\=((-1)(1)+(-1)(1)+(-1)(1)+(-1)(1)+(1)(1)+(1)(1)+(1)(1)+(1)(1))\cdot (0.5)^{3}=0$

$\widehat{Maj}(\left\{1 \right\})=\langle{Maj, \chi_{\left\{1 \right\}}}\rangle=E\left[Maj\cdot \chi_{\left\{1 \right\}}\right]\\=((-1)(-1)+(-1)(1)+(-1)(-1)+(-1)(-1)+(1)(1)+(1)(-1)+(1)(1)+(1)(1))\cdot (0.5)^{3}=\frac{1}{2}$

$\widehat{Maj}(\left\{2 \right\})=\langle{Maj, \chi_{\left\{2 \right\}}}\rangle=E\left[Maj\cdot \chi_{\left\{2 \right\}}\right]\\=((-1)(-1)+(-1)(-1)+(-1)(1)+(-1)(-1)+(1)(1)+(1)(1)+(1)(-1)+(1)(1))\cdot (0.5)^{3}=\frac{1}{2}$

Similarily, $\widehat{Maj}(\left\{3 \right\})=\frac{1}{2}$

$\widehat{Maj}(\left\{1,2 \right\})=\langle{Maj, \chi_{\left\{1,2 \right\}}}\rangle=E\left[Maj\cdot \chi_{\left\{1,2 \right\}}\right]=((-1)(1)+(-1)(-1)+(-1)(-1)+(-1)(1)+(1)(1)+(1)(-1)+(1)(-1)+(1)(1))\cdot (0.5)^{3}=0$

Similarily, $\widehat{Maj}(\left\{1,3 \right\})=\widehat{Maj}(\left\{2,3 \right\})=0$

And $\widehat{Maj}(\left\{1,2,3 \right\})=-\frac{1}{2}$

Therefore through Fourier transform and given all the Fourier Coefficient, we can express our Majority function in dimension three as a multilinewar function $f=\frac{x_{1}}{2}+\frac{x_{2}}{2}+\frac{x_{3}}{2}-\frac{x_{1}\cdot x_{2}\cdot x_{3}}{2}$. We can confirm the correctness of such function by plugging in $x_1,x_2,x_3$ and confirm the output.

**Some Notes and Interesting Facts**:

 - As long as we follow the above algorithm for finding the Fourier transform, our polynomial will always be multilinear.
 - Every Boolean function can be uniquely expressed as a multilinear polynomial. (Hopefully we can prove the uniqueness later on).
 - It seems like by adding up the square of each coefficient, the result will always be $1$. For example, for the majority function above, $(\frac{1}{2})^{2}+(\frac{1}{2})^{2}+(\frac{1}{2})^{2}+(-\frac{1}{2})^{2}=1$. I currently have no way to verify this yet, but it seems to work with every Fourier transform that I have tried so far and it reminds me of the formula for computing the distance in a space. I will try to find some supporting evidence, and hopefully readers can shed some lights on such observation as well.