
class Solution:
    def addToArrayForm(self, A: 'List[int]', K: int) -> 'List[int]':
        ANum = 0
        for i,v in enumerate(A):
            ANum += v * (10**(len(A) - (i + 1)))
            
        finalNum = ANum + K
        
        resultList = []
        for i,v in enumerate(str(finalNum)):
            resultList.append(int(v))
            
        return resultList


sol = Solution()
sol.addToArrayForm(A = [1,2,0,0], K = 34)

