class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort() # Sort the array in increasing order

        for i in range(len(nums)):
            # Check if the index equals the value, if mismatch happens @False is returned
            if nums[i] != i:
                return i # Return the current value the for loop stopped on

        return len(nums) # If nothing found, length of @nums is returned
