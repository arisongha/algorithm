
class Solution:
    def __init__(self):
        self.dic = dict()
    
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if self.dic.get(n) != None:
            return self.dic.get(n)
        else:
            self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.dic[n] 


sol = Solution()
sol.climbStairs(10)

