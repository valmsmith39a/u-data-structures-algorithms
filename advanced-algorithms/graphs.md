graphs

    data structure to show relationships between objects

    show how different things connected to one another 

    also called networks

    similar to tree

    node (vertex)

    tree is a specific type of graph

    adjacent nodes: 2 nodes connected by an edge

    edges can contain information too

    possible to have 2 edge, for ex, travelling to and from a node

    undirected graph: no sense of direction

    graphs can have cycles but trees can't. be careful of cyles - infite loops 

        make sure graph taking in is acyclic: has no cycles 

    DAG: Directed Acylcic Graph: Directed Graph with no cycles 

    Graph Theory

        Connectivity

        Disconnected graph: 

            has some node (vertex) that cannot be reached by other nodes (vertices) 

        Connected graph:

            has *no* disconnected nodes (vertices)

        Connectivity: 

            minimum number of edges for a graph to become disconnected 

            can answer the question: which graph is stronger? 


Vertex object

    Ex name: , id: 

    Can be connected to edges 

Edge object

    Ex strength: , id: 


Edge list (2D list - 2 dimensional listk)

    List of edge k

    Graph with 

    0 - 1 - 3 - 2

    Ex [[0, 1], [1, 2], [1, 3]]

    Each pair is id numbers of vertices that the edge connects 

Adjacency list (2D list)

    [[1], [0, 2, 3], [1, 3], [1, 2]]

Adjacency Matrix

    [[1, 0, 0, 0],
     [0, 1, 1, 1],
     [1, 0, 1, 0]]

Graph Traversal: Intro

    Graphs good for modeling connections between elements 

    Graphs are easy to traverse based on connections 

    Graph traversal similar to Tree traversal. Remember Tree is specific type of graph. 

    Depth first search: follow 1 path as far as it will go 

    Breadth first search: look at nodes adjacent to each other before moving on to the next level 

Graph Traversal: Depth First Search (DFS - Stack)

    1. Begin with any node

    2. Mark node you have selected as "Seen"

    3. Use a Stack to track seen nodes 

    4. Pick an edge, mark that node as "Seen"

    5. More edges/unseen nodes, keep repeating k

    6. If go back to a node seen before, go back to previous node and try another edge 

    7. If no more edges with new nodes, pop the node from the stack, go back to the node before it (next one on the stack)


Graph Traveral: DFS - Recursion 

    1. When run out of new nodes to explore, you've hit base case 

    2. Then go back up level of recursion which is the previous node 

    3. Visit every edge and vertex once

        Run-time is: O(|E| + |V|)





            

            