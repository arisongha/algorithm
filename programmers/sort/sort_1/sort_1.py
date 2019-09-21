
def solution(array, commands):
    answer = []
    for i,v in enumerate(commands):
        answer.append(sorted(array[v[0]-1:v[1]])[v[2]-1])
    return answer


solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])

