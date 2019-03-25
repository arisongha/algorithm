
class Solution:
    def intersection(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        result = []
        
        setNums1 = list(set(nums1))
        setNums2 = list(set(nums2))
        
        dic = dict()
        
        for i,v in enumerate(setNums1):
            dic[v] = dic.get(v, 0) + 1
        
        for i,v in enumerate(setNums2):
            if not dic.get(v) ==  None:
                result.append(v)
                
        return result
        


sol = Solution()
sol.intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4])

