
import collections

class Solution:
    def findPairs(self, nums: 'List[int]', k: int) -> int:
        
        if k < 0:
            return 0

        result = 0
        count = collections.Counter(nums)
        
        for num in count:
            if k != 0:
                if num - k in count:
                    result += 1
            else:
                if count[num] > 1:
                    result += 1
        return result



sol = Solution()
sol.findPairs([3, 1, 4, 1, 5], k = 2)

