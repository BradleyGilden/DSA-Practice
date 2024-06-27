# Graphs

Graph data structures are a way of representing relationships between pairs of objects. In a graph, objects are represented as nodes (or vertices), and the relationships between these objects are represented as edges (or links). Graphs are used in various fields, such as computer science, mathematics, and engineering, to model and solve problems involving interconnected data.

Here are the key components and types of graphs:

1. **Nodes (Vertices)**: The fundamental units of a graph, representing entities.

2. **Edges**: The connections between nodes. Edges can be directed or undirected. They represent relationships between the entities.

3. **Types of Graphs**:
   - **Undirected Graph**: Edges have no direction. The connection between two nodes is bidirectional. <p align="center"><img width="400" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Undirected_graph.svg/347px-Undirected_graph.svg.png?20060311152740"></p>

   - **Directed Graph (Digraph)**: Edges have a direction, indicating a one-way relationship from one node to another. <p align="center"><img width="400" src="https://upload.wikimedia.org/wikipedia/commons/2/23/Directed_graph_no_background.svg"></p>

   - **Weighted Graph**: Edges have weights (or costs) associated with them, representing the strength or capacity of the connection. <p align="center"><img width="400" src="https://upload.wikimedia.org/wikipedia/commons/f/f0/Weighted_network.svg"></p>

   - **Unweighted Graph**: All edges are considered equal, with no weights. (See first two figures)
   - **Cyclic Graph**: Contains at least one cycle, a path where the first and last nodes are the same. <p align="center"><img width="300" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Graph_cycle.svg/1200px-Graph_cycle.svg.png"></p>

   - **Acyclic Graph**: Contains no cycles (See figure 1-3).

   - **Connected Graph**: There is a path between any two nodes (See figure 1-4).

   - **Disconnected Graph**: At least one pair of nodes does not have a path connecting them. <p align="center"><img width="400" src="https://www.tutorialspoint.com/discrete_mathematics/images/unconnected_graph.jpg" /></p>

   - **Tree**: A special type of acyclic, connected graph where any two nodes are connected by exactly one path.
  
  (N.B 4th graph is not a tree due to a cycle) <p align="center"><img width="500" src="https://miro.medium.com/v2/resize:fit:1400/1*29CZ_RNJl_05PdPDCLqcFg.png" /></p>

   - **DAG (Directed Acyclic Graph)**: A directed graph with no cycles, often used to represent processes with dependencies. <p align="center"><img width="500" src="https://miro.medium.com/v2/resize:fit:1400/1*Fi1AZPZLrGf-6wM_wTSPQw.png" /></p>

4. **Graph Representations**:
   - **Adjacency Matrix**: A 2D array where rows and columns represent nodes, and the presence or absence of an edge is indicated by the value at the intersection of a row and column. <p align="center"><img width="500" src="https://mathworld.wolfram.com/images/eps-svg/AdjacencyMatrix_1002.svg" /></p>

   - **Adjacency List**: An array or list where each index represents a node and contains a list of nodes to which it is connected. <p align="center"><img width="500" src="https://media.geeksforgeeks.org/wp-content/uploads/20230727155209/Graph-Representation-of-Directed-graph-to-Adjacency-List.png" /></p>

   - **Edge List**: A list of all edges, where each edge is represented by a pair (or tuple) of nodes. <p align="center"><img width="500" src="https://storage.googleapis.com/algodailyrandomassets/curriculum/graphs/implementing-graphs-graph.png" /></p>

Graphs are used in various applications, such as social networks (to represent relationships between people), web page linking (to represent hyperlinks between web pages), transportation networks (to represent routes and connections), and many algorithms (like Dijkstra's shortest path, depth-first search, and breadth-first search) to solve complex problems.
