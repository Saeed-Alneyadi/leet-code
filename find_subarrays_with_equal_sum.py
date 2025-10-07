class Solution(object):
    def findSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sums = [sum([nums[idx], nums[idx + 1]]) for idx in range(len(nums) - 1)]

        for s in set(sums):
            if sums.count(s) > 1:
                return True
        
        return False
