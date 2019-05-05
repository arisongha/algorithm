
class Solution:
    def validMountainArray(self, A: 'List[int]') -> bool:
        
        if len(A) < 3:
            return False
        
        up = True
        beforeNum = A[0]
        
        for i,v in enumerate(A[1:]):
            if v == beforeNum:
                return False
            
            if up:
                if v < beforeNum:
                    if i == 0:
                        return False
                    up = False
            else:
                if v > beforeNum:
                    return False
                    
            if len(A[1:])-1 == i and up == True:
                return False
            
            beforeNum = v
            
        return True
            
            

sol = Solution()
sol.validMountainArray([3,5,5])

