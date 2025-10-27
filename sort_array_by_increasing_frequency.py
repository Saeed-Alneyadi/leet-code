class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Variable Initialization
        lib = {}
        ans = []
        
        # Insert each unique number with its count to @lib
        for num in set(nums): lib.update({num:nums.count(num)})

        # Return sorted the array in increasing order based on the frequency of the values,
        # If multiple values have the same frequency, sort them in decreasing order
        return sorted(nums, key=lambda x: (lib[x], -x))
