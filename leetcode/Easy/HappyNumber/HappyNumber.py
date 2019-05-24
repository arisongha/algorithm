
class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        
        confirm = set()
        
        while n is not 1:
            if n in confirm:
                return False
            
            confirm.add(n)
            
            n = sum([int(num)**2 for num in str(n)])
            
            if n == 1:
                return True



sol = Solution()
sol.isHappy(7)

