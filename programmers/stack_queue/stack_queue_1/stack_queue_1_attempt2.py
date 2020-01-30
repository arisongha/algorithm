def solution(progresses, speeds):
    answer = []
    while sum(answer) != len(progresses):
        for i,v in enumerate(progresses):
            if v < 100:
                progresses[i] = v + speeds[i]
            if v > 100:
                progresses[i] = 100
        
        complete_cnt = 0
        for i in range(0, len(progresses)):
            if progresses[i] == 100:
                complete_cnt += 1
            else:
                break
        if len(answer) == 0:
            if complete_cnt != 0:
                answer.append(complete_cnt)
        else:
            if complete_cnt != 0 and sum(answer) != complete_cnt:
                answer.append(complete_cnt-sum(answer))
        
    return answer
