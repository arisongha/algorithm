
class Solution:
    def isMonotonic(self, A: 'List[int]') -> bool:
        beforeNum = A[0]
        monotype = "none"
        
        for ind, num in enumerate(A):
            if ind > 0:
                if not beforeNum == num:
                    if monotype == "none" and num > beforeNum:
                        monotype = "up"

                    elif monotype == "none" and num < beforeNum:
                        monotype = "down"
                        
                    if monotype == "up":
                        if num < beforeNum:
                            return False
                    elif monotype == "down":
                        if num > beforeNum:
                            return False

                    beforeNum = num
                
        return True
                    
                
sol = Solution()
sol.isMonotonic([1,2,4,5])

