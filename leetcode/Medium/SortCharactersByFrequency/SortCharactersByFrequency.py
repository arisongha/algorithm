
class Solution:
    def frequencySort(self, s: str) -> str:
        dic = dict()
        for i,v in enumerate(s):
            dic[v] = dic.get(v, 0) + 1
            
        li = sorted(dic.items(), key=lambda k:k[1])
        li.reverse()
        
        result = ""
        for i in li:
            result += i[0]*i[1]
            
        return result



sol = Solution()
sol.frequencySort("tree")

