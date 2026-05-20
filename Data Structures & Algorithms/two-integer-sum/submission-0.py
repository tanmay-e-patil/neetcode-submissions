class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if num in nums_dict:
                return [i, nums_dict[num]] if i < nums_dict[num] else [nums_dict[num], i]
            nums_dict[complement] = i        
        return [-1,-1]