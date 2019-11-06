
# coding: utf-8

# In[7]:


import itertools

def solution(numbers):
    permutations = itertools.permutations(numbers)
    int_list = []
    for permutaion in permutations:
        int_list.append(int(''.join(str(num) for num in permutaion)))
    return str(max(int_list))


# In[8]:


solution([3, 30, 34, 5, 9])


# In[14]:


def solution(numbers):
    numbers = list(map(str, numbers))
    print(numbers)
    numbers.sort(key=lambda x: x*3, reverse=True)
    print(numbers)
    return str(int(''.join(numbers)))


# In[15]:


solution([3, 30, 34, 5, 9])

