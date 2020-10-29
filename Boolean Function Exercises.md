[Link to Exercises](http://www.contrib.andrew.cmu.edu/~ryanod/?p=301#exgolomb)

Exercise 10:

a. Show that every $f : \{\mathsf{False},\mathsf{True}\}^n \to \{\mathsf{False},\mathsf{True}\}$ can be represented as a multilinear polynomial $\begin{equation} \label{eqn:zotzo-poly} q(x) = \sum_{S \subseteq [n]} c_S \prod_{i \in S} x_i, \end{equation}$


1. Thoughts: we will start with an arbitrary $f$ and shows that by using ``the interpolation method'' we can map $\{0,1\}^n \to \{0,1\}$. Let us define a n-dimensional input denoted as $A_{n}$, where $A_{n} = (a_1, \dots, a_n) \in \{0,1\}^n$

2. We could generate in total $2^{n}$ inputs, since each bit has to be either 0 or 1. By applying the method of interpolation, for each point $a_{i}$, where $1\leq i \leq n$, we obtain the characteristic function $1_{\{a\}}(x) = \left(\tfrac{1+a_1x_1}{2}\right)\left(\tfrac{1+a_2x_2}{2}\right) \cdots \left(\tfrac{1+a_nx_n}{2}\right)$. Thus we obtain $f(x) = \sum_{a \in \{0,1\}^n} f(a) 1_{\{a\}}(x)$ after adding up all the inputs.

3. Since the characteristics polynomial only has degress one for $x_{i}$ where $1\leq i \leq n$, the interpolation will always produce a multilinear polynomial. Another way we could look at it is that since $x_{i} \in \left\{0,1\right\}$ and $0^{2}=0, 1^{2}=1$, all degrees higher than 1 can be expressed with a variable with degree $1$ instead. (same argument applies when $a \in \{-1,1\}$).
<div style="text-align: right"> $\square$ </div>

b. Showing its uniqueness (using some theorems that is already mentioned in the blog post)

1. During our blog post, we have discussed that $\chi_{S}(x_{1},x_{2},...,x_{n})= \prod_{i\in S}x_{i}$. Essentially, every function $f:\{-1, 1\}^{n}\rightarrow \mathbb{R}$ is a linear combination of $\chi_{S}$. Since the total number of $\chi_{S}$ function is $2^{n}=dim(V)$, $\chi_{S}$ is a linearly independent basis for V. Independence implies solution is trivial and unique.

<div style="text-align: right"> $\square$ </div>

c. Show that all coefficient will be in the range $[-2^n, 2^n]$.
1. For a fourier coefficient, $c_{S}=\langle f,g \rangle=E_{x\sim \left\{-1,1\right\}^{n}}(f(x)g(x))$. Since $-1 \leq f(x) \leq 1$ and $-1 \leq g(x) \leq 1$, $-1 \leq f(x)g(x) \leq 1$. Since in total we have $2^n$ inner product as stated above in section b, we conclude that $c_{S}$ will bein the range $[-2^n, 2^n]$.
<div style="text-align: right"> $\square$ </div>

d. 
