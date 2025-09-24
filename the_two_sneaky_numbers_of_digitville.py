class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Return an array of size two containing the duplicates numbers
        return list({num for num in nums if nums.count(num) > 1})
