
class Solution:
    def reverse(self, x: int) -> int:
        minus = False
        if x < 0:
            minus = True
            x = x * -1
        
        string = str(x)
        reverse = ""
        for i,v in enumerate(string):
            reverse = v + reverse
        
        result = ""
        for i,v in enumerate(reverse):
            if result == "" and v == "0":
                pass
            else:
                result += v
                
        result = int(result)
        
        if minus == True:
            result = result * -1
            
        if not -2**31 < result < 2**31 -1:
            result = 0
            
        return result



sol = Solution()
sol.reverse(1534236469)

