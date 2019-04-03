
class Solution:
    def uniqueMorseRepresentations(self, words: 'List[str]') -> int:
        morseDic = {"a":".-",
                    "b":"-...",
                    "c":"-.-.",
                    "d":"-..",
                    "e":".",
                    "f":"..-.",
                    "g":"--.",
                    "h":"....",
                    "i":"..",
                    "j":".---",
                    "k":"-.-",
                    "l":".-..",
                    "m":"--",
                    "n":"-.",
                    "o":"---",
                    "p":".--.",
                    "q":"--.-",
                    "r":".-.",
                    "s":"...",
                    "t":"-",
                    "u":"..-",
                    "v":"...-",
                    "w":".--",
                    "x":"-..-",
                    "y":"-.--",
                    "z":"--.."}
        
        morseList = []
        for word in words:
            morse = ""
            for w in word:
                morse += morseDic.get(w)
            morseList.append(morse)
        
        dic = dict()
        for i, morse in enumerate(morseList):
            dic[morse] = dic.get(morse, 0) + 1
            
        return len(dic)
            


sol = Solution()
sol.uniqueMorseRepresentations(words = ["gin", "zen", "gig", "msg"])

