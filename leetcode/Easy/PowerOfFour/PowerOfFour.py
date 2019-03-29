
class Solution:
    def isPowerOfFour(self, num: int) -> bool:

        count = 0
        while True:
            if 4**count == num:
                return True
            
            if 4**count > num:
                return False
            count += 1
            


sol = Solution()
sol.isPowerOfFour(63)

