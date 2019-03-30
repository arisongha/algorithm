
class Solution:
    def singleNumber(self, nums: 'List[int]') -> int:
        
        dic = dict()
        for i,v in enumerate(nums):
            dic[v] = dic.get(v, 0) + 1
            
        for k,v in dic.items():
            if dic.get(k) == 1:
                return k
            


sol = Solution()
sol.singleNumber([4,1,2,1,2])

