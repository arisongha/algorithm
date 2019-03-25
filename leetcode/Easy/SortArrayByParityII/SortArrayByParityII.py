
class Solution:
    def sortArrayByParityII(self, A: 'List[int]') -> 'List[int]':
        
        evenlist = []
        oddlist = []
        
        result = [0]*len(A)
        for i,v in enumerate(result):
            if not i % 2 == 0:
                result[i] = 1
                
        for i,v in enumerate(A):
            if v % 2 == 0:
                evenlist.append(v)
            else:
                oddlist.append(v)
                
                
        for i,v in enumerate(result):
            if v % 2 == 0:
                result[i] = evenlist.pop()
            else:
                result[i] = oddlist.pop()
                
        return result
        
            
sol = Solution()
sol.sortArrayByParityII([4,2,5,7])

