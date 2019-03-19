
class Solution:
    def flipAndInvertImage(self, A: 'List[List[int]]') -> 'List[List[int]]':
        for i,v in enumerate(A):
            v.reverse()
            
            for v_i,v_v in enumerate(v):
                if v[v_i] == 0:
                    v[v_i] = 1
                else:
                    v[v_i] = 0
        
        return A
        

sol = Solution()
sol.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]])

