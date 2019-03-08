class Solution:
    def generate(self, numRows: int) -> 'List[List[int]]':
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            beforeList = self.generate(numRows-1)[numRows-2]
            expendList = []
            expendList.append(1)
            for i,v in enumerate(beforeList):
                if not i == len(beforeList) - 1:
                    appendNum = beforeList[i] + beforeList[i+1]
                    expendList.append(appendNum)
            expendList.append(1)
            
            return self.generate(numRows-1) + [expendList]
            

sol = Solution()
sol.generate(100)