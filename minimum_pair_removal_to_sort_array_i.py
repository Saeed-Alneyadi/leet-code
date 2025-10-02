class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Variable Initialization
        count = 0
        
        # Loop stops when @nums is in increasing order
        while nums != sorted(nums):
            sums = [nums[idx] + nums[idx + 1] for idx in range(len(nums) - 1)] # Creates @sums, which is sums of every adjacent pairs in @nums
            min_sum = min(sums) # Get the minimum sum in @sums
            min_idx = sums.index(min_sum) # Get the index of the minimum sum in @sums

            # Set @nums to a new @nums with adjacent pairs replaced with minimum sum
            nums = nums[:min_idx] + nums[min_idx + 2:]
            nums.insert(min_idx, min_sum)
            # print(nums)

            # Incrementing @count
            count += 1

        # Return @count which is the minimum number of operations needed to make the array non-decreasing
        return count
