
class Solution:
    def maxArea(self, height: 'List[int]') -> int:
        first, last = 0, len(height) - 1
        maxArea = 0
        while first < last:
            h_first, h_last = height[first], height[last]
            maxArea = max(maxArea, (last-first) * min(h_first, h_last))

            if h_last < h_first:
                last -= 1
            else:
                first += 1
        return maxArea


sol = Solution()
sol.maxArea([1,8,6,2,5,4,8,3,7])

