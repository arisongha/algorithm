
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letters = [v for i,v in enumerate(S) if v.isalpha()]
        letters.reverse()
        letterlist = list(S)
        
        result = ""
        for i,v in enumerate(letterlist):
            if v.isalpha():
                letterlist[i] = letters.pop(0)
                
            result += letterlist[i]
        
        return result


sol = Solution()
sol.reverseOnlyLetters("a-bC-dEf-ghIj")

