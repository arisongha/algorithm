
def solution(heights):
    answer = []
    
    for i,v in enumerate(reversed(heights)):
        for ind, val in enumerate(reversed(heights[0:len(heights)-i-1])):
            if val > v:
                answer.append(len(heights)-i-1-ind)
                break
        if len(answer) is not i+1:
            answer.append(0)
    
    return list(reversed(answer))


solution([3,9,9,3,5,7,2])

