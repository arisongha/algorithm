
class Solution:
    def findAnagrams(self, s: str, p: str) -> 'List[int]':
        p_length = len(p)
        sorted_p = sorted(p)
        result = []
        for i,v in enumerate(s):
            if sorted(s[i:i+p_length]) == sorted_p:
                result.append(i)
        
        return result



sol = Solution()
sol.findAnagrams(s= "abab", p= "ab")

