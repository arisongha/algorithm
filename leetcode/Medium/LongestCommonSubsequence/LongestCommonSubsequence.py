class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        short = ""
        long = ""
        if len(text1) >= len(text2):
            long = text1
            short = text2
        else:
            long = text2
            short = text1
            
        long_dic = dict()
        for i,v in enumerate(long):
            long_dic[v] = i+1
            
        before = 0
        tempstr = ""
        result = []
        for i,v in enumerate(short):
            if long_dic.get(v) and long_dic[v] > before:
                tempstr += v
                before = long_dic[v]
                result.append(tempstr)
            elif long_dic.get(v) and long_dic[v] < before:
                temp = v
                before = long_dic[v]
                result.append(tempstr)
                
        if len(result) == 0:
            return 0
        else:
            return max([len(x) for x in result])

