class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # s = 0
        # n = len(nums)
        # for i in range(n):
        #     s = nums[i]
        #     for j in range(i + 1, n):
        #         s = max(s, s + nums[j])
        #         print(s)
        # return s
        s = 0
        l = 0
        res = nums[0]
        for num in nums:
            if num < 0:
                l += 1
        #     else:
        #         s += num
        #         res = num
        #         break
        if l == len(nums):
            return max(nums)
        for r in range(len(nums)):
            s += nums[r]
            if s < 0:
                s = 0
            res = max(res, s)
            print(res)
        return res
            
            


        