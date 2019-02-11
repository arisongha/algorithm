
class Solution(object):
    def reverseWords(self, s):
        
        stripInput = s.strip()
        inputList = stripInput.split(" ")
        inputList.reverse()
        
        output =""
        for i,v in enumerate(inputList):
            if not v == "":
                output += v + " "
        
        stripOuput = output.rstrip()
        
        print(stripOuput)
        return stripOuput


sol = Solution()

sol.reverseWords("   a   b ")

