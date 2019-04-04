
class Solution:
    def findDuplicates(self, nums: 'List[int]') -> 'List[int]':
        dic = dict()
        for i,v in enumerate(nums):
            dic[v] = dic.get(v, 0) + 1
            
        result = []
        for k,v in dic.items():
            if v == 2:
                result.append(k)
                
        return result



sol = Solution()
sol.findDuplicates([4,3,2,7,8,2,3,1])

