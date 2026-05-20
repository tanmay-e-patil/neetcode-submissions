class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for v1,v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        print(adj)
        visited = set()
        res = 0

        def dfs(node, par):
            nonlocal res

            if node in visited:
                return
            visited.add(node)

            found_par = False
            for nei in adj[node]:
                if nei == par:
                    found_par = True
                    continue
                dfs(nei, node)

            print(node, par, found_par)
            if not found_par:
                res += 1
        
        for i in range(n):
            print(visited)
            if i not in visited:
                dfs(i, -1)
        return res
        