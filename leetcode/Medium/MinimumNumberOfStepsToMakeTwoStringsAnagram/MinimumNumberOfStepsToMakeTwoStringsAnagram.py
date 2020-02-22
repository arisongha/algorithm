class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sdic = dict()
        for v in s:
            sdic[v] = sdic.get(v, 0) + 1
        tdic = dict()
        for v in t:
            tdic[v] = tdic.get(v, 0) + 1
            
        count = 0
        for k,v in sdic.items():
            if v - tdic.get(k, 0) > 0:
                count += v - tdic.get(k, 0)
        
        return count
