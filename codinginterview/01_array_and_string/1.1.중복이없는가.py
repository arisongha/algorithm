
# coding: utf-8

# In[2]:


def charDuplicate(string):
    dic = dict()
    for s in string:
        dic[s] = dic.get(s, 0) + 1
        if dic[s] > 1:
            return True
    return False


# In[6]:


charDuplicate("abcdefg")

