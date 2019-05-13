
# coding: utf-8

# In[37]:


class Solution:
    def findPairs(self, nums: 'List[int]', k: int) -> int:
        if k < 0:
            return 0
        
        result = []
        for i,v in enumerate(nums):
            for ind,val in enumerate(nums):
                cup = []
                if not i == ind:
                    if v - val == k:
                        cup = sorted([v, val])
                        if not cup in result:
                            result.append(cup)
        
        return len(result)


# In[38]:


sol = Solution()
sol.findPairs([1, 3, 1, 5, 4], k = 0)

