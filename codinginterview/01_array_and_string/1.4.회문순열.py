'''
주어진 문자열이 회문(palindrome)의 순열인지 아닌지 확인하는 함수를 작성하라. 
회문이란 앞으로 읽으나 뒤로 읽으나 같은 단어 혹은 구절을 의미하며, 순열이란 문자열을 재배치하는 것을 뜻한다. 
회문이 꼭 사전에 등장하는 단어로 제한될 필요는 없다.
'''

def palindrome(string):
    dic = dict()
    for s in string:
        dic[s] = dic.get(s, 0) + 1
    
    odd_count = 0
    for k,v in dic.items():
        if v % 2 != 0:
            odd_count += 1
            if odd_count > 1:
                return False
            
    return True


palindrome("aaaabbbbcddee")

