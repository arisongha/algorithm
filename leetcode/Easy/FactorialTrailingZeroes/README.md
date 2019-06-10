# Factorial Trailing Zeroes

Given an integer n, return the number of trailing zeroes in n!.

- Example 1:

```
Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
```

- Example 2:

```
Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
```

- Note: Your solution should be in logarithmic time complexity.

## My Result

**First Attempt** : Time Limit Exceeded

**Second Attempt** : Time Limit Exceeded

## TODO 

- 두번째 시도: countZero = str(resultInt).count("0") 코드를 넣어서 두번째 for loop 최대 trail 0의 개수의 제한을 걸어주었지만 결과는 같았다.
