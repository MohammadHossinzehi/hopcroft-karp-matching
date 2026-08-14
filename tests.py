"""
Unit tests for Hopcroft-Karp algorithm implementation.

Tests cover various graph structures and edge cases to ensure
the algorithm correctness and edge handling.
"""

import unittest
from hopcroft_karp import BipartiteGraph


class TestHopcroftKarp(unittest.TestCase):
    """Test suite for Hopcroft-Karp bipartite matching."""
    
    def test_empty_graph(self):
        """Test matching on empty graph."""
        g = BipartiteGraph()
        self.assertEqual(g.hopcroft_karp(), 0)
        self.assertEqual(g.get_matching(), {})
    
    def test_single_edge(self):
        """Test matching with single edge."""
        g = BipartiteGraph()
        g.add_edge(1, 10)
        self.assertEqual(g.hopcroft_karp(), 1)
        matching = g.get_matching()
        self.assertEqual(matching[1], 10)
    
    def test_complete_bipartite_k2_2(self):
        """Test complete bipartite graph K_2,2."""
        g = BipartiteGraph()
        g.add_edge(1, 10)
        g.add_edge(1, 11)
        g.add_edge(2, 10)
        g.add_edge(2, 11)
        self.assertEqual(g.hopcroft_karp(), 2)
    
    def test_complete_bipartite_k3_3(self):
        """Test complete bipartite graph K_3,3."""
        g = BipartiteGraph()
        for i in range(1, 4):
            for j in range(10, 13):
                g.add_edge(i, j)
        self.assertEqual(g.hopcroft_karp(), 3)
    
    def test_chain_graph(self):
        """Test matching on chain graph (path)."""
        g = BipartiteGraph()
        edges = [(1, 10), (2, 11), (3, 12)]
        for u, v in edges:
            g.add_edge(u, v)
        self.assertEqual(g.hopcroft_karp(), 3)
    
    def test_star_graph(self):
        """Test matching on star graph (center to leaves)."""
        g = BipartiteGraph()
        center = 1
        for i in range(10, 15):
            g.add_edge(center, i)
        self.assertEqual(g.hopcroft_karp(), 1)
    
    def test_disjoint_components(self):
        """Test matching on graph with disjoint components."""
        g = BipartiteGraph()
        # Component 1
        g.add_edge(1, 10)
        g.add_edge(1, 11)
        g.add_edge(2, 11)
        # Component 2
        g.add_edge(3, 20)
        g.add_edge(4, 21)
        self.assertEqual(g.hopcroft_karp(), 3)
    
    def test_no_perfect_matching(self):
        """Test graph where perfect matching doesn't exist."""
        g = BipartiteGraph()
        g.add_edge(1, 10)
        g.add_edge(2, 10)
        # Right vertex 10 can only match one of 1 or 2
        self.assertEqual(g.hopcroft_karp(), 1)
    
    def test_matching_correctness(self):
        """Verify returned matching has no conflicts."""
        g = BipartiteGraph()
        edges = [
            (1, 10), (1, 11),
            (2, 11), (2, 12),
            (3, 12), (3, 13)
        ]
        for u, v in edges:
            g.add_edge(u, v)
        
        matching = g.get_matching()
        
        # Check each left vertex appears at most once
        self.assertLessEqual(len(matching), 3)
        
        # Check each value (right vertex) is unique
        values = list(matching.values())
        self.assertEqual(len(values), len(set(values)))
        
        # Check all edges in matching exist
        for u, v in matching.items():
            self.assertIn(v, g.graph[u])
    
    def test_large_complete_bipartite(self):
        """Test on larger complete bipartite graph."""
        n = 20
        g = BipartiteGraph()
        for i in range(1, n + 1):
            for j in range(100, 100 + n):
                g.add_edge(i, j)
        self.assertEqual(g.hopcroft_karp(), n)
    
    def test_matching_different_sizes(self):
        """Test various graph sizes."""
        for size in [1, 2, 3, 5, 10]:
            g = BipartiteGraph()
            for i in range(1, size + 1):
                g.add_edge(i, 100 + i)
            self.assertEqual(g.hopcroft_karp(), size)
    
    def test_duplicate_edges(self):
        """Test that duplicate edges don't affect matching."""
        g = BipartiteGraph()
        g.add_edge(1, 10)
        g.add_edge(1, 10)  # Add same edge again
        g.add_edge(2, 11)
        self.assertEqual(g.hopcroft_karp(), 2)


class TestBipartiteGraphProperties(unittest.TestCase):
    """Test properties of BipartiteGraph class."""
    
    def test_graph_initialization(self):
        """Test proper graph initialization."""
        g = BipartiteGraph()
        self.assertEqual(len(g.left_vertices), 0)
        self.assertEqual(len(g.right_vertices), 0)
    
    def test_vertices_tracking(self):
        """Test that vertices are properly tracked."""
        g = BipartiteGraph()
        g.add_edge(1, 10)
        g.add_edge(2, 11)
        self.assertIn(1, g.left_vertices)
        self.assertIn(2, g.left_vertices)
        self.assertIn(10, g.right_vertices)
        self.assertIn(11, g.right_vertices)
    
    def test_adjacency_list(self):
        """Test adjacency list structure."""
        g = BipartiteGraph()
        g.add_edge(1, 10)
        g.add_edge(1, 11)
        self.assertEqual(len(g.graph[1]), 2)
        self.assertIn(10, g.graph[1])
        self.assertIn(11, g.graph[1])


if __name__ == '__main__':
    unittest.main()
