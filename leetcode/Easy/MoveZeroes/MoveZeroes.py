
class Solution:
    def moveZeroes(self, nums: 'List[int]') -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroIndex = []
        notzeroIndex = []
        count = len(nums)
        
        for i,v in enumerate(nums):
            if v == 0:
                zeroIndex.append(v)
            if v != 0:
                notzeroIndex.append(v)
            
        nums.extend(notzeroIndex)
        nums.extend(zeroIndex)
        
        for i in range(count):
            nums.pop(0)


sol = Solution()
sol.moveZeroes([0,0,1])

