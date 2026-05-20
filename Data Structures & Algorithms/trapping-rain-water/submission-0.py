class Solution:
    def trap(self, height: List[int]) -> int:
        #Find height where its bigger than prev value
        #that hieght is forst anchor, then in each iteration,
        #that the next height is lower, calculate area,
        # once the next height is equal or higher, that becomes the new anchor
        
        l = 0
        r = len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

