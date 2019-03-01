
class Solution:
    def wordBreak(self, s: str, wordDict: 'List[str]') -> bool:
        
        for i in range(len(wordDict)):
            dupS = s
            for word in wordDict[i:]:
                if word in dupS:
                    dupS = dupS.replace(word, ".")
            
            dupS = dupS.replace(".","")
            if len(dupS) == 0:
                return True
        
        return False


sol = Solution()
sol.wordBreak(s = "ccaccc", wordDict = ["cc","ac"])

