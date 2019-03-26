
class Solution:
    def sortedSquares(self, A: 'List[int]') -> 'List[int]':
        result = []
        for i,v in enumerate(A):
            result.append(v*v)
            
        result.sort()
        
        return result
        


sol = Solution()
sol.sortedSquares([-4,-1,0,3,10])

