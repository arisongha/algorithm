
class Solution:
    def numPairsDivisibleBy60(self, time: 'List[int]') -> int:
        result = []
        for i,v in enumerate(time):
            for ind, val in enumerate(time):
                if not i == ind:
                    if (v + val)%60 == 0:
                        if not set([i,ind]) in result:
                            result.append(set([i,ind]))
        
        return len(result)



sol = Solution()
sol.numPairsDivisibleBy60([30,20,150,100,40])

