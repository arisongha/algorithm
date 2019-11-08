
class Solution:
    def combinationSum(self, candidates: 'List[int]', target: int) -> 'List[List[int]]':
        ans = []
        candidates = sorted(candidates)
        
        def dfs(nums, cur_set, cur_sum):
            for i in range(len(nums)):
                temp_sum = nums[i] + cur_sum
                if temp_sum == target:
                    ans.append(cur_set + [nums[i]])
                elif temp_sum > target:
                    return
                else:
                    dfs(nums[i:], cur_set + [nums[i]], temp_sum)
        
        dfs(candidates, [], 0)
        
        return ans


sol = Solution()
sol.combinationSum(candidates = [2,3,6,7], target = 7)

