
class Solution:
    def findDisappearedNumbers(self, nums: 'List[int]') -> 'List[int]':
        return list(set(range(1, len(nums)+1)) - set(nums))


sol = Solution()
sol.findDisappearedNumbers([4,3,2,7,8,2,3,1])

