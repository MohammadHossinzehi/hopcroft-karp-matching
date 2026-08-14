"""
Hopcroft-Karp Algorithm for Maximum Bipartite Matching.

Efficient algorithm for finding maximum matching in bipartite graphs.
Time complexity: O(E * sqrt(V))
"""

from collections import defaultdict, deque
from typing import Dict, List, Tuple, Set


class BipartiteGraph:
    """Represents a bipartite graph with two sets of vertices."""
    
    def __init__(self):
        self.graph = defaultdict(list)
        self.left_vertices = set()
        self.right_vertices = set()
    
    def add_edge(self, u: int, v: int) -> None:
        """Add an edge from left vertex u to right vertex v."""
        self.graph[u].append(v)
        self.left_vertices.add(u)
        self.right_vertices.add(v)
    
    def hopcroft_karp(self) -> int:
        """
        Find maximum matching using Hopcroft-Karp algorithm.
        
        Returns:
            The size of the maximum matching
        """
        match_left = {}
        match_right = {}
        
        def bfs() -> bool:
            """BFS to find augmenting paths."""
            queue = deque()
            dist = {}
            
            for u in self.left_vertices:
                if u not in match_left:
                    dist[u] = 0
                    queue.append(u)
                else:
                    dist[u] = float('inf')
            
            dist[None] = float('inf')
            
            while queue:
                u = queue.popleft()
                if dist[u] < dist[None]:
                    for v in self.graph[u]:
                        match_u = match_right.get(v, None)
                        if dist.get(match_u, float('inf')) == float('inf'):
                            dist[match_u] = dist[u] + 1
                            if match_u is not None:
                                queue.append(match_u)
            
            return dist[None] != float('inf')
        
        def dfs(u: int) -> bool:
            """DFS to find augmenting paths."""
            if u is not None:
                for v in self.graph[u]:
                    match_u = match_right.get(v, None)
                    if dist.get(match_u, float('inf')) == dist.get(u, 0) + 1:
                        if dfs(match_u):
                            match_left[u] = v
                            match_right[v] = u
                            return True
                dist[u] = float('inf')
                return False
            return True
        
        matching_size = 0
        while bfs():
            dist = {}
            for u in self.left_vertices:
                if u not in match_left:
                    if dfs(u):
                        matching_size += 1
        
        return matching_size
    
    def get_matching(self) -> Dict[int, int]:
        """
        Get the maximum matching.
        
        Returns:
            Dictionary mapping left vertices to matched right vertices
        """
        match_left = {}
        match_right = {}
        
        def bfs() -> bool:
            queue = deque()
            dist = {}
            
            for u in self.left_vertices:
                if u not in match_left:
                    dist[u] = 0
                    queue.append(u)
                else:
                    dist[u] = float('inf')
            
            dist[None] = float('inf')
            
            while queue:
                u = queue.popleft()
                if dist[u] < dist[None]:
                    for v in self.graph[u]:
                        match_u = match_right.get(v, None)
                        if dist.get(match_u, float('inf')) == float('inf'):
                            dist[match_u] = dist[u] + 1
                            if match_u is not None:
                                queue.append(match_u)
            
            return dist[None] != float('inf')
        
        def dfs(u: int) -> bool:
            if u is not None:
                for v in self.graph[u]:
                    match_u = match_right.get(v, None)
                    if dist.get(match_u, float('inf')) == dist.get(u, 0) + 1:
                        if dfs(match_u):
                            match_left[u] = v
                            match_right[v] = u
                            return True
                dist[u] = float('inf')
                return False
            return True
        
        while bfs():
            dist = {}
            for u in self.left_vertices:
                if u not in match_left:
                    dfs(u)
        
        return match_left


if __name__ == "__main__":
    # Example usage
    g = BipartiteGraph()
    
    # Create a bipartite graph
    edges = [
        (1, 10), (1, 11),
        (2, 11), (2, 12),
        (3, 12), (3, 13),
        (4, 13), (4, 14)
    ]
    
    for u, v in edges:
        g.add_edge(u, v)
    
    matching_size = g.hopcroft_karp()
    print(f"Maximum matching size: {matching_size}")
    
    matching = g.get_matching()
    print(f"Matching: {matching}")
