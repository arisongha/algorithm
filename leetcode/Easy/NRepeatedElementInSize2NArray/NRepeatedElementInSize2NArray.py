
class Solution:
    def repeatedNTimes(self, A: 'List[int]') -> int:
        dic = dict()
        for i,v in enumerate(A):
            dic[v] = dic.get(v, 0) + 1
            if dic.get(v) > 1:
                return v



sol = Solution()
sol.repeatedNTimes([2,1,2,5,3,2])

