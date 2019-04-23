
class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count("A") > 1:
            return False
        
        countL = 0
        for r in s:
            if r == "L":
                countL += 1
            else:
                countL = 0
                
            if countL == 3:
                return False
            
        return True



sol = Solution()
sol.checkRecord("PPALLP")

