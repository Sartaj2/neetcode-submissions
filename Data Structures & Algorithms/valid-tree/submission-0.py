from collections import deque
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Tree must have exactly n-1 edges
        if len(edges) != n - 1:
            return False
        
        # Build the adjacency list (hashmap)
        hashmap = {i: [] for i in range(n)}
        for a, b in edges:
            hashmap[a].append(b)
            hashmap[b].append(a)
        
        # BFS setup
        visitset = set()
        queue = deque()
        queue.append((0, -1))  # (node, parent)
        
        while queue:
            node, parent = queue.popleft()
            if node in visitset:
                return False  # Found a cycle
            visitset.add(node)
            for neighbor in hashmap[node]:
                if neighbor == parent:
                    continue  # Don't revisit the node we came from
                queue.append((neighbor, node))
        
        # Check if all nodes are connected
        return len(visitset) == n
