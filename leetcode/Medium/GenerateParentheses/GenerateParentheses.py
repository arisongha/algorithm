import itertools

class Solution:
    def generateParenthesis(self, n: int) -> 'List[str]':
        parenthList = ["(",")"] * n
        permutation = itertools.permutations(parenthList)
        parenth_list = []
        for per in permutation:
            temp_stack = []
            for p in per:
                temp_stack.append(p)
                if temp_stack.count(")") > temp_stack.count("("):
                    temp_stack = []
                    break
            if temp_stack != [] and temp_stack not in parenth_list:
                parenth_list.append(temp_stack)
        result = []
        for v in parenth_list:
            result.append("".join(v))
        return result
            

sol = Solution()
sol.generateParenthesis(3)

