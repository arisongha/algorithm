
class Solution:
    def findMaxAverage(self, nums: 'List[int]', k: int) -> float:
        
        maxSum = -float("inf")
        sumNum = sum(nums[0:k])
        
        for i,v in enumerate(nums):
            if sumNum > maxSum:
                maxSum = sumNum
                
            if i+k < len(nums):
                sumNum = sumNum - nums[i] + nums[i+k]
                
        return maxSum/k



sol = Solution()
sol.findMaxAverage([0,1,1,3,3], 4)

