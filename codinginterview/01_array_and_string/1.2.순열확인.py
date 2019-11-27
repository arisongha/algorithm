
# coding: utf-8

# In[2]:


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
        


# In[7]:


permutation("aaab", "baaa")

