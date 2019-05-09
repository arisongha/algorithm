
class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        dic = dict()
        for i,v in enumerate(s):
            dic[v] = dic.get(v, 0) + 1
        
        length = 0
        oneCount = 0
        odd = 0
        for k,value in dic.items():
            if not value == 1:
                if not value % 2 == 0:
                    length += (value-1)
                    odd += 1
                else:
                    length += value
            else:
                oneCount += 1
        
        if length % 2 == 0 and oneCount >= 1:
            length += 1
        else:
            if odd >= 1:
                length += 1
                
                
        return length



sol = Solution()
sol.longestPalindrome("ababababa")

