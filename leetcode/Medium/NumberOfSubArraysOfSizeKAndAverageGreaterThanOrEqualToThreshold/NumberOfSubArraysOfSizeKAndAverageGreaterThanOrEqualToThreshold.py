from itertools import combinations
class Solution:
    def numOfSubarrays(self, arr: 'List[int]', k: int, threshold: int) -> int:
        count = 0
        num_list = []
        for nums in combinations(arr, 3):
            avg = sum(nums) // k
            if nums not in num_list and avg >= threshold:
                count += 1
                num_list.append(nums)
                
        return count
        
