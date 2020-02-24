class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for li in grid:
            for num in li:
                if num < 0:
                    count +=1
                    
        return count
