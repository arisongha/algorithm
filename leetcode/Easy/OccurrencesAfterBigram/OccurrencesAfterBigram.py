class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> 'List[str]':
        temp = []
        result = []
        text_list = text.split(" ")
        for i,v in enumerate(text_list):
            if len(temp) == 0 and v == first:
                temp.append(v)
                continue
                
            if len(temp) != 0 and temp[-1] == first:
                if v == first or v == second:
                    temp.pop()
                    temp.append(v)
                else:
                    temp = []
                continue
            
            if len(temp) != 0 and temp[-1] == second:
                result.append(v)
                temp.pop()
                if v == first:
                    temp.append(v)
        return result
