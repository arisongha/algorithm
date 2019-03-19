
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> 'List[str]':
        AList = A.split(" ")
        BList = B.split(" ")
        
        dicA = dict()
        dicB = dict()
        
        for i,v in enumerate(AList):
            dicA[v] = dicA.get(v, 0) + 1
            
        for i,v in enumerate(BList):
            dicB[v] = dicB.get(v, 0) + 1
            
        result = []
        
        for k,v in dicA.items():
            if v < 2 and dicB.get(k) == None:
                result.append(k)
                
        for k,v in dicB.items():
            if v < 2 and dicA.get(k) == None:
                result.append(k)
                
        return result


sol = Solution()
sol.uncommonFromSentences(A = "apple apple", B = "banana")

