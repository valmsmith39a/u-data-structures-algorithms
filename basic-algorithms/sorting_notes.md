sorting

    in-place
        
        rearrange, so don't have to copy data into another data structure

        usually higher run-time but lower space complexity

    not in-place

        copy data into another data structure

        usually lower run-time but greater space complexity

types

    bubble sort

        naive approach

        run-time: 
            
            average case: (n-1)(n-1) = n^2 + 2n + 1 => O(n^2)

            best case: O(n) if only 1 number needed to be bubbled up or already in correct order
            
        space complexity: O(1) bc don't need extra data structures

    merge sort

        divide and conquer

        lower run-time, greater space compexity

        run-time: n comparisons for log n steps => O( n log n)

        space complexity: auxilary space = O(n), because copying into new arrays

        number of inversions:

            number of pairs of numbers that are inversted (out of order)

    quick sort

        divide and conquer

        don't use if array almost sorted, bc will lead to worst case

        best case is when pivots moved to center

        run-time:

            average: O(n log n)

            worst case: O (n)

        space complexity:

            sorting in-place, so no extra space, so O(1)


    heap sort

        


    

