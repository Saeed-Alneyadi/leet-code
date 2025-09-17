class Solution(object):
    def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Return the smallest index i of nums such that i % 10 = nums[i]
        for idx, num in enumerate(nums):
            if idx % 10 == num:
                return idx

        # Return -1 if such index does not exist
        return -1
