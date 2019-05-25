
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        divisor = set()
        count = 1
        while True:
            if num % count == 0:
                divisor.add(count)
                divisor.add(num // count)
            count += 1
            
            if count > num//2:
                divisor.remove(num)
                if sum(divisor) == num:
                    return True
                else:
                    return False



sol = Solution()
sol.checkPerfectNumber(20996011)

