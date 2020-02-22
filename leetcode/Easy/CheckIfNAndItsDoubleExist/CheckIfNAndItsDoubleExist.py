class Solution:
    def checkIfExist(self, arr: 'List[int]') -> bool:
        arr.sort()
        for i,v in enumerate(arr):
            if v > 0:
                if 2*v in arr[i+1:]:
                    return True
            elif v == 0:
                if arr.count(0) > 1:
                    return True
            else:
                if 2*v in arr[:i+1]:
                    return True
        return False
