
class Solution:
    def __init__(self):
        self.dic = dict()
        
    def rob(self, nums: 'List[int]') -> int:
        if len(nums) == 0:
            return 0
        
        elif len(nums) == 1:
            return nums[0]
        
        elif len(nums) == 2:
            return max(nums)
        
        elif self.dic.get(len(nums)) != None:
            return self.dic.get(len(nums))
        
        else:
            self.dic[len(nums)] = max(self.rob(nums[:len(nums)-2]) + nums[len(nums)-1], self.rob(nums[:len(nums)-1]))
            return self.dic[len(nums)]
        

sol = Solution()
sol.rob([1,1,6,8,4,0,0,10])

