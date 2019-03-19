
class Solution:
    def maxProfit(self, prices: 'List[int]') -> int:
        largestMargin = 0
        for i, price in enumerate(prices):
            buy = price
            sell = max(prices[i+1:], default=0)
            if sell - buy > largestMargin:
                largestMargin = sell - buy
                
        return largestMargin



sol = Solution()
sol.maxProfit([7,6,4,3,1])

