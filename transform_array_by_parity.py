class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [num % 2 for num in nums] # Generate an array of 0s and 1s, where 0s for evens and 1s for odds
        result.sort() # Sort the @result array
        return result # Return @result
