# Find Pivot Index

Given an array of integers nums, write a method that returns the "pivot" index of this array.
We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.
If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

- Example 1:

```
Input: 
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation: 
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
```


- Example 2:

```
Input: 
nums = [1, 2, 3]
Output: -1
Explanation: 
There is no index that satisfies the conditions in the problem statement.
```


- Note:

  - The length of `nums` will be in the range `[0, 10000]`.
  - Each element `nums[i]` will be an integer in the range `[-1000, 1000]`.
  
  

## My Result

**First Attempt** : Time Limit Exceeded

**Second Attempt** : 

**Runtime** : 44 ms, faster than 99.54% of Python3 online submissions for Find Pivot Index.

**Memory Usage** : 14.1 MB, less than 55.87% of Python3 online submissions for Find Pivot Index.

## TODO

- for loop 내부에 sum 연산을 두번 사용하므로 시간복잡도는 O(n^2)나 마찬가지이다. 

- 두번째 시도: sum 연산을 for loop 바깥쪽에서 사용하고 for loop 내에서는 해당 index의 숫자를 빼줘서 index의 좌우의 합이 같은지 확인한다. 그러므로 시간복잡도는 O(n)으로 확 줄었다. (Discuss 참고)
