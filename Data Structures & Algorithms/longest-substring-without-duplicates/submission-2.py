class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        char_set = set()
        max_length = 0
        for i, c in enumerate(s):
            print(char_set)
            
            while c in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(c)
            max_length = max(max_length, len(char_set))
        return max_length
        