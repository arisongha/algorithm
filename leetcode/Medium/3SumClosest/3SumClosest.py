from itertools import combinations
class Solution:
    def threeSumClosest(self, nums: 'List[int]', target: 'int') -> 'int':
        min_closest = 10**6
        min_sum = 0
        for tu in combinations(nums, 3):
            sum_nums = sum(tu)
            if abs(sum_nums-target) < min_closest:
                min_closest = abs(sum_nums-target)
                min_sum = sum_nums
        return min_sum
