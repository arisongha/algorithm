
class Solution:
    def dominantIndex(self, nums: 'List[int]') -> int:
        maxNum = max(nums)
        maxInd = nums.index(maxNum)
        for i,v in enumerate(nums):
            if not i == maxInd and v*2 > maxNum:
                return -1
            
        return maxInd



sol = Solution()
sol.dominantIndex(nums = [1,2,3,4])

