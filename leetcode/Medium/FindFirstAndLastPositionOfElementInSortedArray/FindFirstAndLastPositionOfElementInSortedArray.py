
class Solution:
    def searchRange(self, nums: 'List[int]', target: int) -> 'List[int]':
        result = []
        for i,v in enumerate(nums):
            if len(result) == 0 and v == target:
                result.append(i)
            
            if len(result) == 1 and not v == target:
                result.append(i-1)
                
            elif len(result) == 1 and i == len(nums)-1:
                result.append(len(nums)-1)
            
                
        if len(result) == 0:
            result.extend([-1,-1])
            
        return result



sol = Solution()
sol.searchRange(nums = [3,3,3], target = 3)

