
class Solution:
    def hasGroupsSizeX(self, deck: 'List[int]') -> bool:
        if len(deck) <= 1:
            return False
        
        dic = dict()
        for i,v in enumerate(deck):
            dic[v] = dic.get(v, 0) + 1
            
        even = False
        odd = False
        smallestNum = 10000
        for k,v in dic.items():
            if v == 1:
                return False
            
            if v % 2 == 0:
                even = True
            else:
                odd = True
                
            if v < smallestNum:
                smallestNum = v
        
        if even and odd == False:
            return True
        
        else:
            for k,v in dic.items():
                if not v % smallestNum == 0:
                    return False
            return True
            


sol = Solution()
sol.hasGroupsSizeX([1,2,3,4,4,3,2,1])

