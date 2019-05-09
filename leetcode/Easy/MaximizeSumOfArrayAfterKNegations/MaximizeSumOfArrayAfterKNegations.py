
class Solution:
    def largestSumAfterKNegations(self, A: 'List[int]', K: int) -> int:
        
        A = sorted(A)
        minusCount = 0
        zero = False
        for i,v in enumerate(A):
            if v == 0:
                minusCount = i
                zero = True
                break
            if v > 0:
                minusCount = i
                break
        
        if minusCount < K:
        elif minusCount == k:
        
        return minusCount



sol = Solution()
sol.largestSumAfterKNegations(A = [2,-3,-1,5,-4], K = 2)

