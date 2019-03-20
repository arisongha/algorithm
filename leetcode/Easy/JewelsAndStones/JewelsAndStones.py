
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for i,v in enumerate(S):
            if v in set(J):
                count += 1
                
        return count


sol = Solution()
sol.numJewelsInStones(J = "aA", S = "aAAbbbb")

