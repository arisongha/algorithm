
def solution(numbers, target):
    answer = 0
    result = [0]
    for _, v in enumerate(numbers):
        temp_list = []
        for ind,val in enumerate(result):
            temp_list.append(val + v)
            temp_list.append(val - v)

        result = temp_list
    
    answer = result.count(target)
    
    return answer


solution([1, 1, 1, 1, 1], 3)

