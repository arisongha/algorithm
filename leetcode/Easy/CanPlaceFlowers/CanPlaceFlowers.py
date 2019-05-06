
class Solution:
    def canPlaceFlowers(self, flowerbed: 'List[int]', n: int) -> bool:
        zeroCount = 0
        maxNum = 0
        for i,v in enumerate(flowerbed):
            if v == 0:
                zeroCount += 1
            else:
                zeroCount = 0
                
            if zeroCount > maxNum:
                maxNum = zeroCount
        
        if not maxNum % 2 == 0:
            return maxNum-2 >= n
        else:
            return maxNum-3 >= n



sol = Solution()
sol.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1)

