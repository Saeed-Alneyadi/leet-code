class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Variables Initialization
        result = []
        arr_len = len(nums)
        idx = 0

        # Loops through every element where it calculate the sum of array parition to this element
        # append it to @result
        while idx < arr_len:
            result.append(sum(nums[:idx + 1]))
            idx += 1

        # Return @result with sums of 1d rrays
        return result
