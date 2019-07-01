
class Solution:
    def maxSubArray(self, nums: 'List[int]') -> int:
        
        dp = [nums[0]]*len(nums)
        
        for i in range(1, len(nums)):
            
            if dp[i-1] > 0:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = nums[i]
        
        return max(dp)



sol = Solution()
sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

