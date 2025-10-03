class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Variables Initialization
        count = 0

        # Loops until sum of @nums is divisible by k
        while sum(nums) % k > 0:
            # Variables Initialization
            idx = 0
            nums[idx] -= 1
            count += 1

            # Checks if the nums element reachs 0 so it moves to the next one by incrementing @idx
            if nums[idx] == 0:
                idx += 1

        # Return @count which contains the minmu number of operations required to make the sum of the array divisible by @k
        return count
