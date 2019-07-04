
class Solution:
    def hasGroupsSizeX(self, deck: 'List[int]') -> bool:
        if len(deck) <= 1:
            return False
        
        dic = dict()
        min = 1000000
        for i,v in enumerate(deck):
            dic[v] = dic.get(v, 0) + 1
            
        for k,v in dic.items():
            if dic.get(k) < min:
                min = dic.get(k)
        
        if min < 2:
            return False
                
        if min > 2 and min % 2 == 0:
            min = 2
                
                
        for k,v in dic.items():
            if v % min != 0:
                return False
                        
        return True
            



sol = Solution()
sol.hasGroupsSizeX([1,2,3,4,4,3,2,1])

