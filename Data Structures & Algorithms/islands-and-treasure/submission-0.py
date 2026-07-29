import collections
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
        
        rows, cols = len(grid), len(grid[0])
        INF = 2**31 - 1
        queue = collections.deque()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Add all treasure chest locations to queue first (multi-source BFS)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        # BFS from all treasure chests simultaneously
        while queue:
            row, col = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                
                # Check bounds and if cell is land that hasn't been visited
                if (0 <= nr < rows and 0 <= nc < cols and 
                    grid[nr][nc] == INF):
                    
                    # Update distance (current distance + 1)
                    grid[nr][nc] = grid[row][col] + 1
                    queue.append((nr, nc))