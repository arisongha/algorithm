
class Solution:
    def findDuplicate(self, nums: 'List[int]') -> int:
        dic = dict()
        for num in nums:
            if dic.get(num) is 1:
                return num
            else:
                dic[num] = dic.get(num, 0) + 1

                
sol = Solution()
sol.findDuplicate([3,1,3,4,2])

