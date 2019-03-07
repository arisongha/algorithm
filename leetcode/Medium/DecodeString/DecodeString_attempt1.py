
class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        decodeWord = ""
        count = 0

        for index, letter in enumerate(s):
            if letter.isnumeric():
                stack.append(letter)
                count += 1
            else:
                if letter == "]":
                    count -= 1
                    stack.append(letter)
                    if count == 0:
                        stack.pop()
                        # 여기에서 String으로 다시 변환
                        num = 0
                        numBool = False
                        resultText = ""
                        lettes = ""
                        for i,v in enumerate(stack):
                            if not "[" in stack:
                                if v.isnumeric() and numBool == False:
                                    num = v
                                    numBool = True
                                elif v.isnumeric() and numBool == True:
                                    resultText += int(num) * letters
                                    numBool = False
                                else:
                                    letters += v
                            else:
                                if v.isnumeric() and numBool == False:
                                    num = v
                                    numBool = True
                                elif v.isnumeric() and numBool == True:
                                    restOfStack = ""
                                    for s in stack[i:]:
                                        restOfStack += s
                                    resultText += int(num) * restOfStack
                                    return self.decodeString(resultText)
                                else:
                                    resultText += v
                        
                else:
                    if letter == "[":
                        if count > 1:
                            stack.append(letter)
                    else:
                        stack.append(letter)
                    
                
sol = Solution()
sol.decodeString("3[a2[c6[b]]]")

