class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        palindrome_list = []
        def isPalindrome(temp_s):
            for i in range(0, len(temp_s)//2):
                if temp_s[i] != temp_s[len(temp_s)-1-i]:
                    return False
            return True
        for i in range(0, len(s)):
            for j in range(i+1, len(s)+1):
                temp_s = s[i:j]
                if isPalindrome(temp_s):
                    palindrome_list.append(temp_s)
        
        palindrome_list = sorted(palindrome_list, key=lambda x:len(x), reverse=True)
        return palindrome_list[0]
