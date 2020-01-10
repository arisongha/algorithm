class Solution:
    def minimumAbsDifference(self, arr: 'List[int]') -> 'List[List[int]]':
        mini = 1000000
        result = []
        for i in arr:
            for j in arr:
                if not i == j:
                    if i > j and i-j<mini:
                        mini = i-j
                    elif i < j and j-i<mini:
                        mini = j-i
                        
        for i in arr:
            for j in arr:
                temp = []
                if not i == j:
                    if i > j and i-j==mini:
                        mini = i-j
                        temp.append(j)
                        temp.append(i)
                        result.append(temp)
        
        return sorted(result)
