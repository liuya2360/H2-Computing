# Graph Theory 
## Djikstra 
> https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm  

### Brief Description   
Dijkstra's algorithm to find the shortest path between a and b. It picks the unvisited vertex with the lowest distance, calculates the distance through it to each unvisited neighbor, and updates the neighbor's distance if smaller. Mark visited when done with neighbors.

### Pseudocode 
```
function Dijkstra(Graph, source):

      create vertex set Q

      for each vertex v in Graph:             
          dist[v] ← INFINITY                  
          prev[v] ← UNDEFINED                 
          add v to Q                      
      dist[source] ← 0                        
      
      while Q is not empty:
          u ← vertex in Q with min dist[u]    
                                              
          remove u from Q 
          
          for each neighbor v of u:           // only v that are still in Q
              alt ← dist[u] + length(u, v)
              if alt < dist[v]:               
                  dist[v] ← alt 
                  prev[v] ← u 

      return dist[], prev[]
```


## Floyd-Warshall  
> https://en.wikipedia.org/wiki/Floyd–Warshall_algorithm  

### Brief Description  
Flopd-Warshall algorithm is an algorithm for finding **shortest paths** in a **weighted** graph with **positive** or **negative** edge weights (but with no negative cycles).

### Pseudocode 
```
1 let dist be a |V| × |V| array of minimum distances initialized to ∞ (infinity)
2 for each edge (u,v)
3    dist[u][v] ← w(u,v)  // the weight of the edge (u,v)
4 for each vertex v
5    dist[v][v] ← 0
6 for k from 1 to |V|
7    for i from 1 to |V|
8       for j from 1 to |V|
9          if dist[i][j] > dist[i][k] + dist[k][j] 
10             dist[i][j] ← dist[i][k] + dist[k][j]
11         end if
```

## Topological Sort 
> https://en.wikipedia.org/wiki/Topological_sorting  

### Pseudocode (Depth-first search) 
```
L ← Empty list that will contain the sorted nodes
while exists nodes without a permanent mark do
    select an unmarked node n
    visit(n)

function visit(node n)
    if n has a permanent mark then return
    if n has a temporary mark then stop   (not a DAG)
    mark n with a temporary mark
    for each node m with an edge from n to m do
        visit(m)
    remove temporary mark from n
    mark n with a permanent mark
    add n to head of L
```

### Example Qustions 
> https://dunjudge.me/analysis/problems/104/

