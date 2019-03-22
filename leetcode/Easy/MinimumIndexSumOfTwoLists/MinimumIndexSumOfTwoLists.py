
class Solution:
    def findRestaurant(self, list1: 'List[str]', list2: 'List[str]') -> 'List[str]':
        dicA = dict()
        dicB = dict()
        
        for i,v in enumerate(list1):
            dicA[v] = dicA.get(v, i)
            
        for i,v in enumerate(list2):
            dicB[v] = dicB.get(v, i)
            
        
        leastNum = 2000
        leastMenu = ""
        leastDic = dict()
        for k,v in dicA.items():
            if not dicB.get(k) == None:
                leastDic[k] = leastDic.get(k, v + dicB.get(k))
                
                if v + dicB.get(k) < leastNum:
                    leastNum = v + dicB.get(k)
                
        result = []
        for k,v in leastDic.items():
            if v == leastNum:
                result.append(k)
                
        return result
                    
        

sol = Solution()
sol.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],["KFC","Burger King","Tapioca Express","Shogun"])

