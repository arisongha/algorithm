# Problem Statement

A string X is an anagram of string Y if X can be obtained by arranging all characters of Y in some order, without removing any characters and without adding new characters. For example, each of the strings "baba", "abab", "aabb" and "abba" is an anagram of "aabb", and strings "aaab", "aab" and "aabc" are not anagrams of "aabb". 

A set of strings is anagram-free if it contains no pair of strings which are anagrams of each other. Given a set of strings S, return the size of its largest anagram-free subset. Note that the entire set is considered a subset of itself.

## Definition

Class: AnagramFree
Method: getMaximumSubset
Parameters: tuple (string)
Returns: integer
Method signature: def getMaximumSubset(self, S):

## Limits

Time limit (s): 840.000
Memory limit (MB): 64

## Constraints

- S will contain between 1 and 50 elements, inclusive.
- Each element of S will contain between 1 and 50 characters, inclusive.
- Each element of S will consist of lowercase letters ('a'-'z') only.
- All elements of S will be distinct.

## Examples

0)

{"abcd","abdc","dabc","bacd"}
Returns: 1
All of the strings in S are anagrams of each other, so no two of them can simultaneously belong to an anagram-free set.

1)

{"abcd","abac","aabc","bacd"}
Returns: 2
One of the maximum anagram-free subsets of S is {"abcd","abac"}.

2)

{"aa","aaaaa","aaa","a","bbaaaa","aaababaa"}
Returns: 6
Note that strings of different length cannot be anagrams of each other.

3)

{"creation","sentence","reaction","sneak","star","rats","snake"}
Returns: 4

This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.
