class Solution:
    def countSubstrings(self, s: str) -> int:
        result = []
        for i in range(0, len(s)):
            count = i+1
            while count != len(s)+1:
                temp = s[i:count]
                if temp == temp[::-1]:
                    result.append(temp)
                count += 1
        return result
