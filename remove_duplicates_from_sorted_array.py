class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Variables Initialization
        idx = 1

        # Remove duplicates
        while nums != set(nums) and idx < len(nums):
            if nums[idx - 1] == nums[idx]:
                nums.pop(idx - 1)
            else:
                idx += 1

        # Return the new length of the @nums
        return len(nums)
