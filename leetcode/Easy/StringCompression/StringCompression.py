
class Solution:
    def compress(self, chars: 'List[str]') -> 'int':
        
        count = 1
        tempCharsSize = len(chars)
        beforeChar = ""
        
        for i in range(tempCharsSize):
            
            if i==0 or chars[i] != beforeChar:
                if count != 1:
                    countString = str(count)
                    
                    for _,v in enumerate(countString):
                        chars.append(v)
                        
                    count = 1
                
                chars.append(chars[i])
                beforeChar = chars[i]
            
            elif i>0 and chars[i] == beforeChar:
                count += 1
            
            if i == tempCharsSize-1:
                countString = str(count)
                
                for _,v in enumerate(countString):
                    if countString != "1":
                        chars.append(v)
                
                count = 1
        
        for i in range(tempCharsSize):
            chars.remove(chars[0])
        
        return len(chars)


sol = Solution()

sol.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])

