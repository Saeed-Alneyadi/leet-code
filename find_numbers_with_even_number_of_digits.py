class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Create a list of @nums element where their string version letter counts is even, return the length of this generated @list
        return len([num for num in nums if len(str(num)) % 2 == 0])
