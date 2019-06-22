# Valid Mountain Array

Given an array A of integers, return true if and only if it is a valid mountain array.
Recall that A is a mountain array if and only if:

  - `A.length >= 3`
  - There exists some `i` with `0 < i < A.length - 1` such that:
    - `A[0] < A[1] < ... A[i-1] < A[i]`
    - `A[i] > A[i+1] > ... > A[B.length - 1]`
    
    
- Example 1:

```
Input: [2,1]
Output: false
```

- Example 2:

```
Input: [3,5,5]
Output: false
```

- Example 3:

```
Input: [0,3,2,1]
Output: true
``` 

- Note:

  - `0 <= A.length <= 10000`
  - `0 <= A[i] <= 10000`
    
    
## My Result

**First Attempt** : Time Limit Exceeded

**Second Attempt** :

**Runtime** : 80 ms, faster than 15.06% of Python3 online submissions for Valid Mountain Array.

**Memory Usage** : 13.9 MB, less than 76.37% of Python3 online submissions for Valid Mountain Array.

## TODO

- Time complexity

- 두번째 시도: Peak이 하나라는 점에 착안하여 for loop를 짜. 하지만 조건문이 너무 많이 들어간것같다.
