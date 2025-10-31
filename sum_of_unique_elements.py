class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Add to the sum only the numbers that their counts is equal to one 
        return sum([num for num in nums if nums.count(num) == 1])
