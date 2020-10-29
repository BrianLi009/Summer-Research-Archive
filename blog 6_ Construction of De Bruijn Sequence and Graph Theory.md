**This part should not be included in the actual blog**

Post Structure:

1. Make connections with the last blog post, ensure that readers have a fundamental understanding of de Bruijn sequence

2. Connect de Bruijn sequence to graph theory by making graphs and showing how these graphs help us identify the sequence.

3. Prove the existence of Euler circuits

4. Read of the de Bruijn sequence from the grpah

4. Introduce the code, demo with examples, discuss future improvement

**Actual Blog Starts Here**

During [last week's post](https://404briannotfound.tech/views/MAT388/2020/post5.html#a-magic-trick-for-five-participants), we have talked about what de Bruijn sequence is, their fundamental properties, and how it is used in a card trick. This week we are going to extend further on this topic from a graphical perspective, and build up this connection between de Bruijn sequences and graph theory.

## Using De Bruijn Graph to find De Bruijn Sequences
**Definition 1.0:** The $n$-dimensional **de Bruijn graph** of alphabet with size $k$ is a [directed graph](https://en.wikipedia.org/wiki/Directed_graph) representing overlaps between sequences of alphabet symbols. The de Bruijn graph $B(k,n)$ is defined as $(V,E)$, where $V=S^{n}=\left\{(s_{1}s_{1}...s_{1}), (s_{1}s_{1}...s_{2}),..., (s_{1}s_{1}...s_{k}),..., (s_{k}s_{k}...s_{k})\right\}$, and $E=\left\{  ((t_{1},t_{2},...,t_{n}),(t_{2},...t_{n}, s_{j})): t_{i}\in S, 1\leq i \leq n, 1\leq j \leq k\right\}$.

**Note:** The vertices consists of all possible length-n sequences $S$ of the alphabet symbols. If one of the vertices $A$ can be expressed as another vertex $B$ by shifting all its symbols by one place to the left and adding a new symbol from the alphabet at the end of this vertex, then $B$ has a directed edge to $A$.

**Definition 1.1:** An Euler circuit is a connected graph such that starting at a vertex $a$, one can traverse along every **edge** of the graph once to each of the other vertices and return to vertex $a$. In other words, an Euler circuit is an [Eulerian path](https://en.wikipedia.org/wiki/Eulerian_path) that is a circuit.

**Example 1.0**: Let us try constructing $B(2,2)$ sequence using a graphing approach:
To construct a $B(2,2)$ de Bruijn sequence of length $2^{2}=4$, we will be constructing a de Bruijn graph.

 - We will start by listing out the edges. Since the alphabet has size 2, let us assume $S=\left\{0,1\right\}$. Since $n=1$, the only two edges are $0$ and $1$.
 - Now we can find the edges. Since $1$ can be expressed as $0$ shifted left then adding $1$, and $0$ can be expressed as $1$ shifted left then adding $0$, we obtain the edges $(0,1)$ with label "$1$" and $(1,0)$ with label "$0$". And both $0$ and $1$ can be mapped to itself. The label here represents the transition being taken.
 - Finally we can draw out the graph:\
 <img src='https://i.ibb.co/nnfQbjy/1.png' width=100% height=100% >
 - Now we can map out the de Bruijn sequence by tracing an Eulerian circuit. By appending each label of edges (tracing along the edges and cover all of them), we get $(0110)$ or $(1001)$.
 
**Example 1.1**: Let us try constructing $B(2,4)$ sequence using a graphing approach:
To construct a $B(2,4)$ de Bruijn sequence of length $2^{2}=4$, we will be constructing the de Bruijn graph where each vertex has length $3$. 

- We will start by listing out the edges. Since the alphabet has size 2, let us assume $S=\left\{0,1\right\}$. Since $n=3$, the edges are $000$, $001$, $010$, $100$, $110$, $011$, $101$, $111$.

 - Now we can find the edges. We can obtain the following transition:
 
| Tail of the Edge  | Edge Label  | Head of the Edge |
| :------------: |:---------------:| :-------------:|
|   $000$    | $0$ | $000$ |
| $000$  |    $1$     |  $001$ |
| $001$ |    $0$     |    $010$ |
| $001$ |    $1$     |    $011$ |
| $010$ |    $0$     |    $100$ |
| $010$ |    $1$     |    $101$ |
| $100$ |    $0$     |    $000$ |
| $100$ |    $1$     |    $001$ |
| $110$ |    $0$     |    $100$ |
| $110$ |    $1$     |    $101$ |
| $011$ |    $0$     |    $110$ |
| $011$ |    $1$     |    $111$ |
| $101$ |    $0$     |    $010$ |
| $101$ |    $1$     |    $011$ |
| $111$ |    $0$     |    $110$ |
| $111$ |    $1$     |    $111$ |
 - Finally we can draw out the graph:\
 <img src='https://i.ibb.co/HFLH2m2/Wf-Fi-VEHMNch-Rtu-OT.png' width=100% height=100% >
 - Now we can map out the de Bruijn sequence by tracing an Eulerian circuit. Recall that an Eulerian circuit has to pass through all edges, not vertices. By appending each label of edges (tracing along the edges and cover all of them), if we start from $000$, and use the path $000\rightarrow 000 \rightarrow 001 \rightarrow 011 \rightarrow 111 \rightarrow 111 \rightarrow 110 \rightarrow 101 \rightarrow 011 \rightarrow 110 \rightarrow 100 \rightarrow 001 \rightarrow 010 \rightarrow 101 \rightarrow 010 \rightarrow 100 \rightarrow 000$. We will obtain $0111101100101000$.
 
**Lemma 1.0:** A directed graph admits an Eulerian circuit if and only if there are no vertices with odd degree (all vertices have even degree) and is [strongly connected](https://en.wikipedia.org/wiki/Strongly_connected_component).

**Proof:** For the first implication, take $G=(V,E)$ as the Eulerian graph with a closed Eulerian trial $T=[v_{0}v_{1}...v_{k}]$, such that $v_{0}=v_{k}$. For each $v\in V$, the trial $T$ enters $v$ through an edge and exits from another edge of $G$. Thus at each stage, the process of entering and exiting an vertex $v$ increments $2$ to the degree of $v$. Moreover, the trial $T$ passes through each edge of $X$ exactly once, hence each vertex must be of even degree. 

Conversely, assume that each vertex of $G$ has an even degree and $G$ is strongly connected, we will prove that an $G$ admits an Eulerian circuit by induction. As each vertex has even degree and $G$ is strongly connected, $G$ contains a circuit, say $C$. If $C$ contains every edge of $G$, then $C$ is a closed Eulerian circuit hence the proof is complete. Now let us assume the other case, where $C$ is a propoer subset of $E$. Consider the graph $G'$ obtained from $G$ by removing all the edges in $C$. Then $G'$ may be a disconnected graph but each vertex of $G'$ still has even degree. As each component of $G'$ has at least one vertex in common with $C$, we can construct the desired closed Eulerian circuit as follows: Start with a vertex $v_{0} \in C$, if there is a component of $G'$ having $v_{0}$ as a vertex, then traverse this component and come back to $v_{0}$. This is possible since each component is Eulerian. Now,  proceed along the edges of $C$ until we get another component of $G'$ called $v_{1}$. We repeat the process by trav ersing the new component of $G'$ starting with $v_{1}$ and return to $v_{1}$. Such process terminates as we return to the vertex $v_{0} \in C$. Thus lemma 1.0 is proven.

<div style="text-align: right"> $\square$ </div>

**Theorem 1.0:** An Eulerian circuit always exist in a de Bruijn graph.

**Proof:** Let G be a $B(k,n)$ graph. For each vertex, the number of incoming edges is equal to $n$ since such vertex is obtained by shifting the previous vertex and add an extra bit from the alphabet. The same logic applies to the edges going out. The following diagram will illustrate the idea better:
<img src='https://i.ibb.co/vz6xgcM/1.png' width=100% height=100% >
Therefore we can conclude that the number of incoming edges is equal to the number of outgoing edges, thus the edge has an even degree ($odd+odd=even$). Therefore based on lemma 1.0 and the fact that all de Bruijn graph is strongly connected, we can conclude that an Eulerian circuit always exist in a de Bruijn graph.
<div style="text-align: right"> $\square$ </div>

## Exploring with Python Code
I have written a series of functions that generates a de Bruijn graph for any $B(2, n)$ sequences, which means that the program will assume that the alphabet is ${0,1}$. Here is the program and its output:
```
# Input window length, we should be able to genearate a graph assuming k=2
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import itertools
import functools

def generate_node(n):
    """This function inputs an alphabet with size 2 and window size n, and output all nodes in the de Bruijn graph"""
    length = n-1
    lst = list(itertools.product([0, 1], repeat=length))
    return lst
    
def turn_tuple_to_str(tuple):
    string = ''
    for element in tuple:
        string += str(element)
    return string
    
def generate_graph(n):
    """take in window size n and assume alphabet with 0,1, output a de Bruijn graph"""
    node_lst = generate_node(n)
    G = nx.DiGraph(directed=True)
    edge_labels={}
    for node1, node2 in itertools.combinations(node_lst, 2):
        node1_copy = node1[1:]
        node2_copy = node2[:n-2]
        label1 = node2[n-2]
        node1_copy2 = node1[:n-2]
        node2_copy2 = node2[1:]
        label2 = node1[n-2]
        if node1_copy == node2_copy:
            G.add_edge(turn_tuple_to_str(node1), turn_tuple_to_str(node2))
            edge_labels[(turn_tuple_to_str(node1), turn_tuple_to_str(node2))]=label1
        if node1_copy2 == node2_copy2:
            G.add_edge(turn_tuple_to_str(node2), turn_tuple_to_str(node1))
            edge_labels[(turn_tuple_to_str(node2), turn_tuple_to_str(node1))]=label2
    options = {
    'node_color': 'pink',
    'node_size': 5000,
    'width': 3,
    'arrowstyle': '-|>',
    'arrowsize': 30,
    'font_size': 12,
}
    pos = nx.shell_layout(G)
    nx.draw(G, pos, with_labels=True, connectionstyle='arc3, rad = 0.1', **options)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,label_pos=0.1, font_color='red')
```
To use the function:
```
generate_graph(4)
```
<img src="https://i.ibb.co/dpT6s8k/a.png" width=100% height=100% >

Notice that how in this graph $000$ and $111$ does not loop to itself, this is due to the limitation of the graphing package "networkx". The self looping does not seem to show up at all. However, it does exist and we should keep that in mind.

The next step for me, is to generalize this program so that it can graph an alphabet great than 2, that would be something interesting to explore. Thanks for reading!






