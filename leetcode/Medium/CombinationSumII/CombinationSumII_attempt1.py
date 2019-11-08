
import itertools

class Solution:
    def combinationSum2(self, candidates: 'List[int]', target: int) -> 'List[List[int]]':
        if sum(candidates) == target:
            return [candidates]
    
        result = []
        candidates = sorted(candidates)
        sum_ = 0
        count = 0
        for i,v in enumerate(candidates):
            sum_ += v
            if sum_ >= target:
                count = i
        
        for i in range(1,count+1):
            combinations = itertools.combinations(candidates, i)
            for v in combinations:
                temp_sorted_list = sorted(list(v))
                if sum(list(v)) == target and temp_sorted_list not in result:
                    result.append(temp_sorted_list)
        
        return result


sol = Solution()
sol.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8)

