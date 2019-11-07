class Solution:
    def sortColors(self, nums: 'List[int]') -> None:
        oneCount = nums.count(1)
        twoCount = nums.count(2)
        nums_copy = nums.copy()
        
        for v in nums_copy:
            if v == 1:
                nums.remove(1)
            if v == 2:
                nums.remove(2)
                
        nums.extend([1]*oneCount)
        nums.extend([2]*twoCount)
        
        return nums


sol = Solution()
sol.sortColors([2,0,2,1,1,0])

