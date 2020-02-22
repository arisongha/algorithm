class Solution:
    def longestSubsequence(self, arr: 'List[int]', difference: int) -> int:
        max_cnt = 0
        for i,v in enumerate(arr):
            cnt = 1
            beforenum = v
            for j in arr[i+1:]:
                if beforenum+difference == j:
                    cnt += 1
                    beforenum = j
            if cnt > max_cnt:
                max_cnt = cnt
        return max(max_cnt, 1)
