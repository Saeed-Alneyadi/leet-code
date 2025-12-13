class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        # Variable Initialization
        idx = 0

        # Loops through @arr and checks for zeros to insert an extra zero after them
        # while maintaing @arr length
        while idx < len(arr):
            if arr[idx] == 0:
                arr.insert(idx, 0) # Insert zero at @idx in @arr
                idx += 1 # Increment @idx to avoid reading the extra zero
                arr.pop(len(arr) - 1) # Maintains @arr length

            idx += 1 # Increment @idx which is loop counter
