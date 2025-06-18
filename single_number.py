class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Variables Initialization
        freq = Counter(nums)

        # Return the item with one frequency
        return [word for word, count in freq.items() if count == 1][0]
        
