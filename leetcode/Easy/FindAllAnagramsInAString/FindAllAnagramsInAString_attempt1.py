class Solution:
    def findAnagrams(self, s: str, p: str) -> 'List[int]':
        plen = len(p)
        resultList = []
        dic = dict()
        for i,v in enumerate(p):
            dic[v] = dic.get(v,0) + 1
        
        for i,v in enumerate(s):
            sliceWord = s[i:i+plen]
            dic2 = dict()
            for index,value in enumerate(sliceWord):
                dic2[value] = dic2.get(value,0) + 1
            
            if dic == dic2:
                resultList.append(i)
        
        return resultList
    
  
sol = Solution()
sol.findAnagrams(s="abab", p="ab")
