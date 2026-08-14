# Hopcroft-Karp Bipartite Matching Algorithm

An efficient implementation of the Hopcroft-Karp algorithm for finding maximum matchings in bipartite graphs.

## Features

- **Optimal Time Complexity**: O(E * √V) using augmenting path strategy
- **BipartiteGraph Class**: Clean object-oriented interface
- **Multiple Operations**: 
  - Find maximum matching size
  - Retrieve the actual matching
  - Add edges dynamically
- **Comprehensive Tests**: Full unit test coverage
- **Examples**: Practical usage examples

## What is Bipartite Matching?

Given a bipartite graph (two disjoint sets of vertices with edges only between sets), maximum bipartite matching finds the largest set of edges where no two edges share a vertex.

### Applications

- Job assignment (workers to tasks)
- Airline crew scheduling
- Marriage problem matching
- Flow network problems
- Network routing optimization

## Algorithm Overview

The Hopcroft-Karp algorithm uses two main phases:

1. **BFS Phase**: Find shortest augmenting paths using breadth-first search
2. **DFS Phase**: Greedily augment matching along these paths using depth-first search

This two-phase approach guarantees O(E√V) time complexity, better than simpler augmenting path methods.

## Installation

No external dependencies required. Requires Python 3.7+

```bash
git clone https://github.com/MohammadHossinzehi/hopcroft-karp-matching.git
cd hopcroft-karp-matching
```

## Usage

### Basic Example

```python
from hopcroft_karp import BipartiteGraph

# Create graph
g = BipartiteGraph()

# Add edges (left vertex, right vertex)
g.add_edge(1, 10)
g.add_edge(1, 11)
g.add_edge(2, 11)
g.add_edge(2, 12)
g.add_edge(3, 12)
g.add_edge(3, 13)

# Get maximum matching size
matching_size = g.hopcroft_karp()
print(f"Maximum matching: {matching_size}")

# Get the actual matching
matching = g.get_matching()
print(f"Matching pairs: {matching}")
```

### Output

```
Maximum matching: 3
Matching pairs: {1: 10, 2: 11, 3: 12}
```

## Testing

Run the test suite:

```bash
python tests.py
```

### Test Coverage

- Empty graphs
- Single edge
- Complete bipartite graph (K_n,n)
- Disconnected components
- Path graphs
- Cycle graphs

## Algorithm Complexity

- **Time**: O(E * √V)
- **Space**: O(V + E)

Where:
- E = number of edges
- V = total number of vertices

## Design Decisions

1. **Adjacency List Representation**: Efficient for sparse graphs
2. **Nested Functions**: BFS and DFS are problem-specific
3. **Dictionary Matching**: O(1) lookup for matched vertices
4. **Separate Methods**: get_matching() provides flexibility

## Future Enhancements

- Weighted bipartite matching (Hungarian algorithm)
- Maximum flow wrapper
- Visualization utilities
- PyPy/Cython optimization

## References

- Hopcroft, J. E., & Karp, R. M. (1973). "An n^2.5 Algorithm for Maximum Matchings in Bipartite Graphs"
- Diestel, R. (2005). "Graph Theory" (3rd ed.)
- CLRS. "Introduction to Algorithms" (3rd ed.)

## License

MIT License

## Author

Mohammad Hossinzehi
