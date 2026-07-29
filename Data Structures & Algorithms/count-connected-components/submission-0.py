from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hashmap = {i: [] for i in range(n)}
        for a, b in edges:
            hashmap[a].append(b)
            hashmap[b].append(a)

        visitset = set()
        res = 0

        for node in range(n):
            if node not in visitset:
                res += 1
                queue = deque()
                queue.append(node)  # Start component BFS from this node

                while queue:
                    current = queue.popleft()
                    if current in visitset:
                        continue
                    visitset.add(current)
                    for neighbor in hashmap[current]:
                        if neighbor not in visitset:
                            queue.append(neighbor)
        return res
