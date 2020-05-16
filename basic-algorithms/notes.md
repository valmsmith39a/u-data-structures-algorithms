binary search

run-time

* Every time double the size of the array, increase the number of times you search by 1 

* Each time increment the exponent of base 2, (2^x), increase the number of times you search by 1

* Want something like: (The exponent of base 2) + 1

* Ex. 2^3 = 8 Another way to represent is log 8 = 3, so we can represent 3 as log 8 or log n

* Ex 8 * (1/2)^3 = 1 

* General equation would be: n * (1/2)^s

* Solve for s to get s = log (n)

* Runtime of binary search is: O (log n)

* Can create a results table to help compute run-time. Ex. Array Size and Number of iterations


Trie: type of binary tree

Heaps:

* Binary min-heap

* Binary max-heap

* Search in a binary tree: O(n)
* Worst case: O(1/2 n)

* Tips for binary max-heap:

+ If target is larger than node, skip the sub-trees

+ Insert/Extract: O (log n) in the worst case

Trees

* Balanced tree: Nodes condensed to only a few levels

* Unbalanced tree: Nodes spread out among many levels

* Extreme unbalanced tree: Linked List 

* Self balancing tree: use as few levels as possible using insert/delete



