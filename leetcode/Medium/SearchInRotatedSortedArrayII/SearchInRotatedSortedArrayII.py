
class Solution:
    def search(self, nums: 'List[int]', target: int) -> bool:
        for i,v in enumerate(nums):
            if v == target:
                return True
            
        return False



sol = Solution()
sol.search(nums = [2,5,6,0,0,1,2], target = 0)

