
class Solution:
    def findMinDifference(self, timePoints: 'List[str]') -> int:
        
        for i,v in enumerate(timePoints):
            if v == "00:00":
                timePoints[i] = "24:00"
        
        splitList = []
        splitList.append(timePoints[0].split(":"))
        splitList.append(timePoints[1].split(":"))
        
        for ind,li in enumerate(splitList):
            for i,num in enumerate(li):
                splitList[ind][i] = int(num)
                
        bigger = True
        
        if splitList[0][0] < splitList[1][0]:
            splitList[1][0] = splitList[1][0] - 1
            splitList[1][1] = splitList[1][1] + 60
            
        elif splitList[0][0] > splitList[1][0]:
            splitList[0][0] = splitList[0][0] - 1
            splitList[0][1] = splitList[0][1] + 60
            bigger = False
        
        result = 0
        if bigger == True:
            result = (splitList[1][0]-splitList[0][0])*60 + splitList[1][1]-splitList[0][1]  
        
        else:
            result = (splitList[0][0]-splitList[1][0])*60 + splitList[0][1]-splitList[1][1]
            
            
        return result



sol = Solution()
sol.findMinDifference(["23:23","12:50"])

