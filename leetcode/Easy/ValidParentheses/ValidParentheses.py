
class Solution:
    def isValid(self, s: str) -> bool:
        li = []
        dic = {
            "[":1,
            "{":2,
            "(":3,
            "]":-1,
            "}":-2,
            ")":-3,
        }
        
        for string in s:
            if string in dic.keys() and dic.get(string) > 0:
                li.append(dic.get(string))
            elif string in dic.keys() and dic.get(string) < 0:
                if li == [] or dic[string] != -li.pop():
                    return False
            else:
                return False
            
        return li == []



sol = Solution()
sol.isValid("()")

