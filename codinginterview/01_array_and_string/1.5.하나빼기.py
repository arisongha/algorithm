'''
문자열을 편집하는 방법에는 세 가지 종류가 있다. 문자 삽입, 문자 삭제, 문자 교체. 
문자열 두개가 주어졌을 때, 문자열을 같게 만들기 위한 편집수가 1회 이내인지 확인하는 함수를 작성하라.
'''

def minusOne(string1, string2):
    if len(string1) == len(string2):
        count = 0
        for s1,s2 in zip(string1, string2):
            if s1 != s2:
                count += 1
                if count > 1:
                    return False
        return True
    else:
        big_string = ""
        if len(string1) > len(string2):
            big_string = string1
            small_string = string2
            
        else:
            big_string = string2
            small_string = string1
        
        temp_string = ""
        for i, (s1,s2) in enumerate(zip(string1, string2)):
            if s1 != s2:
                temp_string = big_string[0:i] + big_string[i+1:len(big_string)]
                if temp_string == small_string:
                    return True
                else:
                    return False
                
        return True
                

minusOne("pare", "bale")

