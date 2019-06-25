
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        
        
        sminusone = ""
        for i,v in enumerate(s):
            sminusone = s[0:i] + s[i+1:]
            
            if len(sminusone) % 2 == 0 and sminusone[0:len(sminusone)//2] == sminusone[len(sminusone)//2:][::-1]:
                return True
            
            if not len(sminusone) % 2 == 0 and sminusone[0:len(sminusone)//2] == sminusone[len(sminusone)//2:][:0:-1]:
                return True
            
        return False



sol = Solution()
sol.validPalindrome("abcb")

