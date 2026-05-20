class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        l = 0
        r = 0
        n = len(nums)
        length = 1
        max_len = 0
        while r < n:
            c = nums[r]
            
            while c + 1 in s:
                length += 1
                c += 1
            max_len = max(length, max_len)
            length = 1
            r += 1
        return max_len

        