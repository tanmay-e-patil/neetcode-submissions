class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        def helper(idx, cur):
           
            res.add(tuple(cur))
            if idx == len(nums):
                return
            c = nums[idx]
            cur.append(c)
            helper(idx + 1, cur.copy())
            cur.pop()
            helper(idx + 1, cur.copy())
        helper(0, [])
        return [list(r) for r in res]
        