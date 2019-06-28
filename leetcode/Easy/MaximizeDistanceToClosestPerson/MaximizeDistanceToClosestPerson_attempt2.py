
class Solution:
    def maxDistToClosest(self, seats: 'List[int]') -> int:
        one = []
        maxDistCount = 0
        distCount = 0
        
        for i,v in enumerate(seats):
            
            if v == 0:
                distCount += 1
                
            else:
                one.append(1)
                
                if distCount >= maxDistCount:
                    if len(one) == 2:
                        if distCount % 2 == 0:
                            maxDistCount = distCount // 2 - 1
                        else:
                            maxDistCount = distCount // 2 + 1
                        distCount = 0
                    else:
                        maxDistCount = distCount

                    if i != len(seats)-1 and len(one) == 2:
                        one.pop()
                distCount = 0
            
            if i == len(seats)-1 and v == 0:
                if distCount > maxDistCount:
                    return distCount

        return maxDistCount if maxDistCount > 0 else 1
            


sol = Solution()
sol.maxDistToClosest([1,1,1,0,1,0,1,1,0,0,1])

