
class Solution:
    def replaceWords(self, dict: 'List[str]', sentence: str) -> str:
        
        sentenceList = sentence.split(" ")
        
        def haveRoot(word):
            for i,_ in enumerate(word):
                if word[:i] in dict:
                    return word[:i]
            return word

        return " ".join(map(haveRoot, sentenceList))
    

sol = Solution()
sol.replaceWords(dict = ["cat", "bat", "rat"], sentence = "the cattle was rattled by the battery")

