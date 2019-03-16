
class Solution:
    def __init__(self):
        self.dic = dict()
        
    def fib(self, N: int) -> int:
        
        if N == 0:
            return 0
        
        elif N == 1:
            return 1
        
        elif self.dic.get(N) != None:
            return self.dic[N]
        
        else:
            self.dic[N] = self.fib(N-1) + self.fib(N-2)
            return self.dic[N]
        

sol = Solution()
sol.fib(3)

