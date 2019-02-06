
class KiwiJuiceEasy:
    
    def __init__(self):
        self.result = tuple()
    
    def thePouring(self, capacities, bottles, fromId, toId):
        
        capacities = list(capacities)
        bottles = list(bottles)
        
        for i,_ in enumerate(fromId):
            
            if bottles[fromId[i]] + bottles[toId[i]] <= capacities[toId[i]]:
                bottles[toId[i]] = bottles[fromId[i]] + bottles[toId[i]]
                bottles[fromId[i]] = 0
            
            else:
                bottles[fromId[i]] = bottles[fromId[i]] + bottles[toId[i]] - capacities[toId[i]]
                bottles[toId[i]] = capacities[toId[i]]
        
        self.result = tuple(bottles)
        print(self.result)
        
        return self.result


kiwi = KiwiJuiceEasy()

kiwi.thePouring((14, 35, 86, 58, 25, 62), (6, 34, 27, 38, 9, 60), (1, 2, 4, 5, 3, 3, 1, 0), (0, 1, 2, 4, 2, 5, 3, 1))

