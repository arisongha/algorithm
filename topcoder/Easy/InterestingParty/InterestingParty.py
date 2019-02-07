
class InterestingParty:
    
    def __init__(self):
        self.result = 0
    
    def bestInvitation(self, first, second):
        
        wholeInter = first + second
        dic = dict()
        
        for inter in wholeInter :
            dic[inter] = dic.get(inter,0) + 1
        
        largestCnt = -1
        largestInter = ""

        for k,v in dic.items():
            if v > largestCnt:
                largestCnt = v
                largestInter = k
                
        print(largestCnt)
        self.result = largestCnt
        
        return self.result


party = InterestingParty()

party.bestInvitation(("t", "o", "p", "c", "o", "d", "e", "r", "s", "i", "n", "g", "l", "e", "r", "o", "u", "n", "d", "m", "a", "t", "c", "h", "f", "o", "u", "r", "n", "i"),("n", "e", "f", "o", "u", "r", "j", "a", "n", "u", "a", "r", "y", "t", "w", "e", "n", "t", "y", "t", "w", "o", "s", "a", "t", "u", "r", "d", "a", "y"))

