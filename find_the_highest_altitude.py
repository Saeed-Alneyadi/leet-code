class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        # Varaibles Initialization
        alts = [0]

        # Calcualtes altitudes and store them to @alts
        for i, g in enumerate(gain):
            alts.append(alts[i] + g)

        # Return the highest altitude
        return max(alts)
