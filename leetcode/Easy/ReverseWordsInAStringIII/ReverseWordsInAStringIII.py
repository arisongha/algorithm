
class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(word):
            return word[::-1]
        
        return " ".join(map(reverse, s.split(" ")))


sol = Solution()
sol.reverseWords("Let's take LeetCode contest")

