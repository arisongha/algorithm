

class Solution(object):
    def findUnsortedSubarray(self, nums: 'List[int]') -> int:

        sortedNums = sorted(nums)
        if sortedNums == nums:
            return 0 
        else:
            checklist = [i for i,(a,b) in enumerate(zip(sortedNums, nums)) if a != b]
            return len(nums[checklist[0]:checklist[len(checklist)-1]+1])


sol = Solution()
sol.findUnsortedSubarray([1,2,3,4])

