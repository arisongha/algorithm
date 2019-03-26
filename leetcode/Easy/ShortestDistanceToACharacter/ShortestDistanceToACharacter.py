
class Solution:
    def shortestToChar(self, S: str, C: str) -> 'List[int]':
        Cindex = [i for i,v in enumerate(S) if v == C]
        
        result = []
        for i,v in enumerate(S):
            result.append(min([abs(i-ind) for ind in Cindex]))
            
        return result


sol = Solution()
sol.shortestToChar(S = "loveleetcode", C = 'e')

