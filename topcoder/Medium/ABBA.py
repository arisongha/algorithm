
class ABBA:
    def __init__(self):
        self.result = ""
    
    def canObtain(self, initial, target):
        
        initail_len = len(initial)
        beforeword = target
        
        while len(beforeword) > initail_len :
            
            if beforeword[len(beforeword)-1] == "A":
                beforeword = beforeword[:len(beforeword)-1]
            else :
                beforeword = beforeword[:len(beforeword)-1]
                beforeword = beforeword[::-1]
            
            if beforeword == initial :
                self.result = "POSSIBLE"
            else :
                self.result = "IMPOSSIBLE"
                
        print(self.result)
                
        return self.result
    

jamiegame = ABBA()

result = jamiegame.canObtain("BBBBABABBBBBBA", "BBBBABABBABBBBBBABABBBBBBBBABAABBBAA")

