class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Return whether there is duplicates in @nums or not
        return len([num for num in set(nums) if nums.count(num) > 1]) > 0
