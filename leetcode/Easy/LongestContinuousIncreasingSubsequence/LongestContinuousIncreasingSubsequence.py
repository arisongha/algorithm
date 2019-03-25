
class Solution:
    def findLengthOfLCIS(self, nums: 'List[int]') -> int:
        if len(nums) == 0:
            return 0
        
        count = 1
        longestNum = -1
        for i,v in enumerate(nums):
            if i < len(nums) - 1:
                if nums[i+1] <= nums[i]:
                    if count > longestNum:
                        longestNum = count
                    count = 1
                else:
                    count += 1
            elif i == len(nums) - 1:
                if count > longestNum:
                    return count
                else:
                    return longestNum
            
        return longestNum


sol = Solution()
sol.findLengthOfLCIS([1,3,5,4,7])

