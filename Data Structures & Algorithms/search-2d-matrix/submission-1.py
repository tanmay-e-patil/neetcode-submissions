class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # m, n = len(matrix), len(matrix[0])
        # l = 0
        # r = m*n - 1
        # while l <= r:
        #     mid = (l + r) // 2
        #     ro,c = mid // n, mid % n
        #     print(matrix[ro][c])
        #     if matrix[ro][c] < target:
        #         l = mid + 1
        #     elif matrix[ro][c] > target:
        #         r = mid - 1
        #     else:
        #         return True
        # return False

        ROWS, COLS = len(matrix), len(matrix[0])

        top, bottom = 0, ROWS - 1
        while top <= bottom:
            row = (top + bottom) //2
            if target > matrix[row][-1]:
                top += 1
            elif target < matrix[row][0]:
                bottom -= 1
            else:
                break
        if not (top <= bottom):
            return False
        row = (top + bottom) // 2
        l = 0
        r = COLS - 1
        while l <= r:
            mid = (l + r)//2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        return False


        


        