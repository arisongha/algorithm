
class Solution:
    def findMaxAverage(self, nums: 'List[int]', k: int) -> float:
        
        sumNum = 0
        maxSum = -10000
        for i,v in enumerate(nums):
            if i+k <= len(nums):
                sumNum = sum(nums[i:i+k])
                
            if sumNum > maxSum:
                maxSum = sumNum
                
        return maxSum/k



sol = Solution()
sol.findMaxAverage([-1], k = 1)

