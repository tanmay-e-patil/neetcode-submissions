class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(arr):
            rob1, rob2 = 0, 0
            for n in arr:
                tmp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = tmp
            return rob2
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(helper(nums[0: n - 1]), helper(nums[1:n]))

        