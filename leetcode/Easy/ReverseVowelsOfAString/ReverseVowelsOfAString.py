
class Solution:
    def reverseVowels(self, s: str) -> str:
        slist = list(s)
        vowelList = ["A","E","I","O","U","a","e","i","o","u"]
        
        indexList = []
        letterList = []
        for index,value in enumerate(s):
            if value in vowelList:
                indexList.append(index)
                letterList.append(value)
        
        letterList.reverse()
        for i,v in enumerate(indexList):
            slist[v] = letterList[i]
            
        result = ""
        for letter in slist:
            result += letter
            
        return result


sol = Solution()
sol.reverseVowels("aA")

