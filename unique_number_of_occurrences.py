class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr_set = list(set(arr)) # Remove duplicates
        counts = [arr.count(num) for num in arr_set] # Getting the counts for each number in @arr

        # Return @True if all elements in @counts is greater than zero, otherwise @False
        return all(item > 0 for item in [abs(num1 - num2) for i1, num1 in enumerate(counts) for i2, num2 in enumerate(counts) if i1 != i2])
