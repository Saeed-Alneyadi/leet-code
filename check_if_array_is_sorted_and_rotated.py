class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Variable Initialization
        sort = sorted(nums)
        size = len(nums)
        idx = 0

        while idx < size:
            nums.append(nums.pop(0)) # Rotate the array by one position

            # Check @nums if it sorted, return @True if so
            if nums == sort:
                return True 

            # Increment @idx
            idx += 1

        # Return @False if @nums didn't become sorted after some rotations
        return False
