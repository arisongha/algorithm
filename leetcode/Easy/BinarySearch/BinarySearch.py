
class Solution:
    def search(self, nums: 'List[int]', target: int) -> int:
        
        start = 0
        end = len(nums)-1
        
        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
            
        return -1



sol = Solution()
sol.search(nums = [-1,0,3,5,9,12], target = 9)

