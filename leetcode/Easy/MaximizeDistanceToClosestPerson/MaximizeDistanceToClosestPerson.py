
class Solution:
    def maxDistToClosest(self, seats: 'List[int]') -> int:
        maxDistCount = 0
        distCount = 0
        for i,v in enumerate(seats):
            
            if v == 0:
                print("zero", distCount)
                distCount += 1
            else:
                distCount = 0
                
            if distCount > maxDistCount:
                maxDistCount = distCount
                
        return maxDistCount-1
            
        
        

sol = Solution()
sol.maxDistToClosest([1,0,0,0,1,0,1])

