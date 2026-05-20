class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'{':'}', '[': ']', '(': ')'}
        for c in s:
            if c in '{[(':
                stack.append(d[c])
            elif c in '}])':
                if stack:
                    if stack.pop() != c:
                        return False
                else:
                    return False
        return not stack 
        