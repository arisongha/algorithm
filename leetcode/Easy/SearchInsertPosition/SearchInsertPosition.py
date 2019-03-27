
class Solution:
    def searchInsert(self, nums: 'List[int]', target: int) -> int:
        
        try:
            if not nums.index(target) == -1:
                return nums.index(target)
        except:
            for i,v in enumerate(nums):
                if target < v:
                    return i
                
            return len(nums)



sol = Solution()
sol.searchInsert([1,3,5,6], 0)

