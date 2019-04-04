
class Solution:
    def topKFrequent(self, nums: 'List[int]', k: int) -> 'List[int]':
        dic = dict()
        for i,v in enumerate(nums):
            dic[v] = dic.get(v, 0) + 1
        
        dicList = sorted(dic.items(), key=lambda k:k[1])
        dicList.reverse()
        result = []
        print(dicList)
        for i in dicList[:k]:
            result.append(i[0])
                
        return result
        


sol = Solution()
sol.topKFrequent(nums = [1,1,1,2,2,3], k = 2)

