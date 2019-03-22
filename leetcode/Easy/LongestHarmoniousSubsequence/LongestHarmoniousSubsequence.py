
class Solution:
    def findLHS(self, nums: 'List[int]') -> int:
        dic = dict()
        for i,v in enumerate(nums):
            dic[v] = dic.get(v, 0) + 1
        
        largestNum = 0
        for k,v in dic.items():
            if not dic.get(k+1) == None:
                if v + dic.get(k+1) > largestNum:
                    largestNum = v + dic.get(k+1)
                    
        return largestNum



sol = Solution()
sol.findLHS([1,1,1,1])

