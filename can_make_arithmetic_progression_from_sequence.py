class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # Sort the input @arr which is the sequence of numbers
        arr.sort()

        # Calculates the differences and store them in @diff
        diff = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]

        # Return True if all elements in @diff are the same, false otherwise
        return all(element == diff[0] for element in diff)
