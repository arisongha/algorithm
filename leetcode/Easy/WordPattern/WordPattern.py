
class Solution:
    def wordPattern(self, pattern: 'str', str: 'str') -> 'bool':
        
        patternIndexlist = list()
        
        for i,v in enumerate(pattern):
            patternIndexlist.append(pattern.find(v))
        
        strlist = str.split(" ")
        strIndexlist = list()
        strDic = dict()
        
        for i,v in enumerate(strlist):
            strDic[v] = strDic.get(v, i)
        
        for i,v in enumerate(strlist):
            strIndexlist.append(strDic.get(v))
            
        if patternIndexlist == strIndexlist:
            return True
        else:
            return False
        

sol = Solution()

sol.wordPattern(pattern = "abba", str = "dog cat cat dog")

