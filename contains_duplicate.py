class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Return @True if there is a difference in length between @nums list and set, otherwise @False
        return len(nums) - len(set(nums)) > 0
