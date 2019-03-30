
class Solution:
    def containsDuplicate(self, nums: 'List[int]') -> bool:
        dic = dict()
        for i,v in enumerate(nums):
            dic[v] = dic.get(v, 0) + 1
            
            if dic.get(v) > 1:
                return True
            
        return False
    


sol = Solution()
sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2])

