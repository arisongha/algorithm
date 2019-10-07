
class Solution:
    def coinChange(self, coins: 'List[int]', amount: int) -> int:
        count = 0
        div = True
        while div:
            max_coin = max(coins)
            divisible = amount // max_coin
            count += divisible
            amount -= max_coin * divisible 
            coins.remove(max_coin)
            
            if amount == 0:
                return count
            
            if len(coins) == 0:
                return -1
            
            

sol = Solution()
sol.coinChange(coins = [186,419,83,408], amount = 6249)


