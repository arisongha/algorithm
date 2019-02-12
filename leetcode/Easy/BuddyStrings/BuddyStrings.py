
class Solution:
    def buddyStrings(self, A: 'str', B: 'str') -> 'bool':
        
        dicA = dict()
        dicB = dict()
        
        for ai,av in enumerate(A):
            dicA[av] = dicA.get(av, 0) + 1
        
        for bi,bv in enumerate(B):
            dicB[bv] = dicB.get(bv, 0) + 1
        
        if dicA == dicB:
            if len(dicA) == 1:
                if len(A) != 1:
                    return True
                else:
                    return False
            else:
                if len(A) == 2 and A == B:
                    return False
                else:
                    listB = list(B)
                    
                    for a in range(len(A)):
                        for b in range(a+1,len(A)):
                            
                            listA = list(A)
                            temp = listA[a]
                            listA[a] = listA[b]
                            listA[b] = temp
                            
                            if listA == listB:
                                return True
                    
                    return False
                        
        else:
            return False


sol = Solution()

sol.buddyStrings(A = "bcaaa", B = "baaac")

