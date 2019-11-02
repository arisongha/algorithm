
import itertools

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        list_ = [0]*(m-1) + [1]*(n-1)
        permutation = itertools.permutations(list_)
        
        return len(set(permutation))
        

sol = Solution()
sol.uniquePaths(m=7, n=3)

