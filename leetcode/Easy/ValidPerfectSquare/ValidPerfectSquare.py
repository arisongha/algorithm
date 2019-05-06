
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        number = 1
        while True:
            if number**2  == num:
                return True
            
            if number**2 < num:
                number +=1
            else:
                return False



sol = Solution()
sol.isPerfectSquare(num=14)

