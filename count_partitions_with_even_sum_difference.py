class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Store all sum difference of left and right parition of array @nums to @allSums
        allSums = [sum(nums[:i]) - sum(nums[i:]) for i in range(len(nums) - 1)]

        # Return the length of array that consist of even sums
        return len([total for total in allSums if total % 2 == 0])
