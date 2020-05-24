Agents that can plan ahead and solve problems

Route Finding

Problem Definition

    initial state (s0): starting point of the agent 

    Actions (s): function that takes a state as input and returns set of possible actions agent can execute when agent is in this state 

        same action for all states, or different actions dependent on the state 

        input: s: state

        output: {a0, a1, a2,...}: set of possible actions agent can execute when agen is in this state 

    Result (s, a): function that takes state and action and outputs a new state (s')
        
        ex. Agent in one city (initial state), takes left route (action), ends up in a new city (new state)

        input: state, action

        output: s': new state 

    Goal Test(s) -> True/False: function that takes state and returns True/False indicating if goal achieved 
        
        input: state 

        output: boolean value indicating if goal achieved or not 

                  aj     aj+1
    Path Cost (si -> si+1 -> si+2) => cost value (n), where i = 0, 1, 2..., j = 1, 2...

        input: state, action transitions

        output: cost of that path. additive: cost is sum of the costs of the individual steps

    Step Cost (s, a, s') -> n 

        input: state, action, next state

        output: n: cost of that action 

        Ex. route finding: cost may be number of miles, or time takes to get to destination 


State space: all the possible states (cities)

    actions are specific to each city 

    as we follow the actions, we build paths (sequences of actions)


Frontier: ends of the paths - the farthest out of exploration, but haven't explored yet 

Explored part of state 

Unexplored part of the state 

Step cost between cities labeled

Path cost: sum of step costs 

Uniform Cost Search: Cheapest First

    Find the cheapest cost path

Greedy Best First Search:
    
    Get an estimate of the distance between 2 cities

If there is a barrier:
Want to combine Greedy Search (explores small number of nodes in many cases) and Uniform Cost Search which is guaranteed to find the shortest path
     
Uniform Cost search - expands out equally in all directions, may expend additional effort getting to a fairly direct path to the goal.

Greedy best-first search - expands outward toward locations estimated as closer to the goal. If a direct path is available, expends much less effort than Uniform Cost; however, it does not consider any routes in which it may need to temporarily take a further away path in order to arrive at an overall shorter path.

A* Search - utilizes both of these - will try to optimize with both the shortest path and the goal in mind. We'll see how this works in the next video.

A* Search

    Expands the path that has the minimum  value of the function f = g + h 

    f = g + h

    g(path): function returns the cost of the path

    h(path): h(s): function returns the estimated distance (cost) to the goal 

    finds the minimum length path while expanding minimum number of paths possible

    "best estimated total path cost first"

    A* will find the lowest cost if h(s) < true cost.

        h should never overestimate distance to the goal 

        h is "optimistic" and "admissible"





 

