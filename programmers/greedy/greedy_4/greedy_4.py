def solution(people, limit):
    answer = 0
    people = sorted(people)
    sum_weight = 0
    while people:
        front_person = people.pop(0)
        sum_weight += front_person
        if sum_weight > limit:
            answer += 1
            sum_weight = 0
            people.insert(0, front_person)
        elif sum_weight == limit:
            answer += 1
            sum_weight = 0
        else:
            if not people:
                answer += 1
        
    return answer


solution([70,80,50,50], 100)

