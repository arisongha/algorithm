
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        while S.find("#") != -1:
            
            index = S.find("#")
            Slist = list(S)
            if index == 0:
                Slist.pop(index)
            else:
                Slist.pop(index-1)
                Slist.pop(index-1)
            str = ""
            for i,v in enumerate(Slist):
                str += v

            S = str
            
        while T.find("#") != -1:
            index = T.find("#")
            Tlist = list(T)
            if index == 0:
                Tlist.pop(index)
            else:
                Tlist.pop(index-1)
                Tlist.pop(index-1)
            str = ""
            for i,v in enumerate(Tlist):
                str += v
                
            T = str
            
        if S == T:
            return True
        else:
            return False


sol = Solution()
sol.backspaceCompare("a##bbc", "bbc")

