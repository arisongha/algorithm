
def solution(progresses, speeds):
    answer = []
    day_list = []
    for progress, speed in zip(progresses, speeds):
        left_process = 100 - progress
        days_left = 0
        if left_process % speed == 0:
            days_left = left_process // speed
        else:
            days_left = left_process // speed + 1
        day_list.append(days_left)
        
    temp_list = []
    before_pro = 0
    for i,v in enumerate(day_list):
        if i == 0:
            temp_list.append(v)
            before_pro = v
        else:
            if before_pro < v:
                answer.append(len(temp_list))
                temp_list = []
                before_pro = v
            temp_list.append(v)
        if i == len(day_list)-1:
            answer.append(len(temp_list))

    return answer


solution([20,97,3,70,30,55,40],[40,2,12,18,30,5,3])

