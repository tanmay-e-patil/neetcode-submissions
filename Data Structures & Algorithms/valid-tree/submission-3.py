class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n:
            return False
        adj = defaultdict(list)
        for s,e in edges:
            adj[s].append(e)
            adj[e].append(s)
        print(adj)
        visit = set()

        def dfs(node, par):
            if node in visit:
                return False
            visit.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        return dfs(0, -1) and len(visit) == n