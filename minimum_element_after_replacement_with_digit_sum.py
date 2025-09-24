class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Return the minimum element of the array that consist of element, each with it sums of their digits
        return min([sum(int(digit) for digit in str(num)) for num in nums])
