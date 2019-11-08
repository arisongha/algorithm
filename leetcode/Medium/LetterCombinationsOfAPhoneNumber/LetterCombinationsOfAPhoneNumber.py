
class Solution(object):
    def letterCombinations(self, digits: str) -> 'List[str]':
        
        if not digits:
            return []
        
        dic = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        
        def recursive(idx, cur, res):
            if len(cur) == len(digits):
                res.append("".join(cur))
                return
            letters = dic[digits[idx]]
            for letter in letters:
                recursive(idx+1, cur + [letter], res)
        
        ans = []
        recursive(0, [], ans)
        
        return ans


sol = Solution()
sol.letterCombinations("375")

