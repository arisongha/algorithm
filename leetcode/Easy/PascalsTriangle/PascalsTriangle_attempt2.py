class Solution:
    def __init__(self):
        self.dic = dict()
    
    def generate(self, numRows: int) -> 'List[List[int]]':
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        elif self.dic.get(numRows) != None:
            return self.dic.get(numRows)
        else:
            beforeList = self.generate(numRows-1)
            expendList = []
            expendList.append(1)
            for i,v in enumerate(beforeList[numRows-2]):
                if not i == len(beforeList[numRows-2]) - 1:
                    appendNum = beforeList[numRows-2][i] + beforeList[numRows-2][i+1]
                    expendList.append(appendNum)
            expendList.append(1)
            
            self.dic[numRows] = self.generate(numRows-1) + [expendList]
            
            return self.dic[numRows]
            

sol = Solution()
sol.generate(100)