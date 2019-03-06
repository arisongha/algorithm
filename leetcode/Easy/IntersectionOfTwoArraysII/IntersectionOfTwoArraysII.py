
class Solution:
    def intersect(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        
        dic1 = dict()
        dic2 = dict()
        for ind1, num1 in enumerate(nums1):
            dic1[num1] = dic1.get(num1, 0) + 1
            
        for ind2, num2 in enumerate(nums2):
            dic2[num2] = dic2.get(num2, 0) + 1
        
        result = []
        for key, value in dic1.items():
            if dic2.get(key) != None:
                if dic1.get(key) <= dic2.get(key):
                    result.extend([key]*dic1.get(key))
                else:
                    result.extend([key]*dic2.get(key))
        
        return result
        

sol = Solution()
sol.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4])

