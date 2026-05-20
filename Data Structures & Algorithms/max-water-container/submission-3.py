class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        res = 0
        r = len(heights) - 1
        max_l = heights[0]
        max_r = heights[-1]
        while l < r:
            # if max_l < heights[l]:
            #     max_l = heights[l]
            max_l = max(max_l, heights[l])
            max_r = max(max_r, heights[r])
            area = min(max_l, max_r) * (r - l)

            if max_l < max_r:
                l += 1
            else:
                r -= 1
            res = max(res, area)
        return res

        