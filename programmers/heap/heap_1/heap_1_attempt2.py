
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    lenth = len(scoville)
    min_1 = heapq.heappop(scoville)
    for i in range(1,lenth):
        min_2 = heapq.heappop(scoville)
        min_1 = heapq.heappushpop(scoville, min_1 + min_2*2)
        if min_1 >= K:
            return i
        
    return -1


sol = solution([1, 2, 3, 9, 10, 12], 7)

