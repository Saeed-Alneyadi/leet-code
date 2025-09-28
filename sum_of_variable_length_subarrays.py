class Solution(object):
    def subarraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Return the total sum of all elements from the subarray defined for each index in the array
        return sum([sum(num2 for num2 in nums[max(0, i - nums[i]):i + 1]) for i, num1 in enumerate(nums)])
