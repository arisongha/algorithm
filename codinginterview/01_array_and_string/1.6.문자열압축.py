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

