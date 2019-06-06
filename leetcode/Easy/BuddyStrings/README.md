# Buddy Strings

Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

- Example 1:

> `Input`: A = "ab", B = "ba"
`Output`: true

- Example 2:

> `Input`: A = "ab", B = "ab"
`Output`: false

- Example 3:

> `Input`: A = "aa", B = "aa"
`Output`: true

- Example 4:

> `Input`: A = "aaaaaaabc", B = "aaaaaaacb"
`Output`: true

- Example 5:

> `Input`: A = "", B = "aa"
`Output`: false
 
- Note:

  - 0 <= A.length <= 20000
  - 0 <= B.length <= 20000
  - A and B consist only of lowercase letters.
  
## My Result

**First Attempt** : Time Limit Exceeded

**Second Attempt** :

**Runtime** : 40 ms, faster than 79.42% of Python3 online submissions for Buddy Strings.

**Memory Usage** : 13.4 MB, less than 29.77% of Python3 online submissions for Buddy Strings.


## TODO

- 이중 for loop 외의 다른 방법으로 구현 필요

- 두번째 시도: enumerate 와 zip 의 활용 (다른이의 풀이를 참고)
