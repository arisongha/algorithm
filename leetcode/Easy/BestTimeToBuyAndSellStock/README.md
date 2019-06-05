Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.

- Example 1:

```
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
```

- Example 2:

```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

## My Result

**First Attempt** : Time Limit Exceeded

**Second Attempt** :

**Runtime** : 40 ms, faster than 93.50% of Python3 online submissions for Best Time to Buy and Sell Stock.

**Memory Usage** : 14.2 MB, less than 5.40% of Python3 online submissions for Best Time to Buy and Sell Stock.

## TODO

O(n^2) 외의 다른 방법 

- 두번째 시도: for loop 내의 max(price[i+1:]를 제거하고 Min Price 변수를 넣어 for loop를 돌때마다 제거한 코드의 역할을 수행하게끔 하였다. 
