class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Getting the even frequencies stored in @even_freq and the odd ones in @odd_freq
        even_freq = [s.count(ch) for ch in s if s.count(ch) % 2 == 0]
        odd_freq = [s.count(ch) for ch in s if s.count(ch) % 2 == 1]

        # Substract the minimum of @even_freq from the maximum of @odd_freq to get the maximum difference between odd and even frequencies
        return max(odd_freq) - min(even_freq)
