
class Solution:
    def __init__(self):
        self.dic = dict()
    
    def canJump(self, nums: 'List[int]') -> bool:
        if len(nums) == 1:
            return True
        
        self.dic[0] = nums[0]
        for i in range(1, len(nums)):
            if self.dic[i-1] < i:
                return False
            
            self.dic[i] = max(self.dic[i-1], i + nums[i])
            
        return self.dic[len(nums)-1] >= len(nums) - 1
            

sol =  Solution()
sol.canJump([2,3,1,1,4])

