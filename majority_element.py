class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Return the element with a count higher than floor of n/2
        for num in set(nums):
            if nums.count(num) > int(len(nums) / 2):
                return num
