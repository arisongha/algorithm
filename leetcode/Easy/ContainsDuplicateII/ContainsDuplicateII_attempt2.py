
class Solution:
    def containsNearbyDuplicate(self, nums: 'List[int]', k: int) -> bool:
        dic = dict()
        
        for i,v in enumerate(nums):
            if v in dic and i - dic.get(v) <= k:
                return True
            
            dic[v] = i
                
        return False                    
                    



sol = Solution()
sol.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2)

