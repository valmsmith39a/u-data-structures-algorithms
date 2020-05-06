binary search

    use on ordered from list of elements


binary tree

    to search for an element: 
        
        worst case: O(n), because tree could be unbalanced (worst cases being linked list)

        average case: O(1/2 n)

heaps

    max heap: node > child node, root node is largest

    min heap: node < child node, root node is smallest

    heap insert/remove: O(log n)


balanced tree

    uses as few levels as possible


unbalanced tree

    nodes are spread out using many levels

Red Black tree

    5 rules to ensure tree never gets too unbalanced
        1. all nodes have a color (red/black)
        2. all nodes have 2 children (NULL nodes)
            a. all NULL nodes are black
        3. if a node is red, it's children must be black
        4. root node must be black (optional)
        5. Every path's descendent must contain same number of black nodes

    insert: O(log n), because tree is kept balanced, run-time not as large as regular binary tree.
