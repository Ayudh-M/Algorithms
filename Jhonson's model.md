Johnson(G, w)
V* ← V ∪ {s}
E* ← E ∪ { (s,u) : u in V }; all new edges (s,u) get weight 0
Run Bellman-Ford(G*, s) to compute distances δ(s,u) for all u in V
if Bellman-Ford reports that G* has negative-weight cycle
    then report "G has negative-weight cycle"
else 
    Let G = (V, E) be the same graph as G, but with edge weights w(u,v) = w(u,v) + δ(s,u) - δ(s,v)
    for each vertex u in V
        do Run Dijkstra(G, u) to compute distances δ(u,v)


In this pseudocode:

1. **Johnson**: This is the main function for executing Johnson's algorithm on a graph G with edge weight function w.
2. __V_ and E_**: These are the sets of vertices and edges in the modified graph ∗G∗, which includes all elements of G plus a new vertex s and edges from s to every vertex in G.
3. **s**: This is a new vertex added to create ∗G∗ from G.
4. **u and v**: These are vertices in the graph.
5. **w(u,v)**: This is the original weight of the edge from u to v.
6. **δ(s,u) and δ(u,v)**: These are the reweighted distances used to eliminate negative weights and compute shortest path distances, respectively.
7. **Bellman-Ford**: This function is called to compute the reweighting function δ that will be used to eliminate negative edge weights.
8. **Dijkstra**: This function is called to compute the shortest path distances in the reweighted graph G from each vertex u to every other vertex v.


// Johnson's Algorithm to reweight the edges of a graph G to eliminate negative weights and then solve the all-pairs shortest paths problem.
// G is the original graph, and w is the function that gives the weight of each edge in G.

Johnson(G, w)
// This function is the main function for Johnson's algorithm.

// Modify G into graph G* by adding vertex s with edges to all other vertices.
V* ← V ∪ {s}  // V* is the set of vertices in G*, which includes all vertices in G plus a new vertex s.
E* ← E ∪ { (s,u) : u in V }  // E* is the set of edges in G*, which includes all edges in G plus new edges from s to every vertex in G. All new edges (s,u) get weight 0.

// Use G* to transform G to a graph G that has no negative edge weights.
Run Bellman-Ford(G*, s) to compute distances δ(s,u) for all u in V  // Run Bellman-Ford on G* with source vertex s to compute the reweighting function δ.
if Bellman-Ford reports that G* has negative-weight cycle
    then report "G has negative-weight cycle"  // If G* has a negative-weight cycle, then G also has a negative-weight cycle.
else 
    // Let G = (V, E) be the same graph as G, but with reweighted edge weights.
    Let G = (V, E) be the same graph as G, but with edge weights w(u,v) = w(u,v) + δ(s,u) - δ(s,v)  // Reweight the edges of G using the reweighting function δ.
    for each vertex u in V  // Compute distances to all other vertices from each vertex u.
        do Run Dijkstra(G, u) to compute distances δ(u,v)  // Run Dijkstra's algorithm on the reweighted graph G from each vertex u to compute the shortest path distances δ(u,v).

// In this pseudocode:
// δ(s,u) and δ(u,v) are the reweighted distances used to eliminate negative weights and compute shortest path distances, respectively.
// V and E are the sets of vertices and edges in the original graph G, respectively.
// V* and E* are the sets of vertices and edges in the modified graph G*, respectively.
// s is a new vertex added to create G* from G.
// u and v are vertices in the graph.
// w(u,v) is the original weight of the edge from u to v.
