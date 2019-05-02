
class Solution:
    def twoSum(self, nums: 'List[int]', target: int) -> 'List[int]':
        result = []
        for i,v in enumerate(nums):
            for index,value in enumerate(nums):
                if not i == index:
                    if v + value == target:
                        result.append(i)
                        result.append(index)
        
        return list(set(result))



sol = Solution()
sol.twoSum(nums = [3,2,4], target = 6)

