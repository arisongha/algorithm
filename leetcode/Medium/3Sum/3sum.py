from itertools import combinations
class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        result = []
        for tu in combinations(nums, 3):
            sum_tu = sum(tu)
            sorted_tu = sorted(list(tu))
            if sum_tu == 0 and sorted_tu not in result:
                result.append(sorted_tu)
                
        return result
