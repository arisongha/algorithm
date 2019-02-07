# Problem Statement

Mr. White is a very versatile person - absolutely everything is interesting to him. Perhaps this is why he has many friends. Quite unfortunately, however, none of his friends are versatile at all. Each of them is interested only in two topics and refuses to talk about anything else. Therefore, each time Mr. White organizes a party, it's a big problem for him to decide whom to invite so that the party is interesting to everybody. Now that Mr. White has a lot of experience in organizing parties, he knows for sure that a party will be interesting if and only if there's a topic interesting to each of the invited friends. 

You will be given s first and second. The i-th friend of Mr. White is interested in topics first[i] and second[i]. Return the largest number of friends that Mr. White can invite to his party so that the party will be interesting.
Definition

Class: InterestingParty
Method: bestInvitation
Parameters: tuple (string), tuple (string)
Returns: integer
Method signature: def bestInvitation(self, first, second):

## Limits

Time limit (s): 840.000
Memory limit (MB): 64

## Constraints
- first will contain between 1 and 50 elements, inclusive.
- second will contain the same number of elements as first.
- Each element of first and second will contain between 1 and 15 characters, inclusive.
- Each character in first and second will be a lowercase letter ('a'-'z').
- For each valid i, first[i] will not be the same as second[i].
## Examples

0)

{"fishing", "gardening", "swimming", "fishing"}
{"hunting", "fishing", "fishing", "biting"}
Returns: 4
This is a very easy case since everybody is interested in "fishing".

1)

{"variety", "diversity", "loquacity", "courtesy"}
{"talking", "speaking", "discussion", "meeting"}
Returns: 1
Despite being interested in "talking", "speaking", "meeting" and so on, these people have nothing to talk about with each other.

2)

{"snakes", "programming", "cobra", "monty"}
{"python", "python", "anaconda", "python"}
Returns: 3
Mr. White can invite friends 0, 1, 3 (0-based) and they will have an interesting evening talking about "python" (or at least Mr. White thinks so).

3)

{"t", "o", "p", "c", "o", "d", "e", "r", "s", "i", "n", "g", "l", "e", "r", "o", "u", "n", "d", "m", "a", "t", "c", "h", "f", "o", "u", "r", "n", "i"}
{"n", "e", "f", "o", "u", "r", "j", "a", "n", "u", "a", "r", "y", "t", "w", "e", "n", "t", "y", "t", "w", "o", "s", "a", "t", "u", "r", "d", "a", "y"}
Returns: 6

This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.
