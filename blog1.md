In this post we will be talking about a new type of function called Boolean function and a concept called 'Influence'. Then we will provide some examples of Boolean functions and investigate them (and their influence) with the help of some Python scripts.

## What is a Boolean Function?
A Boolean function is defined as:
$$f:\left\{0, 1\right\}^{n}\rightarrow\left\{0, 1\right\}$$

The definition describes a function that maps an n-dimensional sets of Boolean to a single Boolean value. We will be providing concrete examples at the section "Examples of Boolean Functions and their Influence".

## What is Influence?
**The influence of one individual bits "i" on the previous $f$ is defined to be the probability that i is pivotal for a random input:**

$$\mathbf{Inf}_i[f] = \mathop{\bf Pr}_{{\boldsymbol{x}} \sim \{0,1\}^n}[f({\boldsymbol{x}}) \neq f({\boldsymbol{x}}^{\oplus i})]$$
Here is the clarification for our notations:

 - $$\mathop{\bf Pr}[...]: \text{the probability of ...}$$


 - $${\boldsymbol{x}} \sim \{0,1\}^n: \text{ x is being sampled from } \{0,1\}^n$$

 - $$f({\boldsymbol{x}}^{\oplus i}): \text{For the input string} \space(x_1, \dots, x_{i-1}, x_i, x_{i+1}, \dots, x_n), \text{we flip} \space x_i \space \text{from}\space 0 \space \text{to} \space 1 \space\text{or}\space1\space\text{to}\space0$$

To summarize, the Influence of variable "i" can be defined as the probability that when I sample "x" from the uniform measure, the value of the output is different when we flip the "i"th bit.

In my personal opinion, influence is a really good name and it perfectly describes what this concept is measuring. Essentially, influence measures how influential the variable is on the outcome of the Boolean function. We will further explain influence by giving examples and explore them in the next section.

## Total Influence
As the name suggests, the total influence is the sum of all influences such that:

$$\mathbf{I}[f] = \sum_{i=1}^n \mathbf{Inf}_i[f].$$

The total influence has several additional interpretations and hopefully I will be able to address them in a later post. For now, we would like to propose some examples of Boolean functions and calculate their influences.

## Examples of Boolean Functions and their Influence
If we search up "examples of polynomial functions", we will see a tons of examples online. Nevertheless, if we search up "examples of Boolean functions", rarely any results will show up. Therefore I would like to provide some examples of Boolean functions and investigate its influence to analyze their behaviors.

