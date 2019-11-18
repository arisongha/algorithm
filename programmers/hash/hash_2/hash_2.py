def solution(phone_book):
    answer = True
    for number in phone_book:
        for n in phone_book:
            if n is not number and n.startswith(number):
                answer = False
                return answer
    return answer


solution(["12","123","1235","567","88"])

