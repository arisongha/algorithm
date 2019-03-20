

class Solution:
    def findErrorNums(self, nums: 'List[int]') -> 'List[int]':

        
        numList = list(range(1, nums[len(nums)-1] + 1))
        dupNum = 0
        for i,v in enumerate(nums):
            if nums.count(v) == 2:
                dupNum = v
                break
                
        nums.pop(nums.index(dupNum))
        
        misNum = set(numList) - set(nums)
        
        return [dupNum, misNum.pop()]



sol = Solution()
sol.findErrorNums(nums = [1,2,2,4])

