# Contains Duplicate II

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that **nums[i]** = **nums[j]** and the **absolute** difference between i and j is at most k.

- Example 1:

```
Input: nums = [1,2,3,1], k = 3
Output: true
```

- Example 2:

```
Input: nums = [1,0,1,1], k = 1
Output: true
```

- Example 3:

```
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
```


## My Result

**First Attempt** : Time Limit Exceeded

**Second Attempt** : 

**Runtime** : 64 ms, faster than 15.31% of Python3 online submissions for Contains Duplicate II.

**Memory Usage** : 20.6 MB, less than 23.78% of Python3 online submissions for Contains Duplicate II.

## TODO

- Time complexity O(n^2) 이하로.

- 두번째 시도 : dictionary를 이용해서 for loop를 내에서 value 마다 index를 저장해서, 해당 value가 다시 나왔을때 이전에 dictionary에 저장했던 index와 현재 index의 차를 구해서 k값과 비교한다. 굳이 해당 value의 모든 index 값을 저장하지 않아도 된다는 점을 이용했다. (Discuss 풀이 참고)
