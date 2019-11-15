class Solution:
    
    def __init__(self):
        self.ans = []
    
    def generateParenthesis(self, n: int) -> 'List[str]':
        self.helper(n, n, '')
        return self.ans
        
    def helper(self, openp, closep, s):
        if openp < 0 or closep < 0:
            return s
        
        if openp > 0:
            self.helper(openp - 1, closep, s + '(')
        
        if closep > openp:
            self.helper(openp, closep - 1, s + ')')
        
        if closep == 0:
            self.ans.append(s)


sol = Solution()
sol.generateParenthesis(3)

