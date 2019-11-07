
class Solution:
    def findKthLargest(self, nums: 'List[int]', k: int) -> int:
        nums = sorted(nums, reverse=True)
        return nums[k-1]


sol = Solution()
sol.findKthLargest([3,2,3,1,2,4,5,5,6], k = 4)

