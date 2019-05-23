
class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False
        if num == 1:
            return True
        
        prime = [2,3,5]
        go = True
        i = 0
        
        if num in prime:
            return True
        
        while go:
            if i == 3: 
                return False
            if num % prime[i] == 0:
                num = num // prime[i]
                i = 0
                if num in prime:
                    return True
            else:
                i += 1
                


sol = Solution()
sol.isUgly(2)

