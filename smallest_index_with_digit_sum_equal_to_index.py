class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = [sum(int(digit) for digit in str(num)) for num in nums]
        indices = [idx for idx in range(len(sums)) if idx == sums[idx]]

        if len(indices) > 0:
            return indices[0]
        else:
            return -1
