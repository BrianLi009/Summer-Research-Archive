**This part should not be included in the actual blog**

Post Structure:

1. Introduce the card game Set, rules, and what is classified as a set.

2. Make connections between the cards and its algebraic structure by giving definitions and examples

3. Introduce Set Product and what it models

4. Explore Set product's Algebraic properties (associativity, commutativity)

4. Explore more propoerties if possible

**Actual Blog Starts Here**

### Introducing a card game called "SET"

"Set" is a game that is quite popular within the mathematics community. The game is played with a deck of $81$ unique cards. Each card varies in four features across three possibilities. They are the **shapes** (one, two, three), the **colors** itself (oval, squiggle, diamond), the **number of shapes** (solid, unfilled, striped), and the **shading** (red, green, purple). The cheat sheet below created by [Quanta Magazine](https://www.quantamagazine.org/set-proof-stuns-mathematicians-20160531) offers a detailed explanation on how to play the game. You can also play around with the game [here](https://www.setgame.com/set/puzzle). At the end of this post, we will count the total number of SETs."

<img src='https://i.ibb.co/NLRsTyz/Untitled-design-4.png' width=100% height=100%>

### Algebraic Representation of the SET Deck
We want to label each cards with an algebraic representation. There are various motivation behind doing so. One is that giving algebraic representation to the deck allows us to program the game easily. Another reason is that having an algebraic representation allows mathematicians to compute the deck's probabilistic and combinatorics properties. Since there are $4$ features, each of which has $3$ possible values, we can associate each card in the SET deck with an element in the set $D = Z_3 \times Z_3 \times Z_3 \times Z_3$. We simply assign a $1$, $2$, or $0$ with each of the three possible values for a given characteristic as defined below.

**Definition 1.0:** For a card in the game of set, the card can be expressed as a $4$-number tuple $(x_{1},x_{2},x_{3},x_{4})$ such that $x_{i}$ describes a unique feature according to the following table [2]:
| shapes  | colors  | number of shapes | shading |
| :------------: |:---------------:| :-------------:|:---:|
| oval $\rightarrow  1$|red $\rightarrow 1$|one $\rightarrow  1$|solid $\rightarrow 1$ |
| squiggle $\rightarrow 2$ | green $\rightarrow  2$ |  two $\rightarrow 2$ | unfilled $\rightarrow 2$ |
| diamond $\rightarrow  0$ |    purple $\rightarrow  0$    |   three $\rightarrow  0$ | striped $\rightarrow 0$ |

**Example 1.1:** Express the following cards algebraically.

- <img src="https://i.ibb.co/r6QPPgC/22.jpg" width=10% height=10%> : the card has oval shape ($1$), color green ($2$), two shapes ($2$), and unfilled shading
 ($2$). Therefore this card correspond to the tuple $(1,2,2,2)$.
- <img src="https://i.ibb.co/fQB2Lwn/33.jpg" width=10% height=10%> : the card has squiggle shape ($2$), color red ($1$), three shapes ($3$), solid shading ($1$). Therefore the card corresponds to the tuple $(2, 1, 3, 1)$.
- <img src="https://i.ibb.co/dDyPCm9/11.jpg" width=10% height=10%> : the card has diamond shape ($0$), color purple ($0$), one shape ($1$), striped shading ($0$). Therefore the card corresponds to the tuple $(0,0,1,0)$.

### The Set Product of the SET Deck
Now we will define an operation on  $D = Z_3 \times Z_3 \times Z_3 \times Z_3$. This operation reflects how one obtains a "SET" from two given cards.

**Definition 1.2:** Let $x = (x_{1}, x_{2}, x_{3}, x_{4}) \in D$ and $y = (y_{1}, y_{2}, y_{3}, y_{4}) \in D$, then [1] $$ x \cdot y = (2(x_{1}+y_{1})\space \text{mod} \space 3), 2(x_{2}+y_{2})\space \text{mod} \space 3), 2(x_{3}+y_{3})\space \text{mod} \space 3), 2(x_{4}+y_{4})\space \text{mod} \space 3)) $$

**Theorem 1.3:** Given $x, y \in D$ and $x \cdot y = z$, card $x, y, z$ form a SET in the game. Moreover, such $z$ is unique.

**Proof:** To show that $x, y$, and $z = x \cdot y$ are a SET in the game, we will look at each feature in two cases:

1. If $x_{i} = y_{i}$, then $z_{i} = 2(2x_{1}) \space \text{mod}\space 3 = x_{i}$, therefore $x_{i}=y_{i}=z_{i}$. So the $i$th feature of all three cards are all the same.

2. If $x_{i} \neq y_{i}$, let us first assume that $x_{i}=z_{i}$, then $2(x_{i}+y_{i}) \space \text{mod}\space 3 = z_{i} = x_{i}$, then $x_{i} + 2y_{i} \space \text{mod} \space 3 = 0$. This implies that $x_{i} = y_{i}$, which contradicts the assumption. This shows that $x_{i} \neq z_{i}$, thus the $i$th feature of all three cards are all different. Similar results can be obtained when assuming $y_{i} = z_{i}$.

