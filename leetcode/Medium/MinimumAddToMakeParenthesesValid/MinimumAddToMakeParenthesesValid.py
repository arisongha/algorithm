
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        while "()" in S:
            S = S.replace("()","")
        
        return len(S)



sol = Solution()
sol.minAddToMakeValid("((())")

