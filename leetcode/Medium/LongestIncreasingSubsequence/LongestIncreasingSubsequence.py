class Solution:
    def lengthOfLIS(self, nums: 'List[int]') -> int:
        result_list = []
        for ind, num in enumerate(nums):
            temp_list = []
            temp_list.append(num)
            before_num = num
            for i, n in enumerate(nums[ind+1:]):
                if n > before_num:
                    temp_list.append(n)
                    before_num = n
            result_list.append(len(temp_list))
            
        return max(result_list)


sol = Solution()
sol.lengthOfLIS([10,9,2,5,3,7,101,18])

