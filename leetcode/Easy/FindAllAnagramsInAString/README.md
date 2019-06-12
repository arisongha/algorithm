# Find All Anagrams in a String

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.

- Example 1:

```
Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
```

- Example 2:

```
Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
```

## My Result

**First Attempt** : Time Limit Exceeded

**Second Attempt** : Time Limit Exceeded

## TODO

- O(n^2) 외의 다른 방법 

- 두번째 시도 : 절차상의 시간복잡도를 줄였다고 생각했지만 for loop안에서 sorted를 사용했으므로 O(nmlogm)의 시간복잡도가 되었다. Time Limit Exceeded 예제의 시간은 8배 가량 줄었지만 역시 결과는 같았다.
