class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1_count = [0] * 26

        for c in s1:
            s1_count[ord(c) - ord('a')] += 1
        

        def check_permutation(s1_count, sub2):

            
            sub2_count = [0] * 26

            for c in sub2:
                sub2_count[ord(c) - ord('a')] += 1
            return s1_count == sub2_count


        i,j = 0, len(s1)

        for i in range(0, len(s2)):
            if check_permutation(s1_count, s2[i:i+j]):
                return True
        return False
        