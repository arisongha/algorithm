# Problem Statement

John and Brus are studying string theory at the university. Brus likes palindromes very much. A palindrome is a word that reads the same forward and backward. John would like to surprise Brus by taking a s, and appending 0 or more characters to the end of s to obtain a palindrome. He wants that palindrome to be as short as possible. Return the shortest possible length of a palindrome that John can generate.

## Definition

Class: ThePalindrome
Method: find
Parameters: string
Returns: integer
Method signature: def find(self, s):

## Limits

Time limit (s): 840.000
Memory limit (MB): 64

## Constraints

- s will contain between 1 and 50 characters, inclusive.
- Each character of s will be a lowercase letter ('a' - 'z').

## Examples

0)

"abab"
Returns: 5
"ababa" is the shortest palindrome that John can get.

1)

"abacaba"
Returns: 7
Already a palindrome.

2)

"qwerty"
Returns: 11
All characters are different.

3)

"abdfhdyrbdbsdfghjkllkjhgfds"
Returns: 38

This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.
