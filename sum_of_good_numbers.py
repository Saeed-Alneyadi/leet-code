class Solution(object):
    def sumOfGoodNumbers(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Return the sum of all the good elements in the array
        return sum([num for i, num in enumerate(nums) if (i-k<0 and i+k>=len(nums)) or ((i - k < 0) or (num > nums[i - k])) and ((i + k >= len(nums)) or (num > nums[i + k]))])
