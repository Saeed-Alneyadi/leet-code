class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Creates subarrays of size @k stored in @subArrays
        subArrays = [nums[idx:idx + k] for idx in range(len(nums) - k + 1)]
        # print(subArrays)
        
        # Calculate the sum of apperence for each number in @nums in the @subArrays of size @k,
        # store only numbers in @nums that their sum is equal to one, other store -1 instead
        result = [num if (sum(1 if num in arr else 0 for arr in subArrays) == 1) else -1 for num in nums]
        # print(result)

        # Return the largest or maximum number in @result if the length of it is larger than 0, otherwise return -1
        if len(result) > 0: return max(result); return -1
