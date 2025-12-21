class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Zero Counter
        count = 0

        # Remove all zeros in @nums and count how much of them
        while 0 in nums:
            nums.remove(0)
            count += 1

        # Append @count number of zeros to the end of @nums
        for i in range(count):
            nums.append(0)
