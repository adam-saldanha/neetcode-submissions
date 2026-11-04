class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def bfs(r, c) -> int:
            q = deque()
            q.append((r, c))
            count = 1
            grid[r][c] = 0
            while len(q) > 0:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nc < 0 or nr < 0 or nc >= cols or nr >= rows or grid[nr][nc] == 0):
                        continue
                    grid[nr][nc] = 0
                    q.append((nr, nc))
                    count += 1
                    
            return count

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    current = bfs(r, c)
                    if current > maxArea:
                        maxArea = current
        
        return maxArea




        