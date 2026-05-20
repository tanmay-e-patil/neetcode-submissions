class Solution:
    def isPalindrome(self, s: str) -> bool:
        idx = 0
        end = len(s) - 1
        while idx < end:
            while  idx < end and not s[idx].isalnum() :
                idx += 1
                
            
            while end > idx and not s[end].isalnum() :
                end -= 1
                
            

            
            if s[idx].lower() == s[end].lower():
                idx += 1
                end -= 1
            else:
                return False
        return True


        