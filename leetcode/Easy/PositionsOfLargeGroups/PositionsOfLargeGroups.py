
class Solution:
    def largeGroupPositions(self, S: str) -> 'List[List[int]]':
        start = 0
        count = 1
        letter = ""
        
        result = []
        
        for i,v in enumerate(S):
            if not v == letter:
                if count >= 3:
                    result.append([start, start + count - 1])
                start = i
                count = 1
                letter = v

            else:
                count += 1
            
            if i == len(S) - 1 and count >= 3:
                result.append([start, start + count - 1])
            
        return result
                    


sol = Solution()
sol.largeGroupPositions("aaaa")

