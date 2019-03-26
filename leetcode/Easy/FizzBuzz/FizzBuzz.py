
class Solution:
    def fizzBuzz(self, n: int) -> 'List[str]':
        
        result = []
    
        for i in range(1, n+1):
            word = ""
            if i % 3 == 0:
                word += "Fizz"
            
            if i % 5 == 0:
                word += "Buzz"
                
            if word == "":
                word = str(i)
                
            result.append(word)
            
        return result
            


sol = Solution()
sol.fizzBuzz(n=15)

