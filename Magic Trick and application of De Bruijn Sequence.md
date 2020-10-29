**This part should not be included in the actual blog**

Goals: Demonstrate the trick and allow readers to perform the trick by themselves simply based on this post. Introduce the idea behind it and the concept of de Bruijn sequence. End the blog with some generalization.

Note: I will be following a similar format to "A Magic Trick Leads to an Identity: Some Induction Fun" to practice my writing

Post Structure:

1. Talk about how the trick looks like from audiences' perspective

2. Talk about how the trick looks like from performer's perspective

3. Introduce de Bruijn and show how it is applied in this trick (theorems, proofs, etc)

4. Generalization of binary de Bruijn sequence and how it could apply to other tricks or games.

**Actual Blog Starts Here**

## A Magic Trick for Five Participants

This magic trick is first introduced in ["Magical Mathematics: The Mathematical Ideas That Animate Great Magic Tricks"](https://press.princeton.edu/books/hardcover/9780691151649/magical-mathematics) by [Persi Diaconis](https://en.wikipedia.org/wiki/Persi_Diaconis) and [Ron Graham](https://en.wikipedia.org/wiki/Ronald_Graham).

Let us begin by introducing this trick from the audiences' perspective. A magician starts the trick by asking five random volunteers to participate. The deck will be passed between the five volunteers and each volunteer will cut the deck. When the deck is cut by the last(5th) volunteer, the magician asks the 5th volunteer to take the top card then pass it back to the 4th volunteer. The 4th volunteer will repeat the same process until every volunteer has a card in their hand. The magician states that he can guess all five cards if given some additional information about the volunteers, then he or she asks, "Would all of you with a red card please stand up?" Volunteers holding a red card would then stand up accordingly. The magician proceeds to name all five cards correctly, including the number and the suit.

Now we will describe the same magic trick from the magician's perspective. The deck is pre-arranged with some very special properties and only has 32 cards in it, which we will discuss in detail below. When volunteers cut the deck, these properties are preserved. After all five volunteers have cut the deck and received their card, the magician starts to ask multiple questions. However, the only important question is that "Who has the red card?". The magician will utilize the special properties of the deck: these 52 cards are arranged in an order such that **the sequence of red and black cards amongst five consecutive cards uniquely identify the five cards**. Therefore by knowing who has the red card, the magician can tell exactly what these 5 cards are since it exist uniquely in the deck. To explain why this is possible, we hereby introduce the idea of a De Bruijn sequence. 

## De Bruijn Sequence
**Definition**: A de Bruijn sequence is a cyclic sequence of a given alphabet $A$ with size $k$, for which every possible subsequence of length $n$ in $A$ appears as a sequence of consecutive characters exactly once. We say such sequences have property $B(k, n)$. 

**Example 1.0:**
Let us produce the de Bruijn sequence for $B(2, 2)$, where $k=n=2$. Since the alphabet has size $2$, we could define the alphbet $A=\{0,1\}$. Since $n=2$, the possible sequences are $(0,0), (0,1), (1,0), (1,1)$. Therefore we can generate the de Bruijn sequence $0011$. Notice that $0011$ contains $00$, $01$, $11$, and $10$ as it wraps around the sequence.
 
**Example 1.1:**
Let us produce the de Bruijn sequence for $B(2, 5)$, where $k=2, n=5$. Since the alphabet has size $2$, we could define the alphbet $A=\{0,1\}$. Since $n=5$, we have in total $2^5=32$ possible distinct sequences such as $(0,0,0,0,0), (0,0,0,0,1)...$. By using the assitance of a [generator](http://www.hakank.org/comb/debruijn.cgi), we can generate one of the de Bruijn sequences $00000111011010111110011000101001$. Such cyclic sequence contains all $32$ sequences.

**Application in the magic trick:**
In our magic trick, we have $5$ volunteers and $2$ elements in the alphabet (red and black), thus $k=2, n=5$ and we have the case $B(2,5)$. We know it is possible to construct a de Bruijn sequence with a deck of cards since we only have $32$ possible distinct sequences while we have 52 cards (see example 1.1). Recall that the goal is to construct a de Bruijn sequence where the sequence of red and black cards amongst five consecutive cards uniquely identify the five cards. Here is how:

**Step 1:** Select $32$ cards from a normal deck of 52. The number on these selected cards does not matter, but make sure you selected $16$ red cards and $16$ black cards.

**Step 2:** Now we need to construct the de Bruijn deck. Thanks to example 1.1, we have already obtained such sequence $00000111011010111110011000101001$. Now let us assign black(B) to be $0$, and ${\color{red}red(R)}$ to be $1$. For example, a sequence like $01001$ can now be expressed as $B{\color{red}R}BB{\color{red}R}$. Therefore we can translate the whole sequence into $BBBBB{\color{red}R}{\color{red}R}{\color{red}R}B{\color{red}R}{\color{red}R}B{\color{red}R}B{\color{red}R}{\color{red}R}{\color{red}R}{\color{red}R}{\color{red}R}BB{\color{red}R}{\color{red}R}BBB{\color{red}R}B{\color{red}R}BB{\color{red}R}$. 

I have randomly picked $32$ cards that satisfy those criteria:

$2{\spadesuit}$ $8{\spadesuit}$ $J{\spadesuit}$ $6{\spadesuit}$ $A{\spadesuit}$ $2{\color{red} \diamondsuit}$ $2{\color{red} \heartsuit}$ $3{\color{red} \heartsuit}$ $4{\clubsuit}$ $7{\color{red} \heartsuit}$ $J{\color{red} \diamondsuit}$ $7{\spadesuit}$ $Q{\color{red} \heartsuit}$ $Q{\spadesuit}$ $7{\color{red} \diamondsuit}$ $K{\color{red} \heartsuit}$ $5{\color{red} \diamondsuit}$ $K{\color{red} \diamondsuit}$ $4{\color{red} \diamondsuit}$ $10{\clubsuit}$ $7{\clubsuit}$ $4{\color{red} \heartsuit}$ $6{\color{red} \diamondsuit}$ $3{\clubsuit}$ $9{\clubsuit}$ $6{\clubsuit}$ $5{\color{red} \heartsuit}$ $10{\spadesuit}$ $9{\color{red} \diamondsuit}$ $3{\spadesuit}$ $Q{\clubsuit}$ $8{\color{red} \heartsuit}$

**Step 3**: Get ready to perform your trick! You can either memorize the order, or prepare a small cheat sheet. Here is a sample cheat sheet that I have provided for you:
| Color Order  | Corresponding Cards  |
| :------------: |:---------------:|
| $BBBBB$      | $2{\spadesuit}$ $8{\spadesuit}$ $J{\spadesuit}$ $6{\spadesuit}$ $A{\spadesuit}$  |
| $BBBB{\color{red}R}$      |    $8{\spadesuit}$ $J{\spadesuit}$ $6{\spadesuit}$ $A{\spadesuit}$ $2{\color{red} \diamondsuit}$     |
| $BBB{\color{red}R}{\color{red}R}$ |    $J{\spadesuit}$ $6{\spadesuit}$ $A{\spadesuit}$ $2{\color{red} \diamondsuit}$ $2{\color{red} \heartsuit}$     |
| $BB{\color{red}R}{\color{red}R}{\color{red}R}$ |  $6{\spadesuit}$ $A{\spadesuit}$ $2{\color{red} \diamondsuit}$ $2{\color{red} \heartsuit}$ $3{\color{red} \heartsuit}$  |
| $B{\color{red}R}{\color{red}R}{\color{red}R}B$|  $A{\spadesuit}$ $2{\color{red} \diamondsuit}$ $2{\color{red} \heartsuit}$ $3{\color{red} \heartsuit}$ $4{\clubsuit}$  |
| ${\color{red}R}{\color{red}R}{\color{red}R}B{\color{red}R}$ |  $2{\color{red} \diamondsuit}$ $2{\color{red} \heartsuit}$ $3{\color{red} \heartsuit}$ $4{\clubsuit}$ $7{\color{red} \heartsuit}$  |
| ${\color{red}R}{\color{red}R}B{\color{red}R}{\color{red}R}$ |  $2{\color{red} \heartsuit}$ $3{\color{red} \heartsuit}$ $4{\clubsuit}$ $7{\color{red} \heartsuit}$ $J{\color{red} \diamondsuit}$  |
| ${\color{red}R}B{\color{red}R}{\color{red}R}B$ |  $3{\color{red} \heartsuit}$ $4{\clubsuit}$ $7{\color{red} \heartsuit}$ $J{\color{red} \diamondsuit}$ $7{\spadesuit}$   |
| $B{\color{red}R}{\color{red}R}B{\color{red}R}$ |  $4{\clubsuit}$ $7{\color{red} \heartsuit}$ $J{\color{red} \diamondsuit}$ $7{\spadesuit}$ $Q{\color{red} \heartsuit}$   |
| ${\color{red}R}{\color{red}R}B{\color{red}R}B$ |  $7{\color{red} \heartsuit}$ $J{\color{red} \diamondsuit}$ $7{\spadesuit}$ $Q{\color{red} \heartsuit}$ $Q{\spadesuit}$   |
| ${\color{red}R}B{\color{red}R}B{\color{red}R}$ |  $J{\color{red} \diamondsuit}$ $7{\spadesuit}$ $Q{\color{red} \heartsuit}$ $Q{\spadesuit}$ $7{\color{red} \diamondsuit}$   |
| $B{\color{red}R}B{\color{red}R}{\color{red}R}$ |  $7{\spadesuit}$ $Q{\color{red} \heartsuit}$ $Q{\spadesuit}$ $7{\color{red} \diamondsuit}$ $K{\color{red} \heartsuit}$   |
| ${\color{red}R}B{\color{red}R}{\color{red}R}{\color{red}R}$|  $Q{\color{red} \heartsuit}$ $Q{\spadesuit}$ $7{\color{red} \diamondsuit}$ $K{\color{red} \heartsuit}$ $5{\color{red} \diamondsuit}$   |
| $B{\color{red}R}{\color{red}R}{\color{red}R}{\color{red}R}$|  $Q{\spadesuit}$ $7{\color{red} \diamondsuit}$ $K{\color{red} \heartsuit}$ $5{\color{red} \diamondsuit}$ $K{\color{red} \diamondsuit}$   |
| ${\color{red}R}{\color{red}R}{\color{red}R}{\color{red}R}{\color{red}R}$ | $7{\color{red} \diamondsuit}$ $K{\color{red} \heartsuit}$ $5{\color{red} \diamondsuit}$ $K{\color{red} \diamondsuit}$ $4{\color{red} \diamondsuit}$  |
| ${\color{red}R}{\color{red}R}{\color{red}R}{\color{red}R}B$| $K{\color{red} \heartsuit}$ $5{\color{red} \diamondsuit}$ $K{\color{red} \diamondsuit}$ $4{\color{red} \diamondsuit}$ $10{\clubsuit}$  |
| ${\color{red}R}{\color{red}R}{\color{red}R}BB$|  $5{\color{red} \diamondsuit}$ $K{\color{red} \diamondsuit}$ $4{\color{red} \diamondsuit}$ $10{\clubsuit}$ $7{\clubsuit}$   |
| ${\color{red}R}{\color{red}R}BB{\color{red}R}$|  $K{\color{red} \diamondsuit}$ $4{\color{red} \diamondsuit}$ $10{\clubsuit}$ $7{\clubsuit}$ $4{\color{red} \heartsuit}$   |
| ${\color{red}R}BB{\color{red}R}{\color{red}R}$| $4{\color{red} \diamondsuit}$ $10{\clubsuit}$ $7{\clubsuit}$ $4{\color{red} \heartsuit}$ $6{\color{red} \diamondsuit}$    |
| $BB{\color{red}R}{\color{red}R}B$ | $10{\clubsuit}$ $7{\clubsuit}$ $4{\color{red} \heartsuit}$ $6{\color{red} \diamondsuit}$ $3{\clubsuit}$   |
| $B{\color{red}R}{\color{red}R}BB$ | $7{\clubsuit}$ $4{\color{red} \heartsuit}$ $6{\color{red} \diamondsuit}$ $3{\clubsuit}$ $9{\clubsuit}$   |
| ${\color{red}R}{\color{red}R}BBB$ | $4{\color{red} \heartsuit}$ $6{\color{red} \diamondsuit}$ $3{\clubsuit}$ $9{\clubsuit}$ $6{\clubsuit}$   |
| ${\color{red}R}BBB{\color{red}R}$ |  $6{\color{red} \diamondsuit}$ $3{\clubsuit}$ $9{\clubsuit}$ $6{\clubsuit}$ $5{\color{red} \heartsuit}$   |
| $BBB{\color{red}R}B$ |  $3{\clubsuit}$ $9{\clubsuit}$ $6{\clubsuit}$ $5{\color{red} \heartsuit}$ $10{\spadesuit}$   |
| $BB{\color{red}R}B{\color{red}R}$ | $9{\clubsuit}$ $6{\clubsuit}$ $5{\color{red} \heartsuit}$ $10{\spadesuit}$ $9{\color{red} \diamondsuit}$  |
| $B{\color{red}R}B{\color{red}R}B$ |  $6{\clubsuit}$ $5{\color{red} \heartsuit}$ $10{\spadesuit}$ $9{\color{red} \diamondsuit}$ $3{\spadesuit}$  |
| ${\color{red}R}B{\color{red}R}BB$  |  $5{\color{red} \heartsuit}$ $10{\spadesuit}$ $9{\color{red} \diamondsuit}$ $3{\spadesuit}$ $Q{\clubsuit}$   |
| $B{\color{red}R}BB{\color{red}R}$   | $10{\spadesuit}$ $9{\color{red} \diamondsuit}$ $3{\spadesuit}$ $Q{\clubsuit}$ $8{\color{red} \heartsuit}$   |
| ${\color{red}R}BB{\color{red}R}B$   | $9{\color{red} \diamondsuit}$ $3{\spadesuit}$ $Q{\clubsuit}$ $8{\color{red} \heartsuit}$ $2{\spadesuit}$   |
| $BB{\color{red}R}BB$   | $3{\spadesuit}$ $Q{\clubsuit}$ $8{\color{red} \heartsuit}$ $2{\spadesuit}$ $8{\spadesuit}$|
| $B{\color{red}R}BBB$   | $Q{\clubsuit}$ $8{\color{red} \heartsuit}$ $2{\spadesuit}$ $8{\spadesuit}$ $J{\spadesuit}$  |
| ${\color{red}R}BBBB$   | $8{\color{red} \heartsuit}$ $2{\spadesuit}$ $8{\spadesuit}$ $J{\spadesuit}$ $6{\spadesuit}$|

Now by using this cheat sheet, you can perform the trick to a large number of audiences.


## Generalizations and Variations

1. **One variation is to change the value of k**. In a deck of cards if we distinguish element in a set by number, then there are only two options black and red. However, what if we distinguish by number? We could ask who has the highest card, the second highest, and the third highest? That gives us $n=3$. What if we use some other characteristics? What if we are not using standard 52-card deck? What if we use the deck from [Uno](https://en.wikipedia.org/wiki/Uno_(card_game))? Or [set](https://en.wikipedia.org/wiki/Set_(card_game))?

2. **Another variation is to change the value of n**. By changing the length of the subsequece, we should be able to change the number of cards to use to perform this trick. For $B(2,5)$,we are using $32 cards$, what happened if we use $B(2,6)$? How many cards would we need?

We hereby provide some properties of the de Bruijn sequence to help the readers to further generalize the trick.

**Theorem 1**: The number of distinct de Bruijn sequences $B(k, n)$ is $\frac{k!^{k^{n-1}}}{k^n}$.

**Theorem 2**: The length of a de Bruijn sequence $B(k,n)$ is $k^n$.

**Proof**: We agree that the length of $B(k,n)$ should equal to the number of distinct subsequence. Thus the question is translated to "how many distinct sequences exist with length $n$ and alphabet size $k$". For each position, we have $k$ choices, and in total we have $n$ positions. Therefore the length of $B(k,n) = k^n$.
<div style="text-align: right"> $\square$ </div>
