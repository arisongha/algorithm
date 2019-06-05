
class Solution:
    def maxProfit(self, prices: 'List[int]') -> int:
        
        maxPro, minPri = 0, 3.4*(10**38)
        
        for price in prices:
            minPri = min(price, minPri)
            pro = price - minPri
            maxPro = max(pro, maxPro)
            
        return maxPro



sol = Solution()
sol.maxProfit([7,1,5,3,6,4])

