import itertools

class Solution:
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        permutations = itertools.permutations(nums)
        result = []
        for permutation in permutations:
            result.append(list(permutation))
            
        return result


sol = Solution()
sol.permute([1,2,3])

