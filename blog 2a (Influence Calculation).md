## Calculation and Proof for The Influence of Variables on Boolean Functions

During [last week's post](https://404briannotfound.tech/views/MAT388/2020/post1.html#what-is-a-boolean-function), we investigated different Boolean functions and approximated their total influence using Python scripts. Today we will be confirming these results by calculating the influence of these functions using a mathematical approach.\
My approach is to separate potentially influential bits, divide them into different cases and calculate each event's probability then add them up. I am certain that there should be other ways to calculate the total influence but for me this is the most intuitive approach.

### Boolean Functions Example 1: Randomly Generate

A random Boolean functions utilize a computer program to generate a random output for each inputs. To see an example, please refer to the [previous post](https://404briannotfound.tech/views/MAT388/2020/post1.html#boolean-functions-example-1-randomly-generate).

**Theorem 1**: If $f$ is the random Boolean function, then $ \mathbf{I}[f]=0.5n $.

#### Proof

We will calculate the influence of an individual bit first. Since all outputs are random, once we flip the bit, the chances of us getting a different output would be $ 1/2 $. To further expand on this idea, the only two situations that this would happen is that:

$$[f({\boldsymbol{x}}) = 0 \wedge f({\boldsymbol{x}}^{\oplus i})=1]\vee[f({\boldsymbol{x}}) = 1 \wedge f({\boldsymbol{x}}^{\oplus i})=0]$$
Thus individual influence would be:
$$\mathbf{Inf}_i[f]=\mathop{\bf Pr}[[f({\boldsymbol{x}}) = 0 \wedge f({\boldsymbol{x}}^{\oplus i})=1]\vee[f({\boldsymbol{x}}) = 1 \wedge f({\boldsymbol{x}}^{\oplus i})=0]]$$
which is equivalent to:
$$\mathbf{Inf}_i[f] =\mathop{\bf Pr}[f({\boldsymbol{x}}) = 0 \wedge f({\boldsymbol{x}}^{\oplus i})=1]+\mathop{\bf Pr}[f({\boldsymbol{x}}) = 1 \wedge f({\boldsymbol{x}}^{\oplus i})=0]$$
Since each individual event is independent:
$$\mathbf{Inf}_i[f] = {\bf Pr}[f({\boldsymbol{x}}) = 0] \cdot {\bf Pr}[f({\boldsymbol{x}}^{\oplus i}) = 1]+{\bf Pr}[f({\boldsymbol{x}}) = 1] \cdot {\bf Pr}[f({\boldsymbol{x}}^{\oplus i}) = 0]$$
And we obtain the individual influence:
$$=0.5 \cdot 0.5 + 0.5 \cdot 0.5 = 0.5$$

Now since each bit in a random Boolean function have the same influence on our outcome, their individual influence are equal. Thus, we can express **the total influence for a random Boolean function** as:
$$\mathbf{I}[f]=0.5n$$

### Boolean Functions Example 2: Is everything equal to one?
This is a function where the output will be 0 unless all input bits are 1, the [previous post](https://404briannotfound.tech/views/MAT388/2020/post1.html#boolean-functions-example-2-is-everything-equal-to-one) provided examples as well.

**Theorem 2**: If $f$ is the AND Boolean function, then $ \mathbf{I}[f]=\frac{n}{2^{n-1}} $.


#### Proof
Example 2 is a bit more complicated so let us divide the calculation into cases:

1. We have "0" in the ith bit and "1" everywhere else. If we flipped the "0", the output turns from 0 to 1 since all input becomes 1.
2. We have 1 for every bit of the input, and we flip any ith bit, the output turns from 1 to 0.
Thus individual influence would be:
$$\mathbf{Inf}_i[f]=\mathop{\bf Pr}[x_{i}\neq0\wedge(\forall a\neq i, x_{a}=1)]+\mathop{\bf Pr}[\forall a\leq n, x_{a}=1]$$
Due to properties of individual events we have:
$$\mathbf{Inf}_i[f]=\left(\frac{1}{2}\right) \cdot \left(\frac{1}{2}\right)^{n-1}+\left(\frac{1}{2}\right)^{n}$$
Thus we obtain the individual influence:
$$\mathbf{Inf}_i[f]=2\left(\frac{1}{2}\right)^{n}$$

Now since each bit in this Boolean function have the same influence on our outcome, their individual influence are equal. Thus, we can express **the total influence for such functions** as:
$$\mathbf{I}[f]=2\left(\frac{1}{2}\right)^{n} \cdot n=\frac{n}{2^{n-1}}$$
If we would want to graph this as a function, it will match the Python plot.

### Boolean Functions Example 3: Even or Odd?
Now we will investigate the Boolean function that add up all entries in mod 2. Essentially this is equivalent to identifying whether the sum is even or odd. Two examples are written in the [previous post]

**Theorem 3**: If $f$ is the parity Boolean function, then $ \mathbf{I}[f]=n $.

#### Justification
This Boolean function is a bit special due to the fact that no matter which bit we changed, it will affect the output regardless. The reason is that by changing one bit, the sum of our input either increase or decrease by 1. Therefore, an even sum will be odd and an odd sum will be even. Thus the output will turn from 1 to 0 or 0 to 1.

By this argument, the probability of the outcome being affected by a flipped bit is 100%. Therefore, we can conclude that: $$\mathbf{Inf}_i[f]=1$$
Thus we can calculate the total influence to be: $$\mathbf{I}[f]=n$$

### Boolean Functions Example 4: Are the majority of the inputs one?
For this example, if majority of the input is 1, the output would be 1. Otherwise the output would be 0, including the case where the number of 1s and 0s are equal. Examples are shown in the [previous post](https://404briannotfound.tech/views/MAT388/2020/post1.html#boolean-functions-example-4-are-the-majority-of-the-inputs-one):

**Theorem 4**: If $f$ is the majority Boolean function, then $ \mathbf{I}[f]=\frac{n{n-1\choose \frac{n-1}{2}}}{2^{n-1}} $ when n is odd, $ \mathbf{I}[f]=\frac{n{n-1\choose \frac{n}{2}}}{2^{n-1}} $ when n is even.

We can use [Stirling's approximation](https://en.wikipedia.org/wiki/Stirling%27s_approximation#Mentally_estimating_central_effect_in_the_binomial_distribution) to simplify our result. That is, we use the approximation $ \binom{n}{\frac{n}{2}} \sim \frac{2^{n}}{\sqrt{\pi n/2}} $.

Thus we obtain when n is odd, $ \mathbf{I}[f]=\frac{n{n-1\choose \frac{n-1}{2}}}{2^{n-1}} \approx \sqrt{\frac{2}{\pi}} \cdot \sqrt{\frac{n^{2}}{n-1}} = 0.79788\sqrt{\frac{n^{2}}{n-1}}$. If n is even, $ \mathbf{I}[f]=\frac{n{n-1\choose \frac{n}{2}}}{2^{n-1}} \approx \sqrt{\frac{2}{\pi}} \cdot \sqrt{n} = 0.79788\sqrt{n}$
#### Justification
We would like to divide the calculation into two cases based on the Boolean function's dimension's parity (even or odd). Nevertheless, before that we would like to clarify some notations that will come up below:

$$n_{0}:\text{number of 0 in the Boolean input}$$
$$n_{1}:\text{number of 1 in the Boolean input}$$

#### Case 1: Odd dimension
When n is odd, we have two cases where the outcome could be affected:
$$\text{Case 1: }\space n_{1}-n_{0}=1 \wedge x_{i}=1 \space \text{example: 11100}$$
$$\text{Case 1: }\space n_{0}-n_{0}=1 \wedge x_{i}=0 \space \text{example: 00011}$$

Due to properties of independent event:
$$\mathbf{Inf}_i[f]=\mathop{\bf Pr}[x_{i}=1] \cdot \mathop{\bf Pr}[n_{1}-n_{0}=1]+\mathop{\bf Pr}[x_{i}=0] \cdot \mathop{\bf Pr}[n_{0}-n_{1}=1]$$
It is interesting to note that case 1 and case 2 are symmetric with equal properties. Moreover, besides the ith digit that is flipped, the rest of the input has an even length and equal number of 0 and 1, thus:
$$\mathbf{Inf}_i[f]=2 \cdot \left(\frac{1}{2}\right) \cdot {\bf Pr}\left[n_{1}=n_{0}=\frac{n-1}{2}\right]$$

To measure the probaility that there exists $\frac{n-1}{2}$ "0"s, we will use combination to express the total number of ways for that to happen:
$$\mathbf{Inf}_i[f]=2 \cdot \left[\left(\frac{1}{2}\right) \cdot \frac{{n-1\choose \frac{n-1}{2}}}{2^{n-1}}\right]$$

After simplifying, we obtain:
$$\mathbf{Inf}_i[f]=\frac{{n-1\choose \frac{n-1}{2}}}{2^{n-1}}$$

Therefore the total influence:
$$\mathbf{I}[f]=\frac{n{n-1\choose \frac{n-1}{2}}}{2^{n-1}}$$

#### Case 2: Even dimension
When $ n $ is even, we have two cases where the outcome could be affected:
$$\text{Case 1: }\space n_{1}-n_{0}=0 \wedge x_{i}=0 \space \text{example: 111000}$$
$$\text{Case 1: }\space n_{1}-n_{0}=2 \wedge x_{i}=1 \space \text{example: 001111}$$

Due to properties of independent event:
$$\mathbf{Inf}_i[f]=\mathop{\bf Pr}[x_{i}=0] \cdot \mathop{\bf Pr}[n_{1}-n_{0}=0]+\mathop{\bf Pr}[x_{i}=1] \cdot \mathop{\bf Pr}[n_{1}-n_{0}=2]$$

Notice that in case 1, after isolating the flipped bits "0", we have one more "1" than "0". In case 2, after isolating the flipped bits(1), we have one more "1" than "0". Again, these two cases are symmetric. In both of these cases, $n_{1} = n/2$, therefore:

$$\mathbf{Inf}_i[f]=2 \cdot \left(\frac{1}{2}\right) \cdot {\bf Pr}\left[n_{1}=\frac{n}{2}\right]$$

Since the flipped bit is chosen at this point, all other "1" exists in the string with length $n-1$:
$$\mathbf{Inf}_i[f]=\frac{{n-1\choose \frac{n}{2}}}{2^{n-1}}$$

Hence the total influence:
$$\mathbf{I}[f]=\frac{n{n-1\choose \frac{n}{2}}}{2^{n-1}}$$

Notice that if we plug in two consecutives $ n $ (one is even and one is odd) and compare them, we will get the same total influence. This justifies the "Stairs" behaviors of our graph and is something quite interesting to look into.

Now we have calculated and confirmed the accuracy of our plot from the last post. One interesting property of influence is that there is no particular formula to apply during calculation. My approach is solely based on dividing and conquering cases then apply fundamental probability theories. Boolean functions have been widely used in fields like computer science, cryptography and logic. We will definitely discuss more on this topic in some future posts.

