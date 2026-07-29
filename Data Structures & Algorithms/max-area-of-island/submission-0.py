import collections

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        maxIslands = 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visit.add((r, c))
            res = 1  # Area of this island

            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] == 1 and
                        (nr, nc) not in visit):
                        q.append((nr, nc))
                        visit.add((nr, nc))
                        res += 1
            return res

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    maxIslands = max(maxIslands, bfs(r, c))
        return maxIslands
