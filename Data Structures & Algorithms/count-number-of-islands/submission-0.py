class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        num_islands = 0

        def bfs(i, j):
            print(m, n)
            q = deque()
            q.append((i,j))
            visited.add((i,j))
            directions = ((1,0), (0, 1), (-1,0), (0, -1))
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] == "1":
                        visited.add((nr,nc))
                        q.append((nr,nc))


        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == "1":
                    num_islands += 1
                    print(i, j)
                    bfs(i, j)
        return num_islands

       

        