
class Solution:
    def multiply(self, arr):
        return eval('*'.join([str(n) for n in arr]))
    
    def productExceptSelf(self, nums: 'List[int]') -> 'List[int]':
        if list(set(nums))[0] == 0:
            return nums
        result = []
        for i in range(1, len(nums)+1):
            combinations = itertools.combinations(nums, i)
            for combination in combinations:
                mul = self.multiply(list(combination))
                if not mul in nums:
                    result.append(mul)
                
        return sorted((list(set(result))), reverse=True)


sol = Solution()
sol.productExceptSelf([1,2,3,4])

