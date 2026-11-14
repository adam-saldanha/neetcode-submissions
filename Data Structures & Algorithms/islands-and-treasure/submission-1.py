class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        rows = len(grid)
        cols = len(grid[0])
        q = deque()

        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                grid[r][c] = dist
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nc < 0 or nr == rows or nc == cols or (nr, nc) in visited or grid[nr][nc] == -1):
                        continue
                    visited.add((nr, nc))
                    q.append((nr, nc))


            dist += 1

