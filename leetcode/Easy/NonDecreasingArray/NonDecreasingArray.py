
class Solution:
    def checkPossibility(self, nums: 'List[int]') -> bool:
        
        if not nums == list(reversed(sorted(nums))):
            return True
        else:
            return False
        
    

sol = Solution()
sol.checkPossibility([4,2,1])

