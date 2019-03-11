
class Solution:
    def majorityElement(self, nums: 'List[int]') -> int:
        dic = dict()
        
        for i,v in enumerate(nums):
            dic[v] = dic.get(v, 0) + 1
        
        largestKey = ""
        largestNum = -1
        for k,v in dic.items():
            if v > largestNum:
                largestNum = v
                largestKey = k
                
        return largestKey


sol = Solution()
sol.majorityElement([3,2,2,3])

