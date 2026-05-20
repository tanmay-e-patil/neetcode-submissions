class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        s = set(nums)
        count = 0
        n = len(nums)

        for n in nums:
            if n - 1 not in s:
                count = 1
                while n + count in s:
                    count += 1
                longest = max(longest, count)
            
        # i = 0
        # while i < n:
        #     count = 1
        #     while nums[i] + count in s:
        #         count += 1
    
        #     longest = max(longest, count)
        #     i += 1
        #     if longest > n - i + 1:
        #         break
        return longest
