class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Removes the first maximum number
        first = max(nums)
        while first in nums:
            nums.remove(first)

        # If no elements left in @nums, @first, which is first maximum is returned
        if len(nums) == 0:
            return first

        # Removes the second maximum number
        second = max(nums)
        while second in nums:
            nums.remove(second)

        # If no elements left in @nums, @first, which is first maximum is returned
        if len(nums) == 0:
            return first

        # Return the third maximum number
        return max(nums)
