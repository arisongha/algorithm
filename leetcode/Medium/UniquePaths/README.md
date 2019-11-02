## Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

![robot_maze](https://user-images.githubusercontent.com/44221590/68070205-c69fa980-fdae-11e9-996c-ff736d7c49e6.png)
Above is a 7 x 3 grid. How many possible unique paths are there?

- Note: 
m and n will be at most 100.

- Example 1:

```
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
```

- Example 2:

```
Input: m = 7, n = 3
Output: 28
```

## My Result

**First Attempt**: Time Limit Exceeded

## TODO

- itertools.Permutations의 시간복잡도. 너무 오래걸림.
