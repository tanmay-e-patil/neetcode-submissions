class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(n, cur, op, cl):
            if n == op == cl:
                res.append(''.join(cur))
                return
            if op < cl or op > n or cl > n:
                return
            cur.append("(")
            helper(n, cur.copy(), op + 1, cl)
            cur.pop()
            cur.append(")")
            helper(n, cur.copy(), op, cl + 1)
        helper(n, [], 0 , 0)
        return res

        