
class Solution:
    def nextGreatestLetter(self, letters: 'List[str]', target: str) -> str:
        sortedLetters = sorted(letters)
        
        count = 0
        for letter in sortedLetters:
            count += 1
            if letter > target:
                return letter
            
        if count == len(sortedLetters):
            return sortedLetters[0]



sol = Solution()
sol.nextGreatestLetter(letters = ["c", "f", "j"], target = "j")

