
class Solution:
    def reorganizeString(self, S: str) -> str:
        
        dic = dict()
        for i,v in enumerate(S):
            dic[v] = dic.get(v, 0) + 1
        
        largestKey = ""
        largestValue = -1
        
        for key,val in dic.items():
            if val > largestValue:
                largestValue = val
                largestKey = key
        
        dic.pop(largestKey)
        
        sortedStr = sorted(sorted(S), key = S.count)
        
        sumValue = 0
        for key,val in dic.items():
            sumValue += val
            
        if largestValue-1 <= sumValue:
            count = 0
            result = ""
            
            halfNum = len(sortedStr)//2
            half1 = sortedStr[:halfNum]
            half2 = sortedStr[halfNum:]
            
            if len(S)%2 == 0:
                for i in range(len(half1)):
                    result += half1.pop(0)
                    result += half2.pop(0)
            else:
                for i in range(len(half2)):
                    if not len(half2) == 0:
                        result += half2.pop(0)
                    if not len(half1) == 0:
                        result += half1.pop(0)
            return result
        else:
            return ""


sol = Solution()
sol.reorganizeString("ogccckcwmbmxtsbmozlib")

