
class Solution:
    def maxSumAfterPartitioning(self, A: 'List[int]', K: int) -> int:
        
        beforeMax = max(A[:K])
        afterMax = max(A[K+1:])
        
        return sum([beforeMax]*K + [A[K]] + [afterMax]*K)



sol = Solution()
sol.maxSumAfterPartitioning(A = [1,15,7,9,2,5,10], K = 3)

