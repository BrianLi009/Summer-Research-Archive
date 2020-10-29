Structure and Outline:
**This part should not be included in the actual blog**

Goals: Introduce Random Permutation from the fundamental, but also apply it in the context of card shuffling.

Ideas: I want to start by introduce each ideas in random permutation (expected length )

Post Structure:

1. Introduce what Random Permutation is and how it related to Card Shuffling
2. Define length of cycles and compute it in the context of shuffling a deck of cards
3. Define derangement and relate it to card shuffling
4. Conclusion

**Actual Blog Starts Here**

## What is a Permutation?

A random permutation is a random ordering of a set of elements.

**Example**: Let the set be $A=\left\{1,2,3,4,5\right\}$, we can generate random permutations such as $A_{1}=\left\{2,3,4,5,1\right\}$, $A_{2}=\left\{3,2,4,5,1\right\}$, $...$ We will not have enough space to list out all of them, but we can calculate the total number of permutation for $A$ with length of $5$. In fact, we can generalize a theorem that applies to a set with any length.

**Theorem 1.0**: For a set $A$ with $n$ distinct elements, the total number of permutations is equal to $n!$.

**Proof**: Since all elements in the set $A$ are distinctive, there will be no repetition. Thus intuitively, we have $n$ elements that could potentially fill up the first spot. After this we have $(n-1)$ elements left to potentially fill up the second spot. By this logical, the total number of ways to construct such permutation is $n\cdot (n-1) \cdot (n-2) \cdot ... \cdot (2) \cdot (1) = n!$

<div style="text-align: right"> $\square$ </div>

**Application 1.0**: We will give an example in the context of card shuffling. To keep it simple, let us say we have four Aces with different suits. They are $A \clubsuit$, $A{\color{red} \heartsuit}$, $A \spadesuit$, $A {\color{red} \diamondsuit}$. According to theorem 1, there exist $4! = 24$ ways to shuffle them. Now let us think about this in the context of an entire deck. An entire deck has 52 distinct cards in total (excluding jokers), thus we can compute the total permutation to be $52! = 8.06581751709439^{67}$. To put that in perspective, according to an article from [McGill University](https://mcgill.ca/oss/article/did-you-know-infographics/there-are-more-ways-arrange-deck-cards-there-are-atoms-earth), even if someone could rearrange a deck of cards every second of the universe’s total existence, the universe would end before they could reach one billionth of the way to finding a repeat. Let us confirm this conclusion. Our universe has existed for nearly $14$ billion years. There are multiple theories predicting the end of the universe, for instance, the theory of [Heat Death](https://en.wikipedia.org/wiki/Heat_death_of_the_universe) predicted that one hundred quintillion ($10^{20}$) years from now, most of these objects will be swallowed up by the supermassive black holes at the heart of galaxies. So the ratio between shuffling 52 cards and finding a match and the approximate age of the universe would be $\frac{1.4 \cdot 10^{13} + 10^{20}}{52!} \approx 1.25^{-48}$, which is much less than one billionth.
 
## What is a Derangement?
**Definition**: A derangement is a permutation with no fixed points, such that no element is mapped to itself, that is, $\sigma (i) \neq i\in \left\{1,2,3,...,n\right\}$.

**Example 3.0**: Let $S=\left\{1,2,3\right\}$, the derangement of $S$ would be $S=\left\{2,3,1\right\}$ and $S=\left\{3,1,2\right\}$.

**Example 3.1**: Let $S=\left\{1,2,3,4\right\}$, the derangement of $S$ would be $S=\left\{2,1,4,3\right\}$, $S=\left\{2,3,4,1\right\}$, $S=\left\{2,4,1,3\right\}$, $S=\left\{3,1,4,2\right\}$, $S=\left\{3,4,1,2\right\}$, $S=\left\{3,4,2,1\right\}$, $S=\left\{4,1,2,3\right\}$, $S=\left\{4,3,1,2\right\}$, $S=\left\{4,3,2,1\right\}$.

**Theorem 3.0**: The function giving the number of distinct derangement on $n$ elements is called the subfactorial $!n$ and is equal to $!n=n!\sum_{k=0}^n\frac{(-1)^{k}}{k!}$.

**Proof**: Let the set of permutations of n objects be $S_{n}$, its number of derangments be $D_{n}$, and let $A_{i}$ be the subset of $S_{n}$ such that the $i$th object is fixed (ends up in its origninal position). Then $\mid A_{1}\cup A_{2}\cup ... \cup A_{n} \mid$ represents the number of permutations where at least one object is fixed. Thus the number of permutation with no object fixed is $n! - \mid A_{1}\cup A_{2}\cup ... \cup A_{n} \mid$ (recall that total number of permutation is $n!$). Now we need to compute $\mid A_{1}\cup A_{2}\cup ... \cup A_{n} \mid$ using [principle of inclusion-exclusion](https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle), essentially the idea is to eliminate overlapping at the intersection of multiple sets.


 - **Exactly one object is fixed**: After fixing one object, we have $n-1$ objects left to be permutated in $(n-1)!$ possible ways. Thus we have $n \cdot (n-1)! = n!$ number of ways to do so.

 - **Exactly two objects are fixed**: After fixing two objects in ${n}\choose{2}$ ways, we have $n-2$ objects left to be permutated in $(n-2)!$ possible ways. Thus we have ${{n}\choose{2}} \cdot(n-2)! = \frac{n!}{2!}$ number of ways to do so.
 
 - **Exactly three objects are fixed**: After fixing three objects in ${n}\choose{3}$ ways, we have $n-2$ objects left to be permutated in $(n-3)!$ possible ways. Thus we have ${{n}\choose{3}} \cdot (n-3)! = \frac{n!}{3!}$ number of ways to do so
 
 - ... As all objects are fixed, we are left with only one way to accoplish that.
 
 Therefore by principle of inclusion and exclusion, we can conclude that $\mid A_{1}\cup A_{2}\cup ... \cup A_{n} \mid = n! - \frac{n!}{2!} + \frac{n!}{3!} - ... + (-1)^{n+1} = n! \left[ 1-\frac{1}{2!}+\frac{1}{3!}-...+(-1)^{n+1} \frac{1}{n!}\right] = n!\sum_{k=1}^n\frac{(-1)^{k+1}}{k!}$. Therefore the number of derangement in $S_{n}$ is:
 
 $D_{n} = n! -  n!\sum_{k=1}^n\frac{(-1)^{k+1}}{k!} = n!\sum_{k=0}^n\frac{(-1)^{k}}{k!}$

<div style="text-align: right"> $\square$ </div>



**Application**: There is no magic trick that is solely based on the idea of derangement, but it appears everywhere in cards. For instance, let us say you and your friend each has a randomly-shuffled deck of cards. If you two compare the card one at a time and check if it is the same card, what is the probability that there is no match?


 - This question is equivalent to asking "what is the probability of having a derangement for a permutation of length 52?" We can apply the equation to obtain the total number of derangement when $n=52$, and divide that by the number of total permutation when $n=52$, we obtain $P(\text{derangement}) = \frac{!52}{52!} = \frac{52!\sum_{k=0}^{52}\frac{(-1)^{k}}{k!}}{52!}=\sum_{k=0}^{52}\frac{(-1)^{k}}{k!}\approx 0.368$. One interesting fact is that $\lim_{n\rightarrow \infty}\frac{!n}{n!} = \frac{1}{e} \approx 0.3679$.




