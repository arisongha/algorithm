
class Solution:
    def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
        dic = dict()
        for i in range(0, len(strs)):
            word = ''.join(sorted(strs[i]))
            if not word in dic:
                dic[word] = [strs[i]]
            else:
                dic[word].append(strs[i])
        
        return dic.values()


sol = Solution()
sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

