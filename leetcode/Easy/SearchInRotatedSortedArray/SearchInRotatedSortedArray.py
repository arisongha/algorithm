
class Solution:
    def search(self, nums: 'List[int]', target: int) -> int:
        for i,v in enumerate(nums):
            if v == target:
                return i
            
        return -1



sol = Solution()
sol.search(nums = [4,5,6,7,0,1,2], target = 0)

