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

