
class Solution:
    def diStringMatch(self, S: str) -> 'List[int]':

        left = 0
        right = 0
        li = [0]
        
        for i in S:
            if i == "I":
                right += 1
                li.append(right)
            else:
                left -= 1
                li.append(left)

        return [i - left for i in li]



sol = Solution()
sol.diStringMatch("IDID")

