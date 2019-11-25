def solution(clothes):
    answer = 0
    dic = dict()
    for clothes in clothes:
        dic[clothes[1]] = dic.get(clothes[1], 0) + 1
        
    mul_count = 1
    sum_count = 0
    
    if len(dic) == 1:
        for key, val in dic.items():
            return val
    
    for key, val in dic.items():
        mul_count *= (val + 1)
        
    return mul_count-1


solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']])

