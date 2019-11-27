'''
문자열이 주어졌을 때, 이 문자열에 같은 문자가 중복되어 등장하는지 확인하는 알고리즘을 작성하라. 
자료구조를 추가로 사용하지 않고 풀 수 있는 알고리즘 또한 고민하라.
'''

def charDuplicate(string):
    dic = dict()
    for s in string:
        dic[s] = dic.get(s, 0) + 1
        if dic[s] > 1:
            return True
    return False


charDuplicate("abcdefg")

