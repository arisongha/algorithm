
class Solution:
    def fairCandySwap(self, A: 'List[int]', B: 'List[int]') -> 'List[int]':
        num = (sum(B) - sum(A))//2

        for i,v in enumerate(A):
            if v + num in B:
                return [v,v + num]
        
        

sol = Solution()
sol.fairCandySwap(A = [1,2], B = [2,3])

