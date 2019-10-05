# Partition Equal Subset Sum

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

- Note:

```
Each of the array element will not exceed 100.
The array size will not exceed 200.
``` 

- Example 1:

```
Input: [1, 5, 11, 5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
```

- Example 2:

```
Input: [1, 2, 3, 5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
```

## My Result

**First Attempt**: Time Limit Exceeded

## TODO

- combination 후에 list에서 해당 value를 솎아내는 방법이 비효율적이다. O(mn). 
