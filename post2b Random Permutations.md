This post will provide readers with a general idea of what species is and how it is being used for graphs and permutations. Essentially, species exist to facilitate the abstract study of structures on (finite) sets, such as graphs and permutations.
## Definition
We will use the following background material:

 - **Categories**: A [category](https://en.wikipedia.org/wiki/Category_theory) is a collection of objects and maps between them. Examples of categories include groups, rings, sets, and topological spaces.

 - **Functor**: A [functor](https://en.wikipedia.org/wiki/Functor) is a map between categories. For example, a functor might replace topological spaces with groups.

 - **Species**: Let B be the category of finite set, with the morphism within the category be the bijection of these sets, a [species](https://en.wikipedia.org/wiki/Combinatorial_species) is a functor such that:
 $$F: B\rightarrow B$$

We will provide some examples below to make the concept less abstract and easier to perceive. For the purpose of this post, we will mainly focus on species for graphs and permutations.
## The Species of Graphs

#### Definition
We will be writing "Species of Graphs" as "Gra". This is a functor, from finite sets to finite sets. Gra will take a finite set $U$, and output the set of all graph structures on $U$. A graph structure consists of vertices and edges. An edge joins two vertices from $U$. 
$$Gra(U)=\left\{\left(U,E\right) : E \subseteq  \binom{U}{2} \right\}$$
To specify a functor, we must also describe how it acts on morphisms. If $ \sigma : U \rightarrow V $ is a bijection, then $ Gra( \sigma : U \rightarrow V)$ is ...

In this case we have:
$$Gra\left( \sigma: U \rightarrow V\right):Gra\left( U \right)\rightarrow Gra\left( V\right)=\left(U,E\right)\mapsto \left(V,\sigma E\right)$$

We write $\sigma E = \{ \{ \sigma(a), \sigma(b) \} : \{a,b\} \in E\}$. Essentially we are relableing all the vertices and keep the edges where they are.

#### Examples
We will provide an example with 3 edges: 

<p align="center">
<img src='https://i.ibb.co/X2Z74XB/Zhd-Ye-Mnj-SViclvq-Q.png' width=30%  title='Graph1'>
</p>

Now the question is, how many ways can we construct a graph structure out of this? The graphs below showcased the result:
<img src='https://i.ibb.co/G36GfNG/jbw-Ov-Syvi-KYw-HWId.png' width=100%  title='Graph2'>

We can also express these structures using another notation where $G=\left(V,E\right)$, where V stands for vertices and E stands for edges:
$$Gra(u)=\left\{\left(\left\{A,B,C\right\},\left\{(A,B)\right\}\right),\{\left(\left\{A,B,C\right\},\left\{(B,C)\right\}\right),\{\left(\left\{A,B,C\right\},\left\{(A,C)\right\}\right),\{\left(\left\{A,B,C\right\},\left\{(A,B),(B,C)\right\}\right),\{\left(\left\{A,B,C\right\},\left\{(A,C),(B,C)\right\}\right),\{\left(\left\{A,B,C\right\},\left\{(A,B),(A,C)\right\}\right),\{\left(\left\{A,B,C\right\},\left\{(A,B),(A,C),(B,C)\right\}\right)\right\}$$


#### Examples
To see how a , the above structure can be relabled into:

<img src='https://i.ibb.co/vqw6Qqc/w-Wi-Mg-UFznzzug-Qz-M.png' width=100%  title='Graph3'>


## The Species of Permutations

#### Definition
We will be writing "Species of Permutations" as "Perm". Perm will take a finite set u, and output the set of all permutations on u:
$$Perm(U)=\left\{\left(U,f\right),f: U \rightarrow U \textrm{ bijective}\right\}$$
Essentially what this definition is saying is that the output for such finite set would be the set of all permutation structures on u, or simply all the bijections.

A Perm of a bijection from one set to another set can be expressed as:
$$Perm(u\xrightarrow[\text{}]{\sigma}v):(u,f)\mapsto (v,?)$$
We put a question mark because we do not have information on the bijection of v. Therefore, we will be use a diagram chase to find that bijection. Here is the information that we have already obtained:
<p align="center">
<img src='https://i.ibb.co/jRMwrz6/u.png' width=50%  title='Follow the Map'>

Therefore, to get from V to V we could follow the map counterclockwise. We define $ g $ to be:
$$g=\sigma(f(\sigma^{-1}(x)))$$
It follows that $ g $ must be bijective, since it is a composition of three bijections.
</p>


#### Example
$$Perm(\left\{1,2,3\right\})=\left\{\left(1,2,3\right),\left(1,3,2\right),\left(2,1,3\right),\left(2,3,1\right),\left(3,2,1\right),\left(3,1,2\right)\right\}$$


#### Example
Such example is quite similar to the bijection between finite sets for graph.
$$Perm(\left\{1,2,3\right\})=\left\{\left(1,2,3\right),\left(1,3,2\right),\left(2,1,3\right),\left(2,3,1\right),\left(3,2,1\right),\left(3,1,2\right)\right\}\text{can be mapped to:}$$
$$Perm(\left\{A,B,C\right\})=\left\{\left(A,B,C\right),\left(A,C,B\right),\left(B,A,C\right),\left(B,C,A\right),\left(C,B,A\right),\left(C,A,B\right)\right\}$$

## Conclusion

So that concludes our brief introduction of species, specifically for graphs and permutations. Later on we will talk about species addition, multiplication, and definitely some other interesting topics in random permutations. Thanks for reading!