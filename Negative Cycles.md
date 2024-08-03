Understanding a negative cycle:
![[Pasted image 20230926022139.png]]

The negative cycle is B -> C -> D -> B with a total weight of -1.

Let's say the source vertex is A. Initially, the distances are:

- d(A) = 0
- d(B) = Infinity
- d(C) = Infinity
- d(D) = Infinity

After ∣�∣−1=3∣V∣−1=3 iterations of relaxing all edges, the distances will be:

- d(A) = 0
- d(B) = 0
- d(C) = 1
- d(D) = 2

Now, when checking for negative cycles, we examine each edge:

1. For the edge $D -> B$ with weight -3, we check if $d(D)+w(D,B)<d(B)$. Substituting the values, we get $2+(−3)<02+(−3)<0$, which simplifies to $−1<0−1<0$. This condition is true, indicating a negative-weight cycle.

So, the check for negative cycles is effective because it identifies edges that, even after all relaxation steps, can still provide a shorter path, indicating a cycle with a total negative weight.