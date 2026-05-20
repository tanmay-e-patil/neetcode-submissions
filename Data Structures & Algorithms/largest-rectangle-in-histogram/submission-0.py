class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = max(heights)
        # i = 0
        # area = 0
        
        
        for i in range(len(heights) - 1):
            area = 0
            l = max_area + 1
            b = 0
            for j in range(i + 1,len(heights)):
                l = min(l, heights[i], heights[j])
                b = j - i + 1
                area = l * b
                max_area = max(max_area, area)
                # print(l, b, area, max_area)
        return max_area 


            

        