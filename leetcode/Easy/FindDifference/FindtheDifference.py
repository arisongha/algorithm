

class Solution:
    def findTheDifference(self, s: 'str', t: 'str') -> 'str':
        
        slist = sorted(s)
        tlist = sorted(t)
        
        mismatch = [i for i,(a,b) in enumerate(zip(slist,tlist)) if a != b]
        
        if len(mismatch) == 0:
            return tlist[len(tlist)-1]
        else:
            return tlist[mismatch[0]]


sol = Solution()

sol.findTheDifference(s = "ae",t = "eaa")

