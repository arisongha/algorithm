
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: 'List[str]') -> str:
        paragraph = re.sub("[~!@#$%^&*(){}.?';]", "", paragraph.lower())
        paragraph = paragraph.replace(",", " ")
        paragraph = paragraph.replace("  ", " ")
        paralist = paragraph.split(" ")
        
        dic = dict()
        for i,v in enumerate(paralist):
            dic[v] = dic.get(v, 0) + 1
        
        for ban in banned:
            if ban in dic:
                dic.pop(ban)
        
        largestNum = -1
        largestKey = ""
        for k,v in dic.items():
            if v > largestNum:
                largestNum = v
                largestKey = k
        
        return largestKey
        

sol = Solution()
sol.mostCommonWord(paragraph = "a, a, a, a, b,b,b,c, c", banned = ["a"])

