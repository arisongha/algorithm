# Maximum Average Subarray I

Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

- Example 1:

```
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
``` 

- Note:

  - 1 <= `k` <= `n` <= 30,000.
  - Elements of the given array will be in the range [-10,000, 10,000].
  
  
## My Result

**First Attempt** : Time Limit Exceeded

**Second Attempt** : 

**Runtime** : 208 ms, faster than 26.02% of Python3 online submissions for Maximum Average Subarray I.

**Memory Usage** : 15.5 MB, less than 33.05% of Python3 online submissions for Maximum Average Subarray I.

## TODO

- Time complexity O(nm) 이하로.

- 두번째 시도: sum 연산을 for loop 바깥으로 꺼내는 대신 sumNum = sumNum - nums[i] + nums[i+k] 연산을 넣어주었다. for loop가 k만큼 남았을때까지만 계산하도록 if i+k == len(nums): break 를 넣어주었다.
