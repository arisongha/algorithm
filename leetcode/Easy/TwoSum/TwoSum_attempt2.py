

class Solution:
    def twoSum(self, nums: 'List[int]', target: int) -> 'List[int]':
        
        dic = dict()
        
        for i,v in enumerate(nums):
            
            if nums[i] in dic:
                return [dic[nums[i]], i]
            else:
                dic[target - nums[i]] = i



sol = Solution()
sol.twoSum(nums = [2, 7, 11, 15], target = 9)

