
class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'List[int]':
        while len(nums) != 2 :
            for i,v in enumerate(nums):
                if nums.count(v) >= 2:
                    nums.remove(v)
                    nums.remove(v)

        return nums



sol = Solution()
sol.singleNumber([1403617094,-490450406,-1756388866,-967931676,1878401007,1878401007,-74743538,1403617094,-1756388866,-74743538,-490450406,-1895772685])

