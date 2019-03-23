
class Solution:
    def findPeakElement(self, nums: 'List[int]') -> int:
        if len(nums) == 1:
            return 0
        
        peakNum = 0
        peakInd = 0
        for i,v in enumerate(nums):
            if i < len(nums) - 2 and nums[i] < nums[i+1] and nums[i+2] < nums[i+1]:
                return i+1
            
            elif i < len(nums) - 1 and nums[i] < nums[i+1]:
                peakNum = nums[i+1]
                peakInd = i+1
                
        return peakInd
        


sol = Solution()
sol.findPeakElement(nums = [1,2,1])

