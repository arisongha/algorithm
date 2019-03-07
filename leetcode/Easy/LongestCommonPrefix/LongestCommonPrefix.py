
class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> str:
        
        wordlist = [word for i,word in enumerate(zip(*strs))]
        
        if len(wordlist) == 0:
            return ""
        
        for i,word in enumerate(wordlist):
            if len(set(word)) != 1:
                return strs[0][:i]
            else:
                if i == len(wordlist) - 1:
                    return strs[0][:i+1]
            

sol = Solution()
sol.longestCommonPrefix(["flow","flower"])

