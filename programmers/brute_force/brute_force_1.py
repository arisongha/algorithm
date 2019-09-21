
def solution(answers):
    answer = []
    person_1 = [1, 2, 3, 4, 5]
    person_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    length = len(answers)
    person_1_list = person_1*(length // (len(person_1))) + person_1[:(length - (len(person_1))*(length // (len(person_1))))]
    person_2_list = person_2*(length // (len(person_2))) + person_2[:(length - (len(person_2))*(length // (len(person_2))))]
    person_3_list = person_3*(length // (len(person_3))) + person_3[:(length - (len(person_3))*(length // (len(person_3))))]
    
    person_1_count = 0
    person_2_count = 0
    person_3_count = 0
    
    for i,v in enumerate(answers):
        if v == person_1_list[i]:
            person_1_count += 1
        if v == person_2_list[i]:
            person_2_count += 1
        if v == person_3_list[i]:
            person_3_count += 1
    
    max_num = max((person_1_count, person_2_count, person_3_count))
    if person_1_count == max_num:
        answer.append(1)
    if person_2_count == max_num:
        answer.append(2)
    if person_3_count == max_num:
        answer.append(3)
        
    return answer


solution([1,3,2,4,2])

