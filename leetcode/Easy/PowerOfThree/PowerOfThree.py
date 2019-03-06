
import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        return abs(round(math.log(n,3)) - math.log(n,3)) < 0.00000000001


sol = Solution()
sol.isPowerOfThree(19682)

