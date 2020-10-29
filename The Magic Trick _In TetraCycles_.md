A magician holds a deck of SET with eighty-one distinct cards. Each card contains four features that describe the image on the card. They are "shape", "color", "number", and "shading". Four volunteers are chosen from the audience. The magician cut the deck repeatedly and hands out four consecutive cards to the four volunteers. Then the magician allows volunteers to pick a feature that they prefer to describe. Let us assume that the "color" feature is picked. The magician then asked, "Since you picked color, would all of you with a red card please stand up?". After volunteers stand up accordingly, the magician asks "Would all of you with a green card please stand up?" Then the magician can name all four cards accurately, including their shapes, colors, numbers, and shadings.

We will not talk about how to play the game of SET, the following diagram by Quanta Magazine explains the basic rule of the game.

<img src='https://i.ibb.co/NLRsTyz/Untitled-design-4.png' width=100% height=100%>

This trick called "In TetraCycles" is a variation on the "In Cycles" trick developed by Persi Diaconis and Ron Graham and was elaborated in the book "Magical Mathematics: The Mathematical Ideas That Animate Great Magic Tricks". These tricks have various generalizations and magicians may be able to apply them to various decks.

It is surprising that the magician can detect all the cards, especially when no information is given about the other three features. The secret is that the deck is arranged in a very special order, where for every feature, the combination within every four consecutive cards is unique. Such properties are also cyclic, therefore is preserved when cutting the deck. It is astonishing that such a deck arrangement even exists as below:

<img src='https://i.ibb.co/Lz7QjX6/arrangement.jpg' width=100% height=100%>

How is such an arrangement possible? Turns out that the magician is using the properties of a de Bruijn sequence, which contains every possible subsequence. A de Bruijn sequence is a cyclic sequence of a given alphabet $A$ with $k$ elements in it, for which every possible subsequence of length $n$ in $A$ appears as a sequence of consecutive characters exactly once. We refer to such individual sequence as $B(k, n)$. For "In TetraCycles", we will be using a sequence $B(3, 4)$ since $n=4$ corresponds to the fact that each card in SET contains four features, and $k=3$ corresponds to the fact that three options are available for each feature. Let $A=\{0,1,2\}$, we can now provide context to the alphabet as below:

| shapes  | colors  | number of shapes | shading |
| :------------: |:---------------:| :-------------:|:---:|
| oval $\rightarrow  1$|red $\rightarrow 1$|one $\rightarrow  1$|solid $\rightarrow 1$ |
| squiggle $\rightarrow 2$ | green $\rightarrow  2$ |  two $\rightarrow 2$ | unfilled $\rightarrow 2$ |
| diamond $\rightarrow  0$ |    purple $\rightarrow  0$    |   three $\rightarrow  0$ | striped $\rightarrow 0$ |

How do we ensure that the trick works no matter which features the audience pick? We need to ensure that each feature is mapped to its own de Bruijn sequence. This is a challenging process since every SET cards are distinct, meaning that if we line up the four de Bruijn sequence and read off each column, each column will be representing a SET card and the column cannot repeat itself. There are in total over $1.26 \times 10^{19}$ distinct $B(3,4)$, however, randomly picking four of them and line them up will fail inevitably. Our approach to constructing the four de Bruijn sequences for this trick is to apply what we called a "shifting operation". Let B be a de Bruijn sequence, we can create $B_{-1}$ by moving all the digits forward by one, and move the first digit to the end. By applying the same process to $B_{-1}$, we obtain $B_{-2}$. We can obtain $B_{-3}$ using the same method. By lining up $B, B_{-1}, B_{-2}, B_{-3}B_{-2}, B_{-3}$ and reading off each column, we obtain all possible ways to construct a length-4 sequence using elements in $\{0,1,2\}$. 

Now we will generate a de Bruijn sequence with a graphical approach. A de Bruijn graph is a directed graph. We will layout the main procedures as follows: 

1. Generate all **vertices** of the de Bruijn graph based on input values of $k$ and $n$.
2. Find all possible **edges** between these vertices.
3. Find one random **Eulerian circuit**.
4. Find the corresponding **de Bruijn sequence** based on the Eulerian circuit.

By following this process, we have generated a de Bruijn sequence:

$${\small B =102000020201201101221011110001120012102211121122212122002201010210010021202222021}$$

Thus we have $B_{-1}, B_{-2}, B_{-3}$:

$${\small B_{-1} =020000202012011012210111100011200121022111211222121220022010102100100212022220211}$$
$${\small B_{-2} =200002020120110122101111000112001210221112112221212200220101021001002120222202110}$$
$${\small B_{-3} =000020201201101221011110001120012102211121122212122002201010210010021202222021102}$$

Now by assigning $B$ to shape, $B_{-1}$ to color, $B_{-2}$ to number, and $B_{-3}$ to shading, the magician knows exactly how to arrange the deck to complete "In TetraCycles" since each column simply represents a card, and the corresponding shape, color, number, and shading can be found by referencing the table above. 

The cheat sheet below is designed for the shape feature, where 'D' stands for diamond, 'S' stands for squiggle, and 'O' stands for Oval. Once volunteers answer both questions regarding shape, we will be able to determine each card's shape. Then we refer to the cheat sheet to find the corresponding column. The exact four cards are shown on the right.


<img src="https://i.ibb.co/zHhK0yh/cheat-sheet.jpg" width=100% height=100%>

