# Perfect Number

We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.
Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.

- Example:

```
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
```

- Note: 

  - The input number n will not exceed 100,000,000. (1e8)
  
  
## My Result

**First Attempt** : Time Limit Exceeded

**Second Attempt** :



## TODO

- 두번째 시도: 범위를 지정해주지않은 loop를 돌며 append하고 remove 했던 과정 자체가 중복되는 부분이 많았는데 int(num**0.5)+1 를 정해줌으로써 중복된 과정을 제거할 수 있었다.(Discuss 참고)
