
class Solution:
    def addToArrayForm(self, A: 'List[int]', K: int) -> 'List[int]':
        strA = []
        for i,v in enumerate(A):
            strA.append(str(v))
        
        strNum = "".join(strA)
        
        finalNum = int(strNum) + K
        
        resultList = []
        for i,v in enumerate(str(finalNum)):
            resultList.append(int(v))
            
        return resultList
        
        

sol = Solution()
sol.addToArrayForm(A = [1,2,0,0], K = 34)

