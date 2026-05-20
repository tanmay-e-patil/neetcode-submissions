class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1.0 / x
            n *= -1
        res = 1

        while n != 0:
            if n % 2:
                res *= x
                n -= 1
                continue
            x = x * x
            n = n // 2 
        return res

        