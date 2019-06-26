# Can Place Flowers

Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.
Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

- Example 1:

```
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
```

- Example 2:

```
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
```

- Note:

  - The input array won't violate no-adjacent-flowers rule.
  - The input array size is in the range of [1, 20000].
  - **n** is a non-negative integer which won't exceed the input array size.
  

## My Result

**First Attempt** : Failed

**Second Attempt** : 

**Runtime**: 48 ms, faster than 97.11% of Python3 online submissions for Can Place Flowers.

**Memory Usage** : 13.3 MB, less than 66.73% of Python3 online submissions for Can Place Flowers.

## TODO 

- 알고리즘 다시.

- 두번째 시도: flowerbed의 시작과 끝이 일반적인 규칙과 달라서 분기점을 만들어 따지기가 애매했는데, 시작과 끝의 index에 0을 넣어줌으로써 모든 index에서 동일한 규칙을 만들었다. 또한 flower를 넣어서 count 하는 것이 아니라 n에서 직접 빼주어서 count 해주는 것이 좋은 아이디어같다. (Discuss 참고)
