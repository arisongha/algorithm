
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.structure = []
        

    def addWord(self, word: 'str') -> 'None':
        """
        Adds a word into the data structure.
        """
        self.structure.append(word)
        

    def search(self, word: 'str') -> 'bool':
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        notDotIndexList = [i for i,value in enumerate(word) if value != "."]
        for i,v in enumerate(self.structure):
            if len(word) == len(v):
                compreIndexList = [i for i,(a,b) in enumerate(zip(word,v)) if a == b]
                if notDotIndexList == compreIndexList:
                    return True
        
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

wordDic = WordDictionary()

wordDic.addWord("bad")
wordDic.addWord("dad")

wordDic.search("ba.")

