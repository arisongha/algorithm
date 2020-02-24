class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        lennum = n//2
        if n % 2 == 0:
            result = list(range(lennum*(-1),0)) + list(range(1,lennum+1))
        else:
            result = list(range(lennum*(-1),0)) + [0] + list(range(1,lennum+1))
            
        return result
