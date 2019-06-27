
class Solution:
    def diStringMatch(self, S: str) -> 'List[int]':
        count = 0
        maxD = 0
        for i,v in enumerate(S):
            if v == "D":
                count -= 1
            else:
                count += 1
                
            if count < maxD:
                maxD = count
            
        result = []
        if maxD < 0:
            result.append(-1*maxD)
        else:
            result.append(0)
            
        for i,v in enumerate(S):
            if v == "D":
                result.append(result[-1] - 1)
            else:
                result.append(result[-1] + 1)
                
        return result



sol = Solution()
sol.diStringMatch("DDI")

