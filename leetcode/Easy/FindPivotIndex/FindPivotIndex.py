
class Solution:
    def pivotIndex(self, nums: 'List[int]') -> int:
        
        for i,v in enumerate(nums):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
            
        return -1




sol = Solution()
sol.pivotIndex(nums = [1, 7, 3, 6])

