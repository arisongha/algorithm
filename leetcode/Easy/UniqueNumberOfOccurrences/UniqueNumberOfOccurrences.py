class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = dict()
        for i,v in enumerate(arr):
            dic[v] = dic.get(v, 0) + 1
            
        uniquelist = []
        for k,v in dic.items():
            if not v in uniquelist:
                uniquelist.append(v)
            else:
                return False
            
        return True
