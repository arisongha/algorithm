
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        where = "none"
        
        if len(word) == 1:
            return True
        
        if  word[0].isupper() == True:
            if word[1].isupper() == True:
                where = "all"
            elif word[1].isupper() == False:
                where = "first"
            
            elif word[0].isupper() == False:
                where = "none"
                
        else:
            where = "none"
        
        start = 0
        if where == "none":
            start = 1
        else:
            start = 2
            
        for i in range(start, len(word)):
            if where == "all":
                if word[i].isupper() == False:
                    return False
            
            else:
                if word[i].isupper() == True:
                    return False
        
        return True
            
                

sol = Solution()
sol.detectCapitalUse("mL")

