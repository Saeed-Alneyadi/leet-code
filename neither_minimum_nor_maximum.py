class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Gets the length of num and store it to variable to reduce the running of @len variable
        length = len(nums)

        # If length is greater than or equal to 0 and less than or equal to 2, return -1
        if length >= 0 and length <= 2:
            return -1
        else:
            # Remove the minimum and maximum from nums
            nums.remove(max(nums))
            nums.remove(min(nums))

            # Return the first element in nums, which is not the minimum or maximum
            return nums[0]
