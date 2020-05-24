"""
Shortest Path Problem

Find the shortest path in a graph

Weighted edges: each edge has a numeric value 

Shortest path: minimize sum of edges 

For unweighted graph (edges do not have a weight):

    Shortest path is just the number of edges

    Shortest path would be a BFS 

Dijkstra's Algorithm

    Find shortest path for weighted, undirected graph

    Distance value: sum of edge weights from starting node to current node 

    End of algorithm, distance is the distance of the shortest path

    Starting distance for each node is infinity

    Use a min priority queue

        Element with minimum priority (distance) removed efficiently 

        Extract Min: Store all nodes in minimum priority queue and use extract min to remove the minumum element 

        First node has distance of 0

        What is next node to visit? 

            node with the smallest distance value

            run extract min on the queue


    Dijkstra is a greedy algorithm (pick the best option at each step) because always pick node with smallest distance value 

    Run-time of dijkstras: O(|v|^2)

        if priority queue is implemented really efficiently, the run-time is:
            O(|E| + |V| log (|v|) )

    Dijkstra does not work with:
        negative weights
        negative cycles (directed graphs where traversing a node reduces distance)

"""
