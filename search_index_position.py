class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # If @target exist in @nums, the @index() function will return the index of @target in @nums
        if target in nums:
            return nums.index(target)
        else:
            # If @target doesn't exist in @nums, this code segmenet will run

            # If @target is less than the first element, the index of the first element will be returned
            if target < nums[0]:
                return 0

            # Loops to get where @target index should be
            for idx in range(len(nums) - 1):
                if target > nums[idx] and target < nums[idx + 1]:
                    return idx + 1

            # If @target is greater than the last element, the index of the last element will be returned
            if target > nums[len(nums) - 1]:
                return len(nums)
