
class Solution:
    def maxArea(self, height: 'List[int]') -> int:
        max_water = 0
        for ind, val in enumerate(height):
            for i, v in enumerate(height):
                if not i is ind:
                    temp = (ind-i) * min(val, v)
                    if temp > max_water:
                        max_water = temp
        return max_water
                

sol = Solution()
sol.maxArea([1,8,6,2,5,4,8,3,7])

