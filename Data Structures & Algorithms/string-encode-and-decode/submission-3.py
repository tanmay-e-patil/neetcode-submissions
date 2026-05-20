class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + "#" + s)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        # 4#neet4#code
        res = []
        idx = 0
        while idx < len(s):
            n_idx = idx
            while s[n_idx] != '#':
                n_idx += 1
            length = int(s[idx:n_idx])
            idx = n_idx + 1
            n_idx = idx + length
            res.append(s[idx: n_idx])
            idx = n_idx
        return res
            
