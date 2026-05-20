class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l = 0
        r = m*n - 1
        while l <= r:
            mid = (l + r) // 2
            ro,c = mid // n, mid % n
            print(matrix[ro][c])
            if matrix[ro][c] < target:
                l = mid + 1
            elif matrix[ro][c] > target:
                r = mid - 1
            else:
                return True
        return False




        