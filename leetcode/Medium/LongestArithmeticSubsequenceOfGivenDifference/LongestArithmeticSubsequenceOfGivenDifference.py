class Solution:
    def longestSubsequence(self, arr: 'List[int]', difference: int) -> int:
        result = []
        for i,v in enumerate(arr):
            beforeNum = arr[i]
            tempList = []
            
            for ind,val in enumerate(arr[i+1:]):
                if val == beforeNum + difference:
                    if len(tempList) == 0:
                        tempList.append(beforeNum)
                        tempList.append(val)
                    else:
                        tempList.append(val)
                    beforeNum = val
            result.append(tempList)
        
        maxLength = 0
        maxLengthList = []
        for v in result:
            if len(v) > maxLength:
                maxLength = len(v)
                maxLengthList = v
                
        if len(maxLengthList) == 0:
            return 1
        return len(maxLengthList)
