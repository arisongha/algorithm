
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        
        strList = list(str(x))
        strRevList = list(str(x))
        strRevList.reverse()
        
        if strList == strRevList:
            return True
        else:
            return False


sol = Solution()
sol.isPalindrome(10)

