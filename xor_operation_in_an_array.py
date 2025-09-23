class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        # Variable Initialization
        i = 0
        nums = [0] * n
        result = 0

        # Gets the array with "nums[i] = start + 2 * i" elements
        while i < n:
            nums[i] = start + 2 * i
            i += 1

        # Gets the bitwise XOR of all elements in @nums array
        for num in nums:
            result ^= num

        # Return @result
        return result
