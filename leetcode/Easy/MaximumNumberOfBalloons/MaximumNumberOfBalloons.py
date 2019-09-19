
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = 0
        text_list = list(text)
        boolean = True
        while boolean:
            for c in "balloon":
                if c in text_list:
                    text_list.remove(c)
                    if c == "n":
                        count += 1
                else:
                    boolean = False
                    break
            
        return count
            

sol = Solution()
sol.maxNumberOfBalloons(text = "loonbalxballpoon")

