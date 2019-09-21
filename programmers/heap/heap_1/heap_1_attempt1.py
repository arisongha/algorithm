
def solution(scoville, K):
    answer = 0
    while min(scoville) < K and len(scoville) != 1:
        
        min_1 = scoville.pop(scoville.index(min(scoville)))
        min_2 = scoville.pop(scoville.index(min(scoville)))
        
        scoville.append(min_1 + min_2*2)
        answer += 1
        
    if min(scoville) < K:
        answer = -1
        
    return answer


sol = solution([1,1,1,1,2,3], 7)
