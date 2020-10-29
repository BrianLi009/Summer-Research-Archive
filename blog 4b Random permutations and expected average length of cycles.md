## What is a Cycle?

**Definition**: An **m-cycle** in $S_{n}$ is a string of integers of length $m$, written $(a_{1}a_{2} . . . a_{m})$, where $a_{i} \in {1, 2, . . . , n}$, that corresponds to the permutation in $S_{n}$ that sends $a_{i}$ to $a_{i+1}$ for $1 \leq i \leq m−1$, $a_{m}$ to $a_{1}$, and fixes all the other integers in ${1, 2, . . . , n}$ that do not appear in the cycle. We say $m$ is the length of the cycle. One can think of an m-cycle as follows;

<center><img src='https://i.ibb.co/6F1D1wc/1.png' width = 50% title='m-cycle'></center>


**Example 2.0**: Let $S=\left\{1,2,3,4\right\}$, the permutation $\left(2\space 3\space 4\space 1\right)$ sends $1\rightarrow 2$, $2\rightarrow 3$, $3\rightarrow 4$, and $4\rightarrow 1$. Such permutation has one cycle of length $4$. The cycle is $(1 \space 2\space 3\space 4)$.

**Example 2.1**: Let $S=\left\{1,2,3,4\right\}$, the permutation $\left(2\space 4\space 3\space 1\right)$ sends $1\rightarrow 2$, $2\rightarrow 4$, and $4\rightarrow 1$. As we can see, the position of $3$ remains unchanged, thus $3$ is a **fixed point**. We express this permutation as $(1\space 2\space 4)(3)$, where it has one cycle of length $3$ and one cycle of length $1$ (We count a fixed point as a cycle as well).

**Application 2.0**: A "[perfect shuffle](https://en.wikipedia.org/wiki/Faro_shuffle)" is performed by splitting a deck of cards into exactly two halves and interlocking the cards so that the cards from the $2$ piles alternate into the final pile. Let's say we have ordered deck $(1,2,3,4,...,52)$ We split it into deck $A$ and deck $B$ with both 26 cards: $A=(1,2,3,4,...,25,26)$, $B=(27,28,29,30,...,51,52)$. Now we have two ways to do a perfect shuffle:

1. The top card from B ending up on the top in the shuffled deck (Faro In Shuffle)
2. The top card from A ending up on the top in the shuffled deck (Faro Out Shuffle)

Surprisingly, these two methods yield very different outcomes. By applying Out Shuffle, we need to perform 52 identical shuffles to reach the starting position. However, if we apply Out Shuffle, we would only need 8 shuffles to accomplish the same goal. Let us examine these two shuffle method:

 - By applying Fro In Shuffle (The top card from B ending up on the top in the shuffled deck), after one shuffle, we have:
 ```
(27 1 28 2 29 3 30 4 31 5 32 6 33 7 34 8 35 9 36 10 37 11 38 12 39 13 40 14 41 15 42 16 43 17 44 18 45 19 46 20 47 21 48 22 49 23 50 24 51 25 52 26)
```
The cycle in this case is: 
```
(1 27 40 20 10 5 29 41 47 50 25 39 46 23 38 19 36 18 9 31 42 21 37 45 49 51 52 26 13 33 43 48 24 12 6 3 28 14 7 30 15 34 17 35 44 22 11 32 16 8 4 2)
```
As we can see, we have one giant cycle with length 52. This means that to get card 1 back in the top position, it has to travel through each of the other positions in the cycle. Thus we have to repeat the shuffle 52 times to get each of the cards back to their starting positions.

 - By applying Faro Out Shuffle (The top card from A ending up on the top in the shuffled deck), after one shuffle, we have:
 ```
 (1 27 2 28 3 29 4 30 5 31 6 32 7 33 8 34 9 35 10 36 11 37 12 38 13 39 14 40 15 41 16 42 17 43 18 44 19 45 20 46 21 47 22 48 23 49 24 50 25 51 26 52)
 ```
 The cycle in this case is:
 ```
 (1) (2 27 14 33 17 9 5 3) (4 28 40 46 49 25 13 7) (6 29 15 8 30 41 21 11) (10 31 16 34 43 22 37 19) (12 32 42 47 24 38 45 23) (18 35) (20 36 44 48 50 51 26 39) (52)
 ```
 We can see that there are two cycles of length 1, one cycle of length 2 and six cycles of length 8. Since $gcd(1,2,8)=8$. Therefore, to reach the starting position, we only need to perform 8 shuffles of the top card top kind.

