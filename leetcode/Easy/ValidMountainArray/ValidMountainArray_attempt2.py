
class Solution:
    def validMountainArray(self, A: 'List[int]') -> bool:
        
        peak = False
        down = False
        
        for i,v in enumerate(A):
            
            if i > 0:
                if A[i] == A[i-1]:
                    return False
            
                if A[i] > A[i-1]:
                    if down:
                        return False
                    if not peak:
                        peak = True
                    if peak and i==len(A)-1:
                        return False

                else:
                    down = True
                    if peak:
                        if A[i] > A[i-1]:
                            return False
                        
        
        return peak
            


sol = Solution()
sol.validMountainArray([3,4,9,14,22,29,32,36,39,41,40,37,32,23,21,10,3])

