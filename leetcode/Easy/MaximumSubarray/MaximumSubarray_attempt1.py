
class Solution:
    def __init__(self):
        self.dic = dict()
        self.max = 0
    
    def maxSubArray(self, nums: 'List[int]') -> int:
        
        for i in range(1, len(nums) + 1):
            if nums[i] + self.dic[i-1] > 0:
                self.dic[i] = self.dic[i-1]
            else:
                self.dic[i] = 0
                
            self.max = max(self.max, self.dic[i])
        
        return max


sol = Solution()
sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

