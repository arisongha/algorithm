
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        
        for i,v in enumerate(s):
            word = ""
            for index, value in enumerate(s):
                if not index == i:
                    word = word + value
            
            if word == word[::-1]:
                return True
            
        return False



sol = Solution()
sol.validPalindrome("abc")

