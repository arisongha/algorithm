
class Solution:
    def singleNumber(self, nums: 'List[int]') -> int:
        for i,v in enumerate(nums):
            if nums.count(v) == 1:
                return v
        



sol = Solution()
sol.singleNumber([0,1,0,1,0,1,99])

