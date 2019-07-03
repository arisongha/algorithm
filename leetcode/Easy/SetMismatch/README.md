# Set Mismatch

The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.
Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

- Example 1:
```
Input: nums = [1,2,2,4]
Output: [2,3]
```

- Note:

  - The given array size will in the range [2, 10000].
  - The given array's numbers won't have any order.
  
  
## My Result

**First Attempt** : Failed

**Second Attempt** : 

**Runtime** : 84 ms, faster than 29.37% of Python3 online submissions for Set Mismatch.

**Memory Usage** : 15.7 MB, less than 5.05% of Python3 online submissions for Set Mismatch.

## TODO

- 두번째 시도: 중복된 숫자를 count-up 하기위해서 굳이 dictionary를 쓰지 않아도 됐을것 같다. dictionary를 쓰지 않는 다른 방법을 찾아봐야겠다.

