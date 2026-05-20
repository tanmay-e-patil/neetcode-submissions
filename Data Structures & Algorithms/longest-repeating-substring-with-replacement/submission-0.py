class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}
        max_freq = 0
        l = 0
        for r in range(len(s)):
            char_count[s[r]] = char_count.get(s[r], 0) + 1
            max_freq = max(max_freq, char_count[s[r]])

            if (r - l + 1) - max_freq > k:
                char_count[s[l]] -= 1
                l += 1
        return (r - l + 1)
        