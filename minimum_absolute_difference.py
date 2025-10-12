class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort() # Sort the array @arr in ascending order
        minimum = min([arr[i + 1] - arr[i] for i in range(len(arr) - 1)]) # Getting the minimum absolute difference of all difference between each two elements
        return [[arr[i], arr[i + 1]] for i in range(len(arr) - 1) if arr[i + 1] - arr[i] == minimum] # Return the pairs with a difference equal to the minimum absolute difference
