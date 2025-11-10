class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        # Variables Initalization
        common = -1
        prev = edges[0]

        # Loops every edge except for the first one and see which vertix is the common
        for e in edges[1:]:
            # Checks whether the first vertix in @prev edge does exist in current @e edge
            if prev[0] in e:
                common = prev[0] # Set the common vertix to @prev[0]
            # Checks whether the second vertix in @prev edge does exist in current @e edge
            elif prev[1] in e:
                common = prev[1] # Set the common vertix to @prev[1]

            # Set the current edge in @prev to compare it with the next one
            prev = e

        # Return @common which represents the center
        return common