### Boolean Functions Example 1: Randomly Generate
A random Boolean functions utilize a computer program to generate a random output for each inputs. We here express an example with input length of 2 as a truth table:
| Input[1]  | Input[0]  | Random Output |
| :------------ |:---------------:| -------------:|
| 0 | 0 | 1 |
| 1 | 1 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
I wrote a Python script to **generate a Boolean function in a specific dimension**:
```
import numpy as np
import matplotlib.pyplot as plt
import math
import itertools
import random

def generate(dim):
    combinations = list(itertools.product([0, 1], repeat=dim)) 
    #provides a list of tuple with all the binary combinations with length = dim
    dict = {}
    for tuple in combinations:
        dict[tuple]=(random.getrandbits(1)) # this creates a "random function"
    return dict
```
If we want to **generate a Boolean function in two dimensions**, we simply use dim=2 as the parameter:
```
generate(2)
>>> {(0, 0): 0, (0, 1): 1, (1, 0): 1, (1, 1): 1}
generate(2)
>>> {(0, 0): 0, (0, 1): 1, (1, 0): 0, (1, 1): 1}
```
If we want **a Boolean function in three dimensions**:
```
generate(3)
{(0, 0, 0): 1,
 (0, 0, 1): 0,
 (0, 1, 0): 0,
 (0, 1, 1): 1,
 (1, 0, 0): 1,
 (1, 0, 1): 0,
 (1, 1, 0): 1,
 (1, 1, 1): 0}
```
Now we have successfully generated a Boolean function in a certain dimension, we can start investigate its influence for each bits. Here is my script to **calculate the influence when a specific bit is switched**:
```
def calculate_influence(dict, bit):
    """calculate influence when one bit is flipped, "dict" is the Boolean input"""
    count = 0
    total = 0
    for item in dict:
        original = dict[item]
        if item[bit]==0:
            item = edit_tuple(item, bit, 1)
            total += 1
        else:
            item = edit_tuple(item, bit, 0)
        if dict[item] != original:
            count += 1
            total += 1
    return count / total """return the probability, hence the influence"""
```
Let's try out this function by input a three dimensional Boolean function as our parameter and **investigate its influence at the 0th bits**:
```
function = {(0, 0, 0): 1,
            (0, 0, 1): 0,
            (0, 1, 0): 0,
            (0, 1, 1): 1,
            (1, 0, 0): 1,
            (1, 0, 1): 0,
            (1, 1, 0): 1,
            (1, 1, 1): 0}
calculate_influence(function, 0)
>>> 0.5
```
Therefore, we can conclude that for this function, the influence of the 0th bit is 50%. In other words, when the 0th bit is being switched, exactly 50% of the output will be switched as well. By running this function for each bits of the input and sum it all together, we will **output the total influence of such random Boolean function**:
```
def calculate_total_influence(dict):
    total = 0
    length = len(next(iter(dict)))
    for i in range(length):
        print ("bit" + str(i) + " has influence " + str(calculate_influence(dict, i)))
        total += calculate_influence(dict, i)
    return "total influence = " + str(total)
    
calculate_total_influence(function)
>>> bit0 has influence 0.5
    bit1 has influence 0.5
    bit2 has influence 0.6666666666666666
    'total influence = 1.6666666666666665'
```
There seems to be a pattern where each bit has an approximate influence of 0.5. However, it is not very obvious since the function is three dimensional, thus we only have 3 bits to look at. We will see a better results once we increase the dimension of our input. This time, we would like to **plot the total influence of a random Boolean function from 0 dimension to 20 dimensions**:
```
def influence_plot():
    for bits in range(21):
        x_value = bits
        dict = generate(bits)
        y_value = calculate_total_influence(dict)
        plt.scatter(x_value,y_value)
    plt.xlabel('dimensions', fontsize=16)
    plt.show()
```
<img src='https://i.ibb.co/M2hnrmL/1.png' width=900 height=450 title='Total Influence vs. Input Dimensions'>

#### Observation
Based on the output of our program and the plot, we can conclude that for a random Boolean function:

 - $$\text{The influence of each bit is usually}\space 1/2.$$
 - $$ \text{The total influence is}\space 0.5n = 0.5 + 0.5 + ... + 0.5, \space \text{where n is the dimension of our input.}$$

### Boolean Functions Example 2: Is everything equal to one?
This is a function where the output will be 0 unless all input bits are 1, below is an example of such function in three dimension:
$$f(0,0,0)=0, f(0,0,1)=0, f(0,1,0)=0, f(1,0,0)=0, f(1,1,0)=0, f(1,0,1)=0, f(0,1,1)=0, f(1,1,1)=1$$
We can construct a function that **generate a "Is everything equal to one" function in a specific dimension**:
```
def all_one_boolean_function(dim):
    """this function simulate a boolean function "Is everything equal to one?"""
    combinations = list(itertools.product([0, 1], repeat=dim)) 
    #this gives you a list of tuple with all the binary combinations with length = dim
    dict = {}
    for tuple in combinations:
        if 0 not in tuple:
            dict[tuple] = 1
        else:
            dict[tuple] = 0
    return dict
```
By using the same Python function as before, we can **plot the total influence vs. dimensions graph**:
<img src='https://i.ibb.co/R9Q3r0f/plot.png' width=900 height=450 title='Total Influence vs. Input Dimensions'>

