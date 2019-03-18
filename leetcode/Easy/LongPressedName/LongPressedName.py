
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        beforeLetter = name[0]
        beforeLetterIndex = 0
        
        nameList = []
        for i,v in enumerate(name):
            if not beforeLetter == v:
                nameList.append({beforeLetter: i-beforeLetterIndex})
                beforeLetter = v
                beforeLetterIndex = i
            
            if i == len(name)-1:
                nameList.append({beforeLetter: len(name)-beforeLetterIndex})
                
        beforeLetter1 = typed[0]
        beforeLetterIndex1 = 0
        
        typedList = []
        for i,v in enumerate(typed):
            if not beforeLetter1 == v:
                typedList.append({beforeLetter1: i-beforeLetterIndex1})
                beforeLetter1 = v
                beforeLetterIndex1 = i
            
            if i == len(typed)-1:
                typedList.append({beforeLetter1: len(typed)-beforeLetterIndex1})
            
        if not len(nameList) == len(typedList):
            return False
        
        for i, (a,b) in enumerate(zip(nameList,typedList)): 
            for k,v in a.items():
                if b.get(k) == None:
                    return False
                if b.get(k) < v:
                    return False
                
        return True


sol = Solution()
sol.isLongPressedName(name = "alex", typed = "aaleex")

