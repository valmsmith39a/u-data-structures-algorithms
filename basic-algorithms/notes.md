binary search

run-time

* Every time double the size of the array, increase the number of times you search by 1 

* Each time increment the exponent of base 2, (2^n), increase the number of times you search by 1

* Want something like: (The exponent of base 2) + 1

* Ex. 2^3 = 8 Another way to represent is log 8 = 3, so we can represent 3 as log 8 or log n

* Ex 8 * (1/2)^3 = 1 

* General equation would be: n * (1/2)^s

* Solve for s to get s = log (n)

* Runtime of binary search is: O (log n)

* Can create a results table to help compute run-time. Ex. Array Size and Number of iterations