#### Observation

 - Total Influence approaches 0 as dimensions approaches infinity, which makes sense since as dimension increases, the number of "unaffected" outcomes increase at a much faster rate than the number of "affected" outcomes.
 - The maximum total influence is 1, which happens for 2 dimensional and 3 dimensional input.


### Boolean Functions Example 3: Even or Odd?
Now we will create a Boolean function that add up all entries in mod 2. Essentially this is equivalent to identifying whether the sum is even or odd. Below are two examples illustrating this idea:

 - $$f(1,1,1,0,1,0,1)=1\space \text{since}\space1+1+1+0+1+0+1\equiv1\left(\bmod2\right)$$

 - $$f(1,1,1,0,1,1,1)=0\space \text{since}\space1+1+1+0+1+1+1\equiv0\left(\bmod2\right)$$

After we clarify the definition, we simply need to follow the same procedure as before. First we write **a function that generate such function in a certain dimension**:
```
def even_or_odd(dim):
    """this function simulate a boolean function "Even or Odd"""
    combinations = list(itertools.product([0, 1], repeat=dim)) 
    #this gives you a list of tuple with all the binary combinations with length = dim
    dict = {}
    for tuple in combinations:
        if math.fsum(tuple)%2 == 0:
            dict[tuple] = 0
        else:
            dict[tuple] = 1
    return dict
```
By using the same Python function as before, we can **plot the total influence vs. dimensions graph**:
<img src='https://i.ibb.co/tXs6BPw/plot.png' width=900 height=450 title='Total Influence vs. Input Dimensions'>

#### Observation

 - We obtained a linear relationship that looks similar to example one at first glance. This means that the graph has a constant slope.
 - However, if we look at the y-axis, the total influence is increasing faster compared to example 1. Such observation makes sense since by changing any bits of the input, an even sum turns into an odd sum and vice versa. Therefore, any bit's changes will have influence on the output. If we calculate the slope of this graph, we get exactly 2/3. For now, we can not justify why 2/3 is the slope as further investigation is needed. I would encourage the readers to investigate on the "why" and "how" of this result as well.

### Boolean Functions Example 4: Are the majority of the inputs one?
For this example, if majority of the input is one, the output would be one. Otherwise the output would be 0, including the case where the number of ones and zeroes are equal. Here are some examples:

 - $$f(1,1,1,0,1,0,1)=1\space \text{since the majority is one}$$


 - $$f(1,0,0,0,1,0,1)=0\space \text{since the majority is not one}$$

Like before, let us create the **Python function that generates Boolean functions example 5**:
```
def majority_one(dim):
    """this function simulate a boolean function "Are the majority of the inputs one"""
    combinations = list(itertools.product([0, 1], repeat=dim)) #this gives you a list of tuple with all the binary combinations with length = dim
    dict = {}
    for tuple in combinations:
        if tuple.count(1) > tuple.count(0):
            dict[tuple] = 1
        else:
            dict[tuple] = 0
    return dict
```

By using the same Python function as before, we can **plot the total influence vs. dimensions graph**:
<img src='https://i.ibb.co/9H3q9C6/plot.png' width=900 height=450 title='Total Influence vs. Input Dimensions'> 

#### Observation

 - Based on the graph with dimensions up to 20, it seems like the curve has a shape similar to a logarithmic function.


 - The rate of increase for total influence gradually slows down as dimension increases, however, it does not approach any constant value.

 - There seems to be an oscillating behavior along the curve, it would be helpful if the reader can investigate and justify the oscillating behavior.

## Conclusion
That is all for this week's post. We talked about what a Boolean function is and the definition of influence for a Boolean function. We investigated some examples of Boolean functions, plotted their influence and stated our observation. The advantage of our use of programming is that it allows us to generate our results quickly and utilize the visualization to conduct analysis. Nevertheless, the disadvantage would be the fact that it is hard to justify the shape of our curve and explain them in a mathematically sound manner. We hope in a later post, we will be able to justify and explain the curve of each examples with mathematics. Thanks for reading!
















