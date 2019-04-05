
class Solution:
    def singleNonDuplicate(self, nums: 'List[int]') -> int:
        dic = dict()
        for i,v in enumerate(nums):
            dic[v] = dic.get(v, 0) + 1
            
        for k,v in dic.items():
            if v == 1:
                return k



sol = Solution()
sol.singleNonDuplicate([1,1,2,3,3,4,4,8,8])

