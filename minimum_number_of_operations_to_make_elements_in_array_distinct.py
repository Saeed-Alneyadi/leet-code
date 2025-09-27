class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Variable Initialization
        count = 0

        # Keeps removing 3 elements until there is no duplicates in @nums while calculating 
        # 3 element removal opearation count
        while True:
            if len([n for n in nums if nums.count(n) > 1]) > 0:
                count += 1
                for i in range(3):
                    if len(nums) > 0:
                        nums.pop(0)
            else:
                break

        # Return the minimum number of operations for 3 elements removal
        return count
