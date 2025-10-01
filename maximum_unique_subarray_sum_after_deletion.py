class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # If all number in @nums are negative...
        if all(num < 0 for num in nums):
            # Returning the maximum of negative numbers will give you the maximum value
            return max(nums)
        else:
            # Returning the sum of all positive numbers will give you the maximum value
            return sum(num for num in list(set(nums)) if num >= 0)
