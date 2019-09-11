
class Solution:
    def distanceBetweenBusStops(self, distance: 'List[int]', start: int, destination: int) -> int:
        s = 0
        d = 0
        if start > destination:
            s = destination
            d = start
        elif start < destination:
            s = start
            d = destination
        else:
            return 0
        return min(sum(distance[s:d]),sum(distance[d:]) + sum(distance[0:s]))



sol = Solution()
sol.distanceBetweenBusStops(distance = [7,10,1,12,11,14,5,0], start = 7, destination = 2)

