
class AB:
    
    def __init__(self):
        self.result = ""
    
    def createString(self, N, K):
        
        if K > N//2 * (N - N//2) :
            return self.result
        
        beforeN = 0
        evenBool = True
        
        for i in range(1,35):
            if i**2 <= K < i*(i+1) :
                beforeN = i
                evenBool = True
                
            elif i*(i+1) <= K < (i+1)**2 :
                beforeN = i
                evenBool = False
        
        loopNum = 0
        if evenBool == True :
            loopNum = 2*beforeN
        else :
            loopNum = 2*beforeN + 1
        
        wordList = []
        for i in range(loopNum) :
            if i < loopNum//2 :
                wordList.append("A")
            else :
                wordList.append("B")
        
        while len(wordList) < N :
            
            if wordList.count("A") * wordList.count("B") == K :
                wordList.insert(0, "B")
            else :
                backIndex = K - wordList.count("A") * wordList.count("B")
                wordList.insert(len(wordList) - backIndex, "A")
        
        for i,v in enumerate(wordList) :
            self.result += v
                
        return self.result 
                

ab = AB()

ab.createString(10,12)

