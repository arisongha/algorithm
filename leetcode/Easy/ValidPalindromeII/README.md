# Valid Palindrome II

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.


- Example 1:

```
Input: "aba"
Output: True
```

- Example 2:

```
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
```

- Note:

The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

## My Result

**First Attempt** : Time Limit Exceeded

**Second Attempt** : Time Limit Exceeded

## TODO

- 두번째 시도: 이중 for loop를 제거해야겠다는 생각으로 단일 for loop 안에서 string 의 slicing 처리로 단순 비교하려고 했는데, slicing이 O(n)의 시간복잡도를 가지는지 몰랐다. for loop 밖에서 slicing을 하던지해야 할것같다. 

