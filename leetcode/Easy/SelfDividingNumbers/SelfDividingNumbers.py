
class Solution(object):
    def selfDividingNumbers(self, left, right):
        result = []
        for i in range(left, right+1):
            s = str(i)
            boolean = True
            for d in s:
                if d=="0" or i%int(d)!=0:
                    boolean = False
                    break
            if boolean:
                result.append(i)
        return result



sol = Solution()
sol.selfDividingNumbers(left = 1, right = 22)

