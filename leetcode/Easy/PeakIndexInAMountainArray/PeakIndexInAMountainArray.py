
class Solution:
    def peakIndexInMountainArray(self, A: 'List[int]') -> int:
        return A.index(max(A))


sol = Solution()
sol.peakIndexInMountainArray([0,2,1,0])

