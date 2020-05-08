divide and conquer

    find median without first sorting the list

    another interpretation: n elements, find the kth smallest of A, set k = n/2

    Easy: sort elements, output kth element, O(nlogn) time (merge sort)

    Now: no sorting, O(n) time

quick sort comparison

    also divide/conquer

    bad pivot: smallest or largest bc then O(n^2) time. 
    
    good pivot: median 

    O(nlogn) time


approach

    choose a pivot, p

    3 buckets a < p, a == p, a > p

    depending on k searching for, we know which bucket it's in

    [2, 4, 6] [7, 7] [8, 9, 13, 15]

    k <= 3, then k in bucket 1

    k is 4, 5, then k is 7

    k is 6 - 9, then k is in bucket 3

want O(n) time

    if smallest or largest, will get O(n^2) time

    if median, then will be O(n/2) time => O(n)

    if band, O(n/4), O(3/4n) => O(n)

    if pivot is within any band that is some fraction of n at smallest/largest, will get O(n) time

    Ex. O(n/100), O(99/100n) => O(n)

    Definition of a "good" pivot: n/4, 3n/4

Key is to find a good pivot in O(n) time

    then T(n) = T(3/4 n) + O(n) => O(n)

    T (3/4 n) is run-time to search using pivot

    O(n) is the run-time to find the pivot

    O(n) to partition into 3 buckets

Slack

    3/4 n would be good, but actually up to 99/100 n would be good

    We have extra "slack" of 24/100 n

    Use this slack to find a good pivot

    O(n) + O(n/24) time to find a good pivot

    T(n) = T(3n/4) + T(n/5) + T(n)
            1           2       3
           k 
    2, 3 used to find a good pivot 

How

    Choose a subset of A, called s, where size is n / 5

    then run the median algorithm on this subset s

    Find the median of this subset s, which will be runtime of T (n/5)

    Need subset S to be a representative sample of array A



