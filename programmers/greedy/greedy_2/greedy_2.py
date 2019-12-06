def solution(number, k):
    answer = ''
    count = len(number) - k
    number = [int(n) for n in number]
    return_num = []
    while count:
        max_num = max(number)
        max_num_idx = number.index(max_num)
        if len(number[max_num_idx:]) >= len(number) - count:
            return_num.append(number.pop(max_num_idx))
            number = number[max_num_idx+1:]
            count -= 1
            
    return return_num


solution("1924", 2)

