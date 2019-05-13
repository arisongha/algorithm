
class Solution:
    def containsNearbyDuplicate(self, nums: 'List[int]', k: int) -> bool:
        for i,v in enumerate(nums):
            for ind, val in enumerate(nums):
                if not i == ind and 0<i-ind<=k and v == val:
                    return True
                
        return False                    
                    


sol = Solution()
sol.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2)

