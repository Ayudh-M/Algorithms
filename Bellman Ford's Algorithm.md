Bellman-Ford(G, s)
Initialize-Single-Source(G, s)
for i ← 1 to |V| - 1
    do for each edge (u, v) in E
        do Relax(u, v)
for each edge (u, v) in E
    do if d(u) + w(u, v) < d(v)
        then report "Negative-weight cycle reachable from s"


pseudocode:

1. **Bellman-Ford**: This is the main function for executing the Bellman-Ford algorithm on a graph `G` with a source vertex `s`.
2. **Initialize-Single-Source**: This is a function that initializes the distance and predecessor for each vertex in the graph.
3. **i**: This is a variable used to control the outer loop, which iterates `|V| - 1` times, where `|V|` is the number of vertices in the graph.
4. **u and v**: These are vertices in the graph. `u` is the starting vertex of an edge, and `v` is the ending vertex of an edge.
5. **Relax**: This is a function that checks if the path to vertex `v` can be improved by going through vertex `u`, and updates the distance and predecessor of `v` if a shorter path is found.
6. **d(u) and d(v)**: These represent the current known distances of vertices `u` and `v` from the source vertex `s`, respectively.
7. **w(u, v)**: This represents the weight of the edge from vertex `u` to vertex `v`.
8. **π(v)**: This represents the predecessor of vertex `v` in the shortest path from `s` to `v`.
9. **E**: This represents the set of edges in the graph `G`.
10. **|V|**: This represents the number of vertices in the graph `G`.


the longest simple (non-cyclic) path from the source vertex to any other vertex can have at most $∣V∣−1$ edges. Therefore, by iterating $∣V∣−1$ times and relaxing all edges during each iteration, the algorithm guarantees that all shortest path distances are accurately computed, provided there are no negative cycles in the graph.

the Bellman-Ford algorithm, every edge in the graph G is relaxed ∣V∣−1 times, where ∣V∣ is the number of vertices in the graph. This process ensures that the algorithm correctly computes the shortest path distances from the source vertex to all other vertices, even if there are negative weight edges in the graph.

[[Negative Cycles]]

Finally:
[[Jhonson's model]]
