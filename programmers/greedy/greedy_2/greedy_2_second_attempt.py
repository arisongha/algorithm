
# coding: utf-8

# In[33]:


def solution(number, k):
    answer = ''
    count = len(number) - k
    number = [int(n) for n in number]
    return_num = []
    while count:
        pre_number = number[0:len(number)-count+1]
        max_num = max(pre_number)
        return_num.append(max_num)
        max_num_idx = number.index(max_num)
        number = number[max_num_idx+1:]
        count-=1
    
    return return_num
        
        


# In[34]:


solution("4177252841", 4)

