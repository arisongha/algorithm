
class Cryptography:
    
    def __init__(self):
        self.result = 0
        
    def encrypt(self, numbers):
        
        numberList = list(numbers)
        minimumNum = min(numberList)
        for i,val in enumerate(numberList):
            if val == minimumNum:
                numberList[i] += 1
                break
        
        returnNum = 1
        for num in numberList:
            returnNum *= num
        
        self.result = returnNum
        print(self.result)

        return self.result


crypto = Cryptography()

crypto.encrypt((1000,999,998,997,996,995))

