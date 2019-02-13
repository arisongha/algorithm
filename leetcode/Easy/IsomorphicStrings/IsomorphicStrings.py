
class Solution:
    def isIsomorphic(self, s: 'str', t: 'str') -> 'bool':
        
        dicS = dict()
        dicT = dict()
        if len(s) == len(t):
            for i,v in enumerate(s):
                if dicS.get(s[i]) == None: 
                    dicS[s[i]] = dicS.get(s[i], i)
            
            for i,v in enumerate(t):
                if dicT.get(t[i]) == None:
                    dicT[t[i]] = dicT.get(t[i], i)
                    
            slist = []
            tlist = []
            for i,v in enumerate(s):
                slist.append(dicS.get(v))
                
            for k,v in enumerate(t):
                tlist.append(dicT.get(v))
                
            if slist == tlist:
                return True
            else:
                return False
        else:
            return False
        

sol = Solution()

sol.isIsomorphic(s = "abab", t = "baba")

