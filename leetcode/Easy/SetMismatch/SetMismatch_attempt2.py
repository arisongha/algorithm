
class Solution:
    def findErrorNums(self, nums: 'List[int]') -> 'List[int]':
        
        beforeNum = nums[0]
        result = []
        dic = dict()
        for i,v in enumerate(nums):
            dic[v] = dic.get(v, 0) + 1
            
        for k,v in dic.items():
            if v == 2:
                result.append(k)
                
        result.extend(list(set(list(range(1,len(nums)+1)))-set(nums)))
        
        return result



sol = Solution()
sol.findErrorNums([2,3,2])