These two cases above shows that the $i$th feature of all three cards are either all the same or all different, and this is true for any $i$ value such that $1 \leq i \leq 4$. Therefore, given $x \cdot y = z$, card $x$, $y$, $z$ form a SET in the game. Notice that $z$ is unique. To see this, pick any two cards $x$ and $y$, the value of each feature of x and y will either be the same or different. If a given attribute is the same for both $x$ and $y$, then $z$ must also have the same feature so there only exists one choice for that feature of $z$. If the given attribute is different for x and y, then that attribute on $z$ must be different from $x$ and $y$, hence there is only one choice since there are only $3$ different properties to choose from.
<div style="text-align: right"> $\square$ </div>

Now we want to explore some algebraic properties of the set $D$. We want to investigate whether $D$ is a group, and if not, which property of a group also applies in $D$. What does that tell us about this game? Does this discovery encode any further meanings?

**Lemma 1.4:** $D$ under Set Product is commutative.

**Proof:** Given two cards $x$ and $y$, we can deduct the other card $z$ that forms a SET. Notice that the order of $x$ and $y$ does not matter and this trivial property shows commutativity of the Set Product.
<div style="text-align: right"> $\square$ </div>

**Lemma 1.5:** $D$ under Set Product is not associative.

**Proof:** We will prove this by providing a counterexample. Let $x=(1,1,1,1), y =(2,2,1,1), z=(1,2,2,0)$.

 - $x\cdot y = (1,1,1,1) \cdot (2,2,1,1) = (0,0,1,1)$, so $(x\cdot y)\cdot z = (0,0,1,1)\cdot (1,2,2,0) = (2,1,0,2)$
 - $y\cdot z = (2,2,1,1) \cdot (1,2,2,0) = (0,2,0,2)$, so $x\cdot (y \cdot z) = (1,1,1,1) \cdot (0,2,0,2) = (2,0,2,0)$

We can see that $x \neq y$, thus $D$ under Set Product is not associative.
<div style="text-align: right"> $\square$ </div>

Now we are going to discuss some special properties of the Set Product.

**Lemma 1.6:** If $x, y \in D$, then $x\cdot (x\cdot y) = y$

**Proof:** Let $x=(x_{1}, x_{2}, x_{3}, x_{4}), y=(y_{1}, y_{2}, y_{3}, y_{4})$, the $i$th coordinate of $x\cdot (x\cdot y)$ is $2(x_{i} + 2(x_{i} + y_{i})) \space \text{mod} \space 3 = (4x_{i} + 4y_{i} + 2y_{i}) \space \text{mod}\space 3 =  6x_{i}\space \text{mod}\space 3 + 4y_{i} \space \text{mod}\space 3 = 0 + y_{i} \space \text{mod} \space 3 = y_{i}$.
<div style="text-align: right"> $\square$ </div>


**Theorem 1.8:** If $x,y,z \in D$, and $x\cdot y = x\cdot z$, then $y=z$ (Cancelation).

**Proof:** By Lemma 1.6, $y = x\cdot (x\cdot y)$. Since $x\cdot y = x\cdot z$ we
have $y = x\cdot (x\cdot z)$, and by applying Lemma 1.6 again, $y = z$. 
<div style="text-align: right"> $\square$ </div>

Now it is clear that the set $D$ is not a group. However, it does satisfy a subset of algebraic laws within a group. Knowing this, we can use these rules to discover some probabilistic and combinatorics fact about the game SET.

**Definition 1.9:** We define **D-set** to be a subset $S \subseteq D$ such that $S = \{x, y, x\cdot y \}$. Naturally, D-set represents a SET in the game.

**Theorem 2.0:** There are in total $1080$ unique D-set in $D$.

**Proof:** There are $81$ elements in $D$. For each D-set in $D$, there are $81$ choices for $x$ and $80$ choices for $y$. Based on theorem 1.3, we already know that $x \cdot y$ is unique. Due to lemma 1.4, we know that we obtain the same set regardless the order of $x$ and $y$. Thus the total number of unique D-set in $D$ is $\frac{\left(\begin{array}{c}80\\ 2\end{array}\right)}{2}=\frac{80 \cdot 81}{3!} = 1080$.
<div style="text-align: right"> $\square$ </div>

**Theorem 2.1:** Given card $x$, there exist in total $40$ sets that contain $x$.

**Proof:** Once the card $x$ is chosen, we have 80 choices for a second card and then only one choice for the card to finish the set. However, since order doesn’t matter, we’ve counted each set twice, so the number of sets containing any given card is $\frac{80}{2} = 40$.
<div style="text-align: right"> $\square$ </div>


### References
[1] Paola Y. Reyes, The Mathematics of the Card Game Set, Digital Commons @ Rhode Island College

[2]  Judy A. Holdener BS and MS and PhD (2005) PRODUCT-FREE SETS IN
THE CARD GAME SET, Problems, Resources, and Issues in Mathematics Undergraduate Studies, 15:4, 289-297, DOI: 10.1080/10511970508984123
