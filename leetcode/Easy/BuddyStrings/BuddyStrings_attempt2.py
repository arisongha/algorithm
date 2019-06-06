
class Solution:
    def buddyStrings(self, A, B):
        if len(A) != len(B):
            return False

        notSame = []
        for i, (a,b) in enumerate(zip(A,B)):
            if a is not b:
                notSame.append(i)
                

        if len(notSame) == 0:
            return len(set(B)) != len(B)
        
        if len(notSame) != 2:
            return False

        return A[notSame[0]] == B[notSame[1]] and A[notSame[1]] == B[notSame[0]]



sol = Solution()
sol.buddyStrings(A = "bcaaa", B = "baaac")

