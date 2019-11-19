class Solution:
    def plusOne(self, digits: 'List[int]') -> 'List[int]':
        str_digit = ""
        for digit in digits:
            str_digit += str(digit)
        plus_str_digit = str(int(str_digit) + 1)
        result = []
        for v in plus_str_digit:
            result.append(int(v))
        return result


sol = Solution()
sol.plusOne([4,3,2,2])

