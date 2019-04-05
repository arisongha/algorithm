
class Solution:
    def findMin(self, nums: 'List[int]') -> int:
        minimum = nums[0]
        for i in nums[1:]:
            if i < minimum:
                minimum = i
                
        return minimum



sol = Solution()
sol.findMin([4,5,6,7,0,1,2])

