class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ltrProduct = [1] * len(nums)
        rtlProduct = [1] * len(nums)

        
        for i in range(1,len(nums)):
            ltrProduct[i] = ltrProduct[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            rtlProduct[i] = rtlProduct[i + 1] * nums[i + 1]
        
        
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = ltrProduct[i] * rtlProduct[i]
        return res






        