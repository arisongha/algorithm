
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        result, idx = 0,0

        while (N >=1):
            remainder = N % 2
            N = N // 2
            result += (10**idx) * remainder
            idx +=1
        
        resultStr = ""
        for i,v in enumerate(str(result)):
            if v == "0":
                resultStr += "1"
            else:
                resultStr += "0"
                
        deciNum = 0
        for i,v in enumerate(resultStr):
            deciNum += int(v) * (2**(len(resultStr) - 1 -i))
        return deciNum



sol = Solution()
sol.bitwiseComplement(10)

