
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        max_word = ""
        big = ""
        small = ""
        if len(str1) > len(str2):
            big = str1
            small = str2
        else:
            big = str2
            small = str1
            
        for i,v in enumerate(small):
            if small[:i+1] in big:
                if len(big) % len(small[:i+1]) == 0 and len(small) % len(small[:i+1]) == 0:
                    if (len(big)//len(small[:i+1]))*small[:i+1] == big and (len(small)//len(small[:i+1]))*small[:i+1] == small:
                        max_word = small[:i+1]
                
        return max_word



sol = Solution()
sol.gcdOfStrings(str1 = "ABABAB", str2 = "ABAB")

