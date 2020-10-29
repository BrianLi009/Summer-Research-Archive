#!/usr/bin/python3

import string;
import random;
from queue import Queue;

deBruijn=[0,0,0,1];

N = 0;

# Using the following table of primitive polynomials:
#  https://baylor-ir.tdl.org/bitstream/handle/2104/8793/GF3%20Polynomials.pdf?sequence=1&isAllowed=y
# Prepared by Peter M. Maurer of Baylor University
# Degree 2 
# 112 122 
# Degree 3 
# 1021 1121 1201 1211

while N < 27-4:
    deBruijn.append((deBruijn[-2] + 2*deBruijn[-3]) % 3); 
    N += 1;

#x^3 + 2x + 1 is irreducible in F_3(x)
#x^3 + 2x^2 + 1 is irreducible in F_3(x)
#AND both are primitive (1021) and (1201).

# The details of this construction appear in:
# De Bruijn Sequences-A Model Example of the Interaction of Discrete Mathematics and Computer Science by Anthony Ralston in Mathematics Magazine Vol. 55, No. 3 (May, 1982), pp. 131-143 

window_length=3;
def CheckdeBruijn(deck):
    deBruijn=True;
    lookup_table = dict();
    for i in range(0,len(deck) - window_length + 1):
        cards = list(deck[i:i+window_length]);
        if not(str(cards) in lookup_table):
            lookup_table[str(cards)] = i;
        else:
            print("Repeat of " + str(cards) + " at " + str(i));
            deBruijn=False;
            return deBruijn;
    return deBruijn;

print("Is the list de Bruijn? " + str(CheckdeBruijn(deBruijn)));
print("How long is the list? " + str(len(deBruijn)));
print(deBruijn);
