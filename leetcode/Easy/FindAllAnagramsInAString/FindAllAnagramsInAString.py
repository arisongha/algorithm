
class Solution:
    def findAnagrams(self, s: str, p: str) -> 'List[int]':
        plen = len(p)
        resultList = []
        
        for i,v in enumerate(s):
            sliceWord = s[i:i+plen]
            if sorted(sliceWord) == sorted(p):
                resultList.append(i)
        
        return resultList


sol = Solution()
sol.findAnagrams("abcabcabcacbcba", "abc")

