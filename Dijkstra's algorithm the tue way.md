Graph terminology
V = set of vertices 
E = set of edges (or: arcs)

in a weighted graph every edge $(u,v)$ has a weight $w(u,v)$

there are 2 ways to represent graphs:
adjacency matrix
adjacency list

Shortest paths:
weight or length of a path = sum of edge weights 

$\delta (u,v)$ 
= shortest distance from u to v
= min weight of all paths from u to v
= they like calling the first node $s$

$d(v)$: stores distance from the source to a vertex $v$ 
if $v$ not reachable: $\delta(s,v)=\infty$
$\pi(v)$ :  is the predecessor of of some vertex v on the path from $s$ to $v$ 

code
=

Initialize-Single-Source(G, s)
S ← empty set
Put all vertices v ∈ V in min-priority queue Q, with d(v) as key
while Q is not empty
    do u ← Extract-Min(Q)
    S ← S ∪ {u}
    for each outgoing edge (u, v) from vertex u
        do Relax(u, v)

Relax(u, v)
    if d(v) > d(u) + w(u, v)
        then d(v) ← d(u) + w(u, v)
             π(v) ← u


In this pseudocode:

1. `Initialize-Single-Source` is a function that initializes the distance and predecessor for each vertex.
2. `S` is a set to keep track of vertices whose shortest distance from the source has been determined.
3. `Q` is a min-priority queue that holds all vertices, prioritized by their current known distance from the source.
4. `u` and `v` are vertices in the graph.
5. `Relax` is a function that checks if the path to vertex `v` can be improved by going through vertex `u`.
6. `d(v)` represents the current known distance of vertex `v` from the source vertex `s`.
7. `w(u, v)` represents the weight of the edge from vertex `u` to vertex `v`.
8. `π(v)` represents the predecessor of vertex `v` in the shortest path from `s` to `v`.

simple path: a path that doesnt go over the number of vertexes in a graph 

next we have [[Bellman Ford's Algorithm]]
