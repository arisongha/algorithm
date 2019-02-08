
class ThePalindrome:
    
    def __init__(self):
        self.result = 0
        
    def find(self, s):
        
        palinBool = False
        
        for index,_ in enumerate(s): 
            checkWord = s[index:]
            
            for i in range(len(checkWord)//2):
                if not checkWord[i] == checkWord[len(checkWord)-(i+1)]:
                    palinBool = False
                    break
                
                palinBool = True
                self.result = len(s) + index
            
            if palinBool == True:
                break
            elif palinBool == False and index == len(s)-1:
                self.result = len(s)*2 -1
        
        print(self.result)
        return self.result


palin = ThePalindrome()

palin.find("abdfhdyrbdbsdfghjkllkjhgfds")

