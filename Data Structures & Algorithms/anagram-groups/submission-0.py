class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        n = len(strs)
        already_add_set = set()
        for i in range(n):
            tmp = []
            if i in already_add_set:
                continue
            tmp.append(strs[i])

            for j in range(i + 1, n):
                if j in already_add_set:
                    continue
                if sorted(strs[i]) == sorted(strs[j]):
                    tmp.append(strs[j])
                    already_add_set.add(j)
            res.append(tmp)
        return res
            
        