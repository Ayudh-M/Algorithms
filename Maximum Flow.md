Basic Flow concepts:
- **Flow conservation** property: The rate at which material enters a vertex must equal the rate at which it leaves the vertex.
- what is the **Maximum-flow problem**?
  In the maximum-flow problem, we wish to compute the greatest rate at which we can ship material from the source to the sink without violating any capacity constraints


- When there is 2 vertices that are connected with nothing we say they are connected with an edge of capacity 0.
- flow networks are not allowed to have anti parallel edges:
  ![[Pasted image 20231011182207.png]]
  but you can put a node in the middle and make it go back

the total flow input is mathamatically legal since you can have flow going in be 0 and going out be 0 and then you are going to have some cycle inside that ultimately ends up as 0 so like a cycle of flow.

![[Pasted image 20240120223913.png]]
![[Pasted image 20240120224234.png]]