
class Solution:
    def findRelativeRanks(self, nums: 'List[int]') -> 'List[str]':
        
        if not nums:
            return []
        
        reversenums = sorted(nums, reverse=True)
        count = len(nums)
        dic = dict()
        
        dic[reversenums[0]] = "Gold Medal" 
        
        if count > 1:
            dic[reversenums[1]] = "Silver Medal" 
        
        if count > 2:
            dic[reversenums[2]] = "Bronze Medal" 
            
        for i in range(3, count):
            dic[reversenums[i]] = str(i+1)
        
        result = []
        for num in nums:
            result.append(dic.get(num))
        
        return result



sol = Solution()
sol.findRelativeRanks([10,3,8,9,4])

