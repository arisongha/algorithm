
class Solution:
    def missingNumber(self, nums: 'List[int]') -> int:
        nums = sorted(nums)
        
        beforeNum = nums[0]
        for i,num in enumerate(nums): 
            if i == 0 and num != 0:
                return 0
            elif i != 0:
                if nums[i] - beforeNum == 2:
                    return beforeNum + 1
                else:
                    beforeNum = nums[i]
            
            if i == len(nums) - 1:
                return nums[i] + 1
            

sol = Solution()
sol.missingNumber([0,1,3])

