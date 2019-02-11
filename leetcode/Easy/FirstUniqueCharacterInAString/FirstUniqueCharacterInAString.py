
class Solution:
    def firstUniqChar(self, s: 'str') -> 'int':
        
        dic = dict()
        dic2 = dict()
        
        for x in s:
            dic[x] = dic.get(x, 0) + 1

        for k,v in dic.items():
            if v == 1:
                findIndex = s.find(k)
                dic2[k] = dic2.get(k, findIndex)
                
        if len(dic2) == 0:
            return -1

        smallest = len(s)
        smallestWord = ""
        
        for k,v in dic2.items():
            if v < smallest:
                smallest = v

        return smallest


sol = Solution()

sol.firstUniqChar("loveleetcode")

