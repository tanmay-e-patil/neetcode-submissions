class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = {'(': ')', '{' : '}', '[': ']'}

        for b in s:
            if b == "(" or b == "{" or b == "[":
                stack.append(b)
            elif b == ")" or b == "}" or b == "]":
                if not stack:
                    return False
                if closing[stack[-1]] == b:
                    stack.pop() 
                else:
                    return False
        return not stack       