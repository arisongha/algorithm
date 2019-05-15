
class Solution:
    def shiftingLetters(self, S: str, shifts: 'List[int]') -> str:
        dic = {
            "a" : 1,
            "b" : 2,
            "c" : 3,
            "d" : 4,
            "e" : 5,
            "f" : 6,
            "g" : 7,
            "h" : 8,
            "i" : 9,
            "j" : 10,
            "k" : 11,
            "l" : 12,
            "m" : 13,
            "n" : 14,
            "o" : 15,
            "p" : 16,
            "q" : 17,
            "r" : 18,
            "s" : 19,
            "t" : 20,
            "u" : 21,
            "v" : 22,
            "w" : 23,
            "x" : 24,
            "y" : 25,
            "z" : 26,
        }
        
        letter_list = []
        for i,v in enumerate(S):
            letter_list.append(dic.get(v))
            
        for i,v in enumerate(letter_list):
            num = (letter_list[i] + sum(shifts[i:]))%26
            if num == 0:
                num = 26
            letter_list[i] = num
            
            
        
        result_word = ""
        dic_reverse = dict()

        for k,v in dic.items():
            string_val = str(v)
            dic_reverse[string_val] = k
            
        for i,v in enumerate(letter_list):
            result_word += dic_reverse.get(str(v))
            
        return result_word



sol = Solution()
sol.shiftingLetters(S = "z", shifts = [52])

