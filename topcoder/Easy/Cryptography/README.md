# Problem Statement
TopCoder Security Agency (TSA, established today) has just invented a new encryption system! This encryption system takes as its input a list of numbers to encrypt. 

You work at TSA and your task is to implement a very important part of the encryption process. You are allowed to pick one number in the input list and increment its value by 1. This should be done in such way that the product of all numbers in the list after this change becomes as large as possible. 

Given the list of numbers as numbers, return the maximum product you can obtain. It is guaranteed that the return value will not exceed 2^62.

## Definition

Class: Cryptography
Method: encrypt
Parameters: tuple (integer)
Returns: long integer
Method signature: def encrypt(self, numbers):

## Limits

Time limit (s): 840.000
Memory limit (MB): 64

## Constraints
- numbers will contain between 2 and 50 elements, inclusive.
- Each element of numbers will be between 1 and 1000, inclusive.
- The return value will not exceed 2^62.

## Examples

0)

{1,2,3}
Returns: 12
If we increment the first number, we get 2*2*3 = 12. If we increment the second, we get 1*3*3 = 9. If we increment the third, we get 1*2*4 = 8. Hence, the correct return value is 12.

1)

{1,3,2,1,1,3}
Returns: 36
The elements of numbers are not necessarily unique.

2)

{1000,999,998,997,996,995}
Returns: 986074810223904000
The answer may be very big, but will not exceed 2^62.

3)

{1,1,1,1}
Returns: 2

This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.
