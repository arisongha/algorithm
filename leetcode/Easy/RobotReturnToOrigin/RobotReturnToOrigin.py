
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dic = dict()
        for i,v in enumerate(moves):
            dic[v] = dic.get(v, 0) + 1
            
        if dic.get("U") == dic.get("D") and dic.get("L") == dic.get("R"):
            return True
        else:
            return False


sol = Solution()
sol.judgeCircle("UD")

