class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True


        
       
        idx = n - 2
        jump_needed = 1
        while idx > 0:
            if nums[idx] < jump_needed:
                jump_needed += 1
            else:
                jump_needed = 1
            idx -= 1
            
            
        return jump_needed <= nums[idx]
        