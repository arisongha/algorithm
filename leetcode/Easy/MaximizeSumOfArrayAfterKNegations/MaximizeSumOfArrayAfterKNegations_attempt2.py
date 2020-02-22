import heapq
class Solution:
    def largestSumAfterKNegations(self, A: 'List[int]', K: int) -> int:
        heapq.heapify(A)
        for i in range(0, K):
            temp = heapq.heappop(A)
            heapq.heappush(A, temp*(-1))
        return sum(A)
