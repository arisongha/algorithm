
class Solution:
    
    def hammingDistance(self, x: int, y: int) -> int:
        result1, idx1 = 0,0
        result2, idx2 = 0,0

        while (x >=1):

            remainder1 = x % 2
            x = x // 2
            result1 += (10**idx1)* remainder1
            idx1 +=1
        
        while (y >=1):

            remainder2 = y % 2
            y = y // 2
            result2 += (10**idx2)* remainder2
            idx2 +=1
        
        list1 = []
        list2 = []
        for i in str(result1):
            list1.append(i)
            
        for i in str(result2):
            list2.append(i)
        
        list2.reverse()
        
        for i in range(abs(len(list2) - len(list1))):
            list1.append("0")
            
        resultList = [i for i,(a,b) in enumerate(zip(list1,list2)) if a != b]    
        
        return len(resultList)


sol = Solution()
sol.hammingDistance(x = 1, y = 3)

