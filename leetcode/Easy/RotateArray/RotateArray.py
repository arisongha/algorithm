
class Solution:
    def rotate(self, nums: 'List[int]', k: int) -> None:
        for i in range(k):
            nums.insert(0, nums.pop())


sol = Solution()
sol.rotate([1,2,3,4,5,6,7],k = 3)

