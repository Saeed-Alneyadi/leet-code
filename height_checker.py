class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # Variable Initialization
        sort = sorted(heights)
        count = 0

        # Count what elements are not the same in the sorted version of @heights
        for idx, item in enumerate(heights):
            if item != sort[idx]:
                count += 1

        # Return @count, which is the number of elements that is not the same
        return count
