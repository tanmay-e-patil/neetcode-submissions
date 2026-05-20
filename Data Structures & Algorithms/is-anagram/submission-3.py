class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(int)
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            d[s[i]] += 1
            d[t[i]] -= 1
        
        for v in d.values():
            if v != 0:
                return False
        return True
        