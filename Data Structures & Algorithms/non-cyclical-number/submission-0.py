class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()

        def helper(n):
            if n == 1:
                return True
            res = 0
            while n != 0:
                q,r = divmod(n, 10)
                res += r * r
                n = q
            if res not in s:
                s.add(res)
            else:
                return False
            return helper(res)
        return helper(n)
        