**Theorem 2.0**: The expected length (average length) of the largest cycle in a random permutation of an $n$-element set as $n\rightarrow \infty$ is $\frac{n}{ln(n)}$.

**Experiement**: We currently do not have a formal proof for theorem 2.0, so instead we attempt to verify the theorem with the help of a Python program. First, we will need a function that output all the cycles in a permutation:
```
def get_cycles(ordered_set, random_comb):
    """this function list out the cycles in a permutation"""
    """my logic:
            outer loop:
            inner loop:
                find what the current item goes to
                add that to the cycle
                set "current item" to that
                stop when you get to the first item
            add a list containing those items to the list of cycles
            start again with an item you haven't used yet
            keep going until the lists are empty (or only have one item)"""
    perm = [ordered_set, random_comb]
    cycle_list = []
    possible_beginnings= perm[0].copy()
    while True:
        if len(possible_beginnings)<2:
            break
        start = possible_beginnings[0]
        current = start
        new = perm[1][perm[0].index(start)]
        possible_beginnings.remove(start)
        if start == new:
            continue
        cycle = [start,new]
        current = new
        while True:
            possible_beginnings.remove(current)
            current = perm[1][perm[0].index(current)]
            if current == start:
                break
            cycle.append(current)
        cycle_list.append(cycle)
    return cycle_list + [get_fixed_pts(ordered_set, random_comb)]
```

Using the above function we can produce cycles of permutations such as:
```
get_cycles([1,2,3,4],[2,4,3,1])
>>> [[1, 2, 4], [3]]
```

Using the above function, let us first graph a plot of "number of cycles vs. length of cycles" with $n=100$ for 10000 trials:

<img src='https://i.ibb.co/VH7DMhm/1.png' title='Number of Cycles vs. Length of Cycles'>

Having data like this, it becomes quite easy to compute the average, and even the mean and mode of cycle length. After running some functions, we achieve the following results for $n=100$:

```
average = 20.68594596830913
median = 9.0
mode = 2
```
Notice that average length = $20.68594596830913 \approx \frac{100}{ln(100)} = 21.71$. It is off by approximately one maybe due to the fact that we only ran 10000 trials. Our next step is to run the same function for different $n$ value. Now we can compute the expected length of the biggest cycle in a random permutation as $n$ increases and plot the graph in comparison to $\frac{n}{ln(n)}$: 
<img src='https://i.ibb.co/MpNhHQy/3.png' title='Average of Cycles vs. Length n'>
Each scatter point is the average cycle length for permutation with length $n$ after 1000 trials. To make the graph readable, only $n$s that are multiples of $10$ are computed. The red curve is the function $\frac{n}{ln(n)}$. We can see that the scatter poitns roughly follows the function but seems to be "bounded below" the function. Anyhow, we will need further mathematical investigation to confirm theorem 2.0.

## Conclusion and Extension
In this post, we have discussed random permutation, cycles, derangment and how they might be connected to card tricks and shuffling. We would like to make two more hypothesis here:

**Hypothesis 1**: The median of length of the largest cycle in a random permutation of an n-element set is ... (TBD)****

**Hypothesis 2**: The mode of the largest cycle in a random permutation of an n-element set is $2$.

These two hypothesis are being made only from an experimental point of view, meaning that it is deducted from observation using computer programs. However, we have not figured out ways to mathematically prove the hypothesis and hopefully readers can contribute to such process.