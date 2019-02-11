
class Solution:
    def reverseString(self, s: 'List[str]') -> 'None':
        
        for i in range(len(s)):
            s.insert(i, s.pop())
        
        print(s)


sol = Solution()

sol.reverseString(["h","e","l","l","o"])

