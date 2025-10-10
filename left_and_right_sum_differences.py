class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Return an array where it consist of difference between the left and right sum in @nums subarray
        return [abs(sum(nums[:i]) - sum(nums[i + 1:])) for i in range(len(nums))]
