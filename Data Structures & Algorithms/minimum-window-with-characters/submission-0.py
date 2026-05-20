class Solution:

    def minWindow(self, s: str, t: str) -> str:
        #xyaozxyz xyz
        if t == "":
            return t
        
        window = {}
        char_count_T = {}

        for c in t:
            char_count_T[c] = char_count_T.get(c, 0) + 1
        
        l = 0

        need, have = len(char_count_T), 0
        res, resLen = [-1, -1], float('inf')

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if c in char_count_T and window[c] == char_count_T[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = (r - l + 1)
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in char_count_T and window[s[l]] < char_count_T[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        print(l, r, resLen)
        return s[l:r+1] if resLen != float('inf') else ""

        