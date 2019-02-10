
class AnagramFree:
    
    def __init__(self):
        self.result = 0
        
    def getMaximumSubset(self, S):
        
        dicSet = set()
        
        for i,v in enumerate(S):
            dic = dict()
            for word in sorted(v):
                dic[word] = dic.get(word, 0) + 1
            dicSet.add((tuple(dic.items())))
        
        self.result = len(dicSet)
        print(self.result)
        
        return self.result
    

ana = AnagramFree()

ana.getMaximumSubset(("creation","sentence","reaction","sneak","star","rats","snake"))

