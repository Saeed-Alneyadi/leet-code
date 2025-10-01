class Solution(object):
    def maxContainers(self, n, w, maxWeight):
        """
        :type n: int
        :type w: int
        :type maxWeight: int
        :rtype: int
        """
        # Returns the minimum among the number of containers that can be held on deck and
        # the number of containers that the ship can hold on its maximum weight
        return min([n*n, maxWeight/w])
