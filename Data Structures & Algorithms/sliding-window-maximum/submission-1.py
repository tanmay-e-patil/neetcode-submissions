class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 9,6,5,4, 3,2,1
        res = []
        
        l = 0
        for r in range(k, len(nums) + 1):
            # print(nums[l:r])
            res.append(max(nums[l:r]))
            l += 1
        return res
        