
class Solution:
    def countCharacters(self, words: 'List[str]', chars: str) -> int:
        dic = dict()
        for c in chars:
            dic[c] = dic.get(c, 0) + 1

        word_list = []
        for word in words:
            count = 0
            for w in word:
                if dic.get(w) != None and word.count(w) <= dic.get(w):
                    count += 1
                else:
                    break
            if count == len(word):
                word_list.append(word)
        
        result = 0
        for v in word_list:
            result += len(v)
            
        return result



sol = Solution()
sol.countCharacters(words = ["hello","world","leetcode"], chars = "welldonehoneyr")

