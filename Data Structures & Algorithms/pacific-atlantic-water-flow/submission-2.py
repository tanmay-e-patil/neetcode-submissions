class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacific = []
        atlantic = []
        m,n = len(heights), len(heights[0])

        for i in range(m):
            pacific.append((i,0))
            atlantic.append((i, n - 1))
        
        for j in range(n):
            pacific.append((0,j))
            atlantic.append((m -1 , j))

        pac = [[False] * n for i in range(m)]
        atl = [[False] * n for i in range(m)]
        
        def bfs(source, ocean):
            q = deque(source)
            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            while q:
                ro, co = q.popleft()
                ocean[ro][co] = True
                for dr,dc in directions:
                    nr,nc = ro + dr, co + dc
                    if 0 <= nr < m and 0 <= nc < n and heights[nr][nc] >= heights[ro][co] and not ocean[nr][nc]:
                        q.append((nr,nc))
        
        bfs(pacific, pac)
        bfs(atlantic, atl)
        res =[]
        
        for i in range(m):
            for j in range(n):
                if pac[i][j] and atl[i][j]:
                    res.append([i,j])
        return res

                

        # def bfs(r,c,pa):
        #     m,n = len(heights), len(heights[0])
        #     q = deque([(r,c)])
        #     directions = [[1,0], [-1,0], [0,1], [0,-1]]
        #     while q:
        #         for _ in range(len(q)):
        #             ro, co = q.popleft()
        #             if pa:
        #                 if ro == m - 1 or co == n - 1:
        #                     return True
        #             else:
        #                 if ro == 0 or co == 0:
        #                     return True
        #             for dr,dc in directions:
        #                 nr,nc = ro + dr, co + dc
        #                 if 0 <= nr < m and 0 <= nc < n and heights[nr][nc] <= heights[ro][co]:
        #                     q.append((nr,nc))
        #     return False
        
        # m,n = len(heights), len(heights[0])
        # res = []
        # for i in range(m):
        #     for j in range(n):
        #         if bfs(i, j, True) and bfs(i, j, False):
        #             res.append([i,j])
        # return res


                    
            