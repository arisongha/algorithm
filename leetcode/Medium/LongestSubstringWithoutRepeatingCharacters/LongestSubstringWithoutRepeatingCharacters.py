class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        max_ = 0
        for i in range(0, len(s)):
            temp_char = s[i]
            for j in range(i+1, len(s)+1):
                result = ""
                dic = dict()
                temp_s = s[i:j]
                for v in temp_s:
                    dic[v] = dic.get(v, 0) + 1
                if len(dic) == len(temp_s):
                    if len(temp_s) > max_:
                        max_ = len(temp_s)
        
        return max_
