
class Solution:
    def titleToNumber(self, s: str) -> int:
        dic = {"A":1,
              "B":2,
              "C":3,
              "D":4,
              "E":5,
              "F":6,
              "G":7,
              "H":8,
              "I":9,
              "J":10,
              "K":11,
              "L":12,
              "M":13,
              "N":14,
              "O":15,
              "P":16,
              "Q":17,
              "R":18,
              "S":19,
              "T":20,
              "U":21,
              "V":22,
              "W":23,
              "X":24,
              "Y":25,
              "Z":26,
              }
        
        sList = list(s)
        sList.reverse()
        step = 1
        result = 0
        for i,v in enumerate(sList):
            if i == 0:
                result += dic.get(v) 
            else:
                result += dic.get(v) * 26**step
                step += 1
                
        return result


sol = Solution()
sol.titleToNumber("ZY")

