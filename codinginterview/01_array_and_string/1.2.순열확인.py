'''
문자열 두 개가 주어졌을 때 이 둘이 서로 순열 관계에 있는지 확인하는 메서드를 작성하라.
'''

def permutation(string1, string2):
    dic1 = dict()
    dic2 = dict()
    for v in string1:
        dic1[v] = dic1.get(v, 0) + 1
        
    for v in string2:
        dic2[v] = dic2.get(v, 0) + 1
        
    if dic1 == dic2:
        return True
    else:
        return False

    
permutation("aaab", "baaa")

