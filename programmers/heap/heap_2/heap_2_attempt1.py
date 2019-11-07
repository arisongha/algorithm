
def solution(stock, dates, supplies, k):
    answer = 0
    before_d = 0
    for i, (d,s) in enumerate(zip(dates, supplies)):
        if stock - (d-before_d) <= 0:
            stock = stock - (d-before_d) + s
            before_d = d
            answer += 1
            if stock - 1 >= k - d:
                return answer
            
        elif i == len(dates)-1 and stock - (d-before_d) < k:
            stock = stock - (d-before_d) + s
            answer += 1
            if stock - 1 >= k - d:
                return answer


solution(4, [4,10,15], [20,5,10], 30)

