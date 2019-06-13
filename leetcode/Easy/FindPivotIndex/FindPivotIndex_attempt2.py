
class Solution:
    def pivotIndex(self, nums: 'List[int]') -> int:
        
        left = 0
        right = sum(nums)
        
        for i,num in enumerate(nums):
            right -= num
            if left == right:
                return i
            left += num
            
        return -1



sol = Solution()
sol.pivotIndex([1, 7, 3, 6, 5, 6])

