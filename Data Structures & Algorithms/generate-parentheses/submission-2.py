class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []
        def helper(op, cl):
            if n == op == cl:
                res.append(''.join(cur))
                return
            if op < n:
                cur.append("(")
                helper(op + 1, cl)
                cur.pop()
            if cl < op:
                cur.append(")")
                helper(op, cl + 1)
                cur.pop()
        helper(0 , 0)
        return res

        