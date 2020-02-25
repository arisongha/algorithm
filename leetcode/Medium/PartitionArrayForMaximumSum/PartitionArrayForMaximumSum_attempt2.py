class Solution:
    def maxSumAfterPartitioning(self, A: 'List[int]', K: int) -> int:
        result = list(range(len(A)))
        firstmax = 0
        knum = 0
        secondmax = 0
        for i,v in enumerate(A):
            if i < K:
                if v > firstmax:
                    firstmax = v
            elif i > K:
                if v > secondmax:
                    secondmax = v
            else:
                knum = v
        for i in range(0, len(result)):
            if i < K:
                result[i] = firstmax
            elif i > K:
                result[i] = secondmax
            else:
                result[i] = knum
        
        return sum(result)
