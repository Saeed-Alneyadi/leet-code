class Solution(object):
    def stableMountains(self, height, threshold):
        """
        :type height: List[int]
        :type threshold: int
        :rtype: List[int]
        """
        # Return an array containing the indices of all stable mountains
        return [idx for idx, hgt in enumerate(height) if idx > 0 and height[idx - 1] > threshold]
