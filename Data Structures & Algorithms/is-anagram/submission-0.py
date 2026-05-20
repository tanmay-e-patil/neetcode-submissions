class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_count = {}
        
        for i,c in enumerate(s):
            char_count[c] = char_count.get(c, 0) + 1
            char_count[t[i]] = char_count.get(t[i] , 0) - 1
        
        for k, v in char_count.items():
            if v != 0:
                return False
        return True
        
        