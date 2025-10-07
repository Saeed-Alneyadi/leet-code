class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Return 0 if length of @nums is less than 2
        if len(nums) < 2:
            return 0
        
        # Sort @nums array in increasing order
        nums.sort()

        # Return the maximum difference between two successive elements in sorted @nums
        return max([nums[idx + 1] - nums[idx] for idx in range(len(nums) - 1)])
