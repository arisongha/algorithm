
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([string.lower() for string in s if string.isalnum()])
        if s == s[::-1]:
            return True
        else:
            return False



sol = Solution()
sol.isPalindrome("A man, a plan, a canal: Panama")

