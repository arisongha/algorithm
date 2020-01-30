def solution(priorities, location):
    done = []
    done_num = []
    prior_num = list(range(len(priorities)))
    while location not in done_num:
        temp = priorities.pop(0)
        temp_num = prior_num.pop(0)
        if temp >= max(priorities):
            done.append(temp)
            done_num.append(temp_num)
        else:
            priorities.append(temp)
            prior_num.append(temp_num)
    
    return len(done_num)
