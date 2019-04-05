
class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> int:
        dic = dict()
        for i,v in enumerate(nums):
            dic[v] = dic.get(v, 0) + 1
        
        result = []
        for k,v in dic.items():
            if v >= 2:
                dic[k] = 2
            
            for i in range(dic[k]):
                result.append(k)
                
        return result
        


sol = Solution()
sol.removeDuplicates(nums = [1,1,1,2,2,3])

