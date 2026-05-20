class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()
        def helper(idx, cur):
            if sum(cur) == target:
                
                res.add(tuple(cur))
                return
            if idx == len(candidates) or sum(cur) > target:
                return
            
            c = candidates[idx]
            cur.append(c)
            helper(idx + 1, cur.copy())
            cur.pop()
            helper(idx + 1, cur.copy())

        helper(0, [])
        return [list(r) for r in res]

  
        