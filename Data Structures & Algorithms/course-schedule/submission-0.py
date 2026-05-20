class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = defaultdict(list)
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if pre_map[crs] == []:
                return True
            
            visit.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            pre_map[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            
        