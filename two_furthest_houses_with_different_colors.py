class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        # Variables Initialization
        distances = []

        # Calulate the distance of only different houses color
        for idx1, house1 in enumerate(colors):
            for idx2, house2 in enumerate(colors):
                if house1 != house2:
                    distances.append(abs(idx1 - idx2))

        # Return the maximum distance of different houses color
        return max(distances)
