
class Solution:
    def findComplement(self, num: int) -> int:

        result, idx = 0,0

        while (num >=1):
            remainder = num % 2
            num = num // 2
            result += (10**idx) * remainder
            idx +=1
            
        strnum = str(result)
        
        resultNum = ""
        for i,v in enumerate(strnum):
            if v == "0":
                resultNum += "1"
            else:
                resultNum += "0"
                
        deciNum = 0
        
        for i,v in enumerate(resultNum):
            deciNum += int(v) * (2**(len(resultNum) - 1 -i))
            
        return deciNum
                


sol = Solution()
sol.findComplement(5)

