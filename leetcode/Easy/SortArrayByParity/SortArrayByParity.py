
class Solution:
    def sortArrayByParity(self, A: 'List[int]') -> 'List[int]':
        
        evenlist = []
        oddlist = []
        
        for i,v in enumerate(A):
            if v % 2 == 0:
                evenlist.append(v)
            else:
                oddlist.append(v)
        
        result = evenlist + oddlist
        
        return result
        
            

sol = Solution()
sol.sortArrayByParity([3,1,2,4])

