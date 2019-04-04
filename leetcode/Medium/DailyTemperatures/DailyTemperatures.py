
class Solution:
    def dailyTemperatures(self, T: 'List[int]') -> 'List[int]':
        result = []
        for i in range(0,len(T)):
            todayTemp = T[i:][0]
            count = 0
            for ind,val in enumerate(T[i:]):
                if val > todayTemp:
                    result.append(count)
                    break
                else:
                    count += 1
                    
                if ind == len(T[i:])-1:
                    result.append(0)
                    
        return result



sol = Solution()
sol.dailyTemperatures(T = [73, 74, 75, 71, 69, 72, 76, 73])

