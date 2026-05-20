class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.INF = 2**31 -1

        def bfs(r,c):
            q = deque([(r,c)])
            visited = set()
            visited.add((r,c))
            directions = [[-1,0], [1,0], [0,-1], [0,1]]
            steps = 0
            while q:
                for _ in range(len(q)):
                    ro,co = q.popleft()
                    if grid[ro][co] == 0:
                        return steps
                    for dr, dc in directions:
                        nr, nc = ro + dr, co + dc
                        if (0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visited and grid[nr][nc] != -1):
                            visited.add((nr,nc))
                            q.append((nr,nc))
                steps += 1
            return self.INF
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == self.INF:
                    grid[i][j] = bfs(i,j)



        # self.INF = 2**31 - 1
        # visited = set()
        
        # def dfs(r,c,steps):
        #     if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or (r,c) in visited or grid[r][c] == -1:
        #         return self.INF
        #     if grid[r][c] == 0:
        #         return steps
        #     if grid[r][c] != self.INF:
        #         return steps + grid[r][c]
            
        #     visited.add((r,c))
            
        #     a = dfs(r + 1, c, steps + 1)
        #     b = dfs(r - 1, c, steps + 1)
        #     d = dfs(r, c + 1, steps + 1)
        #     e = dfs(r, c - 1, steps + 1)
            
        #     visited.remove((r,c))
        #     return min(a,b,d,e)
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == self.INF:
        #             grid[i][j] = dfs(i, j, 0)
        

        