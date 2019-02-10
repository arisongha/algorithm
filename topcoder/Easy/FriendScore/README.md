# Problem Statement

You want to determine the most popular person in a social network. To do this, you will count the number of "2-friends" that each person has. Person A is called a 2-friend of another person B if they are friends with each other or if there exists some person C who is a friend of both A and B. The most popular person is the person with the highest number of 2-friends. (There might be more than one if multiple people all have the maximal number of 2-friends.)
You are given a friends, where the j-th character of the i-th element is 'Y' if person i and person j are friends, and 'N' otherwise. Return the number of 2-friends of the most popular person in this social network.

## Definition

Class: FriendScore
Method: highestScore
Parameters: tuple (string)
Returns: integer
Method signature: def highestScore(self, friends):

## Limits

Time limit (s): 840.000
Memory limit (MB): 64

## Constraints

- friends will contain between 1 and 50 elements, inclusive. 
- Each element of friends will contain exactly N characters 'Y' or 'N', where N is the number of elements in friends. 
- For each i and j, friends[i][j] will be equal to friends[j][i]. 
- For each i, friends[i][i] will be equal to 'N'. 

## Examples

0)

{"NNN", "NNN", "NNN"}
Returns: 0
Here, there are 3 people and none of them are friends, so everybody has zero 2-friends.

1)

{"NYY", "YNY", "YYN"}
Returns: 2
Each person has two 2-friends.

2)

{"NYNNN", "YNYNN", "NYNYN", "NNYNY", "NNNYN"}
Returns: 4
Persons 0 and 4 have two 2-friends, persons 1 and 3 have three 2-friends. Person 2 is the most popular one - four 2-friends.

3)

{"NNNNYNNNNN", "NNNNYNYYNN", "NNNYYYNNNN", "NNYNNNNNNN", "YYYNNNNNNY", "NNYNNNNNYN", "NYNNNNNYNN", "NYNNNNYNNN", "NNNNNYNNNN", "NNNNYNNNNN"}
Returns: 8

4)

{"NNNNNNNNNNNNNNY", "NNNNNNNNNNNNNNN", "NNNNNNNYNNNNNNN", "NNNNNNNYNNNNNNY", "NNNNNNNNNNNNNNY", "NNNNNNNNYNNNNNN", "NNNNNNNNNNNNNNN", "NNYYNNNNNNNNNNN", "NNNNNYNNNNNYNNN", "NNNNNNNNNNNNNNY", "NNNNNNNNNNNNNNN", "NNNNNNNNYNNNNNN", "NNNNNNNNNNNNNNN", "NNNNNNNNNNNNNNN", "YNNYYNNNNYNNNNN"}
Returns: 6

This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.
