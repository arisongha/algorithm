
class Solution:
    def trailingZeroes(self, n: int) -> int:
        resultInt = 1
        count = ""
        for i in range(1,n+1):
            resultInt = resultInt * i
        
        countZero = str(resultInt).count("0")
        
        count = 0
        for i,v in enumerate(str(resultInt)[countZero:]):
            if v == "0":
                count += 1
            else:
                count = 0
                
        return count



sol = Solution()
sol.trailingZeroes(7737)

