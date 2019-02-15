
class Solution:
    def isAnagram(self, s: 'str', t: 'str') -> 'bool':
        
        dicS = dict()
        dicT = dict()
        
        for i,v in enumerate(s):
            dicS[v] = dicS.get(v, 0) + 1
            
        for i,v in enumerate(t):
            dicT[v] = dicT.get(v, 0) + 1
            
        if dicS == dicT:
            return True
        else:
            return False
            

sol = Solution()

sol.isAnagram(s = "rat", t = "car")

