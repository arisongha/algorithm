
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        string = ""
        for i,v in enumerate(S):
            if v in T:
                count = T.count(v)
                string += v*count
                T = T.replace(v,"")
            
        return string + T



sol = Solution()
sol.customSortString("kqep" ,"pekeq")

