## Problem Statement


- You are converting old code for a new compiler version. Each "->" string should be replaced by ".", but this replacement shouldn't be done inside comments. A comment is a string that starts with "//" and terminates at the end of the line. You will be given a program containing the old code. Return a containing the converted version of the code.

- Definition

Class:
AccessChanger
 
Method: 
convert
 
Parameters:
tuple (string)
 

Returns:
tuple (string)
 

Method signature:
def convert(self, program):
  
- Limits

Time limit (s):
840.000
 
Memory limit (MB): 
64
   
 
- Constraints
 - program will have between 1 and 50 elements, inclusive. 
 - Each element of program will contain between 1 and 50 characters, inclusive. 
 - Each character in program will have ASCII value between 32 and 127, inclusive.
  
 
- Examples
 
 0)  
{"Test* t = new Test();","t->a = 1;","t->b = 2;","t->go(); // a=1, b=2 --> a=2, b=3"}
Returns: {"Test* t = new Test();", "t.a = 1;", "t.b = 2;", "t.go(); // a=1, b=2 --> a=2, b=3" }
  
 1) 
{"---> // the arrow --->","---","> // the parted arrow"}
Returns: {"--. // the arrow --->", "---", "> // the parted arrow" }
  
 2) 
{"->-> // two successive arrows ->->"}
Returns: {".. // two successive arrows ->->" }
    
--------------------------------------------------------------------------------
This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved. 
 
 
