class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Variables Intialization
        evens = []
        odds = []

        # Seprate @nums into @evens and @odds
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                evens.append(nums[i])
            else:
                odds.append(nums[i])
        
        # Return new array of @even elements in the left and @odds in the right
        return evens + odds
