
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count = 0
        while True:
            if 2**count == n:
                return True
            
            if 2**count > n:
                return False
            count += 1
            


sol = Solution()
sol.isPowerOfTwo(34)

