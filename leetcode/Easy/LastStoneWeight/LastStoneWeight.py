
class Solution:
    def lastStoneWeight(self, stones: 'List[int]') -> int:
        
        while len(stones) > 1:
            stones = sorted(stones, reverse=True)
            first = stones.pop(0)
            second = stones.pop(0)
            if first > second:
                stones.append(first - second)
        
        if len(stones) == 1:
            return stones[0]
        else:
            return 0


sol = Solution()
sol.lastStoneWeight([2,7,4,1,8,1])

