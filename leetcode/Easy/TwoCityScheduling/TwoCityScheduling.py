
class Solution:
    def twoCitySchedCost(self, costs: 'List[List[int]]') -> int:
        
        minimumCost = 0
        
        for cost in costs:
            minimumCost += min(cost)
            
        return minimumCost



sol = Solution()
sol.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]])

