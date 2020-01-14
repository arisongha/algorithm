class Solution:
    def balancedStringSplit(self, s: str) -> int:
        rcnt = 0
        lcnt = 0
        result = 0
        for i,v in enumerate(s):
            if v == "R":
                rcnt += 1
            elif v == "L":
                lcnt += 1
            
            if rcnt != 0 and rcnt == lcnt:
                result += 1
                rcnt = 0
                lcnt = 0
                
        return result
