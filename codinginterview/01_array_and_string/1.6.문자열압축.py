'''
반복되는 문자의 개수를 세는 방식의 기본적인 문자열 압축 메서드를 작성하라.
예를 들어 aabccccaaa를 압축하면 a2b1c5a3이 된다. 만약 '압축된' 문자열의 길이가 기존 문자열의 길이보다 길다면
기존 문자열을 반환해야 한다.
문자열은 대소문자 알파벳(a~z)으로만 이루어져 있다.
'''
def stringZip(string):
    temp_string = ""
    before_string = ""
    count = 1
    for i,v in enumerate(string):
        if before_string != v:
            if i != 0:
                temp_string = temp_string + before_string + str(count)
                count = 1
            before_string = v
        else:
            count += 1
            
        if i == len(string)-1:
            temp_string = temp_string + before_string + str(count)
    
    if len(string) < len(temp_string):
        return string
    else:
        return temp_string
            

stringZip("aabbbcccc")

