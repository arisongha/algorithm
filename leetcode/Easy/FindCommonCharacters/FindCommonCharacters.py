
class Solution:
    def commonChars(self, A: 'List[str]') -> 'List[str]':
        
        dicAll = dict()
        for i,v in enumerate(A):
            dic = dict()
            for ind,val in enumerate(v):
                dic[val] = dic.get(val, 0) + 1
            
            dicAll[i] = dic
            
        result = []
        for k,v in dicAll.get(0).items():
            count = 0
            smallestVal = dicAll.get(0).get(k)
            for i in range(1,len(dicAll)):
                if dicAll.get(i).get(k) == None:
                    continue
                if dicAll.get(i).get(k) > 0:
                    count += 1
                    if dicAll.get(i).get(k) < smallestVal:
                        smallestVal = dicAll.get(i).get(k)
            
            if count == len(dicAll)-1:
                for m in range(smallestVal):
                    result.append(k)
                
        return result
        
        

sol = Solution()
sol.commonChars(["dadaabaa","bdaaabcc","abccddbb","bbaacdba","ababbbab","ccddbbba","bbdabbda","bdabaacb"]
)

