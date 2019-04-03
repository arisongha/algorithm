
class Solution:
    def findMaxConsecutiveOnes(self, nums: 'List[int]') -> int:
        count = 0
        largestNum = 0
        for i,v in enumerate(nums):
            if v == 1:
                count += 1
                if count > largestNum:
                    largestNum = count
            else:
                count = 0
        
        return largestNum



sol = Solution()
sol.findMaxConsecutiveOnes([1,1,0,1,1,1])

