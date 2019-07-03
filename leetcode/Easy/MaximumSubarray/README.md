# Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

- Example:

```
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```
- Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

## My Result

**First Attemp** : Failed

**Second Attempt** : 

**Runtime** : 32 ms, faster than 99.52% of Python3 online submissions for Maximum Subarray.

**Memory Usage** : 14 MB, less than 11.50% of Python3 online submissions for Maximum Subarray.

## TODO

- 두번째 시도: for loop를 돌면서 현재의 index 이전의 value값이 양수인지 음수인지에 따라 가산할지 말지를 정해나가는 아이디어가 좋은것같다.(Discuss 참고)
