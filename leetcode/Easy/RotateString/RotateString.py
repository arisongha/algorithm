
class Solution:
    def rotateString(self, A: 'str', B: 'str') -> 'bool':
        
        if A == '' and B == '':
            return True
        elif A == '' or B == '':
            return False
        
        
        findWordIndex = 0
        for i in range(len(A)):
            
            if A == B[findWordIndex:len(B)] + B[0:findWordIndex]:
                return True
            
            if B[findWordIndex+1:len(B)-1].find(A[0]) != -1:
                findWordIndex = findWordIndex + B[findWordIndex+1:len(B)-1].find(A[0]) + 1
        
        return False


sol = Solution()

sol.rotateString(A = "bqqutquvbtgouklsayfvzewpnrbwfcdmwctusunasdbpbmhnvy", B = "wpnrbwfcdmwctusunasdbpbmhnvybqqutquvbtgouklsayfvze")

