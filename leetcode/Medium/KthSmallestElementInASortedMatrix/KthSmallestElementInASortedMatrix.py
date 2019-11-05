
class Solution:
    def kthSmallest(self, matrix: 'List[List[int]]', k: int) -> int:
        merge_list = []
        for li in matrix:
            merge_list += li
            
        merge_list = sorted(merge_list)
        
        return merge_list[k-1]


sol = Solution()
sol.kthSmallest(matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,)

