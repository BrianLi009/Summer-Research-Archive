**This part should not be included in the actual blog**

Post Structure:

1. Revisit the idea of de Bruijn sequence, the total number of de Bruijn sequence for B(k,n) and try to prove it

2. Introduce the idea of my de Bruijn generator, how it uses a graphing approach and how I managed to generate all possible de Bruijn sequences

3. Demonstrate the code with good comments and documentation

4. Showcase some examples

**Actual Blog Starts Here**

Today we will be revisiting de Bruijn sequence and providing code for generating them. Furthermore, we will discuss the logic behind our generating method and provide examples. This post is a continuation of ["Construction of De Bruijn Sequence and Graph Theory"](https://404briannotfound.tech/views/MAT388/2020/post6a.html#using-de-bruijn-graph-to-find-de-bruijn-sequences).

Recall that from "Construction of De Bruijn Sequence and Graph Theory", we have created code that can produce a de Bruijn sequence of $B(2, n)$, meaning that the alphabet must have size-$2$, which normally implies alphabet $\{0,1\}$. In this post we will provide code that can essentially **generate all de Bruijn sequences for any $B(k,n)$.** So far, most programs online only generate one de Bruijn sequence. 

The following steps illustrates how our de Bruijn sequence generator works:

1. Generate all **vertices** of the de Bruijn grpah  based on input values of $k$ and $n$.
2. Find all possible **edges** between these vertices.
3. Find one random **Eulerian circuit**.
4. Find the corresponding **de Bruijn sequence** based on step 3.

Now we will break down the code based on the four steps above:

1. The function _generate_vertex_ takes in value $k$ and $n$ and outputs all vertices' value. This is done by outputting all possible ways to write a length (n-1) sequence with alphabet $k$. 
```
def generate_vertex(k, n):
    length = n-1
    lst = list(itertools.product(k, repeat=length))
    return lst
```
2. The function _generate_edges_ takes in value $k$ and $n$ as well, but output not only the vertices but also the edges that connect them.

```
def generate_edges(k, n):
    v_lst = generate_vertex(k,n)
    edge_lst = []
    for v1, v2 in itertools.combinations(v_lst, 2):
        node1_copy = v1[1:]
        node2_copy = v2[:n-2]
        label1 = v2[n-2]
        node1_copy2 = v1[:n-2]
        node2_copy2 = v2[1:]
        label2 = v1[n-2]
        if node1_copy == node2_copy:
            edge_lst.append(turn_tuple_to_str(v1)+ "----" + label1 + "--->" + turn_tuple_to_str(v2))
        if node1_copy2 == node2_copy2:
            edge_lst.append(turn_tuple_to_str(v2)+ "----" + label2 + "--->" + turn_tuple_to_str(v1))
    for element in k:
        edge_lst.append((element*(n-1)) + "----" + element + "--->"+ (element*(n-1)))
    return edge_lst
```

3. The function _eulerian_path_ takes in $k$, $n$ and it outputs the Eulerian path using the [networkX](https://networkx.github.io/) plug in. ['ba', 'aa', 'aa', 'ab', 'bb', 'bb', 'ba', 'ab'] represents the vertices based on the traversing order of the Eulerian path. One interesting thing is that, networkX generates different de Bruijn seqeunces based on different input order of vertices. This is an important property that we will utilize heavily later on.

```
def eulerian_path(k,n):
    edge_lst = generate_edges(k,n)
    new_lst = []
    for item in edge_lst:
        start_vertex = item[:n-1]
        end_vertex = item[-n+1:]
        new_lst.append((start_vertex, end_vertex))
    random.shuffle(new_lst)
    G = nx.DiGraph()
    G.add_edges_from(new_lst)
    return [u for u, v in nx.eulerian_circuit(G)]
```

4. The function _generate_debruijn_ takes in $k$, $n$ and output one de Bruijn seqence based on an Eulerian path generated from _eulerian_path_. What we are doing is that we are simply tracing the edges based on our networkX graph, and that gives us a de Bruijn sequence.

```
def generate_debruijn(k, n: int) -> str:
    vertex_lst = eulerian_path(k,n)
    str = ''
    for vertex in vertex_lst:
        str += vertex[-1]
    return str
```

Now we can combine the four functions above and output a _summary_ of $B(k,n)$.

```
def summary(k, n):
    v_lst = generate_vertex(k,n)
    e_lst = generate_edges(k,n)
    print ("You have entered an alphabet of " + str(k) + ", and you are computing for window length " + str(n))
    print ("The number of vertices is " + str(len(v_lst)) + ", they are " + str(v_lst))
    print ("The number of edges is " + str(len(e_lst)) + ", they are " + str(e_lst))
    print ("Its eulerian circuit is " + str(eulerian_path(k,n)))
    print ("And the de Bruijn sequence is " + str(generate_debruijn(k,n)))
```

We can test out the function:
```
summary(['a','b'],3)
>>> You have entered an alphabet of ['a', 'b'], and you are computing for window length 3
>>> The number of vertices is 4, they are [('a', 'a'), ('a', 'b'), ('b', 'a'), ('b', 'b')]
>>> The number of edges is 8, they are ['aa----b--->ab', 'ba----a--->aa', 'ab----a--->ba', 'ba----b--->ab', 'ab----b--->bb', 'bb----a--->ba', 'aa----a--->aa', 'bb----b--->bb']
>>> Its eulerian circuit is ['ab', 'bb', 'bb', 'ba', 'aa', 'aa', 'ab', 'ba']
And the de Bruijn sequence is aaabbbab
```

Now the question is, how do we generate all de Bruijn sequences? As you might realize by now, there should be a lot more than one de Bruijn sequence for large values of $k$ and $n$. In fact, the number of distinct de Bruijn sequence $B(k,n)$ is $\frac{k!^{k^{n-1}}}{k^n}$. The proof for the case where $k=2$ can be found on [Algebraic Combinatorics] by Richard P. Stanley, starting from page 154. In fact, this number increases at a extremely fast rate, the following table demonstrate the number of distinct de Bruijn sequence for $B(2,n)$:
| $n$  | number of $B(2,n)$  |
| :------------: |:---------------:|
| $1$      | $1$ |
| $2$      |    $1$     |
| $3$ |    $2$    |
| $4$ |    $16$ |
| $5$ | $2,048$ |
| $6$ | $67,108,864$ |
| $7$ | $144,115,188,075,855,872$ |
| $8$ | $1.329\cdot10^{36}$ |

Recall that networkX generates different de Bruijn seqences based on the order of each vertex input. We can utilize this properties to generate all possible de Bruijn sequences by inputting all possible order of vertices. This is what the function _get_as_many_bruijn_ is doing. We randomly shuffled the order in the function _eulerian_path_ so that eventually we can cover all de Bruijn sequence. However, this could be further optimized runtime wise by replacing the "random shuffle" with an organized list with all possible permutation. I am unsure how much significance that may have in terms of reducing the runtime, but it is worth trying out in the near future.

```
def get_as_many_bruijn(k,n):
    total_num = (math.factorial(len(k))**(len(k)**(n-1))/(len(k)**n))
    print ("in total " + str(total_num) + " de Bruijn sequences")
    output = []
    while len(output) < total_num:
        sequence = generate_debruijn(k,n)
        if sequence not in output:
            output.append(sequence)
    return output
```
Here are two outputs of the above function as examples:

```
get_as_many_bruijn(['a','b'],3)
>>> in total 2.0 de Bruijn sequences
>>> ['aaabbbab', 'baaababb']
```

```
get_as_many_bruijn(['a','b','c'],4)
>>> in total 1.2635683568857645e+19 de Bruijn sequences
>>> ['bbcbaccaabacaaaabcaaccccababaaacabcbcbbacbabccacaccbaacbbcccbbbbaabbcacbccbcabbab',
     'aaabcacaccccacbabcccbacbbababbacabcbaabaccbbcbbbaaaccabaacaabbcabbbbccaacbccbcbca',
     'bccbccccbbbbaabbbccaabaacaacccacaccbaaabcbcbbaccabacabcaaaacbcacbbcabbababbcbacba',
     'acbabcbbcbcbacbbababbacaacacabbccccbbbcacbccbcabaccbaacccabcaabbbbaabccaccaaabaaa',
     ...]
```

One can create a SET deck such that the number attribute of the cards is a de Bruijn sequence. Simply pick a de Bruijn sequences from B(3,4), assign these as the numbers of the cards, and then complete the rest of the attributes arbitrarily. This leads to the question: Is it possible arrange the cards such that multiple attributes occur in every possible combination? The following theorem shows that one can arrange the cards such that every attribute is a de Bruijn sequence simultaneously.

**Definition:** For a de Bruijn sequence $B$, we use $B_{i}$ to represent the shifting operation. If $i < 0$, we shift the sequence left. If $i > 0$, we shift the sequence right.

**Example:** Let $B$ be $aaabbbab$, then $B_{-1}$ is $aabbbaba$.

**Theorem 1:**  If $B_0(n)$ is a de Bruijn sequence then $(B_0(n), B_{-1}(n), B_{-2}(n), B_{-3}(n))$ is distinct for all n satisfying 1 <= n <= 81.

**Proof:** Let $B_0 = a_{1}a_{2}a_{3}a_{4}......a_{80}a_{81}$, then $B_{-1} = a_{2}a_{3}a_{4}......a_{80}a_{81}a_{1}$, $B_{-2} = a_{3}a_{4}......a_{80}a_{81}a_{1}a_{2}$, $B_{-3} = a_{4}......a_{80}a_{81}a_{1}a_{2}a_{3}$. 

When reading off the first column of $B_{0}, B_{-1}, B_{-2}, B_{-3}$ in order, we obtained the first letter from each sequence, which can be represented as $(B_{0}(1), B_{-1}(1), B_{-2}(1), B_{-3}(1))$. In the example below that would be $(a,a,b,c)$.

To generalize this, for each $i$th column, reading vertically gives $(B_{0}(i), B_{-1}(i), B_{-2}(i), B_{-3}(i))$. Since $B_{-1}, B_{-2}, B_{-3}$ are generated by shifting $B_{0}$, we have that $B_{-1}(i) = B_{0}(i+1)$, $B_{-2}(i) = B_{0}(i+2)$, $B_{-3}(i) = B_{0}(i+3)$. Thus $(B_{0}(i), B_{-1}(i), B_{-2}(i), B_{-3}(i)) = (B_{0}(i), B_{0}(i+1), B_{0}(i+2), B_{0}(i+3))$. Notice how this is exactly the same thing as reading $B_{0}$ from left to right with a window of four. In other word, reading off the sequences vertically from $B_{0}(i)$ is equivalent to reading off $B_{0}$ horizontally from $B_{0}(i)$ left to right.

Since $B_{0} \in B(3,4)$ is a de Bruijn sequence, $B_{0}$ contains all possible ways to construct a length-4 string with $a, b, c$. The total number of ways to do so is equal to the length of $B_{0}$, which is $3^4 = 81$. This proves that there cannot be overlap, and each sub-sequence with length of four is distinct. Thus reading off the four sequences vertically yield all and distinct strings.

<div style="text-align: right"> $\square$ </div>

**Example:** Let us generate a de Bruijn sequence $B(3, 4)$ using the program:
```
generate_debruijn(['a','b','c'],4)
>>> aabccccacacbbabbacbababcbbcbacabbccabcacccbbbaacbcbccbaabbbbcabaaaacaabaccaaccbca
```
Now to shift this sequence by $0, -1,-2, -3$, we obtain four sequences that essentially represent the same $B(3, 4)$:

$B_0\space \space: \textcolor{blue}{a}abccccacacbbabbacbababcbbcbacabbcca\textcolor{red}{bcac}ccbbbaacbcbccbaabbbbcabaaaacaabaccaaccbca$

$B_{-1}: \textcolor{blue}{a}bccccacacbbabbacbababcbbcbacabbcca\textcolor{red}{bcac}ccbbbaacbcbccbaabbbbcabaaaacaabaccaaccbcaa$

$B_{-2}: \textcolor{blue}{b}ccccacacbbabbacbababcbbcbacabbcca\textcolor{red}{bcac}ccbbbaacbcbccbaabbbbcabaaaacaabaccaaccbcaaa$

$B_{-3}: \textcolor{blue}{c}cccacacbbabbacbababcbbcbacabbcca\textcolor{red}{bcac}ccbbbaacbcbccbaabbbbcabaaaacaabaccaaccbcaaab$

Notice that by reading column by column (the blue letters), we can obtain all possible ways to construct a length-$4$ string with the letter $a,b,c$. This can be confirmed by the reader.



