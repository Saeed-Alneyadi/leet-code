class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        # Variables Initialization
        locations = [(0,0)]

        # Reads the @path and store coordinates
        for i, p in enumerate(path):
            pair = locations[i]
            if p == 'N':
                locations.append((pair[0], pair[1] + 1))
            elif p == 'E':
                locations.append((pair[0] + 1, pair[1]))
            elif p == 'S':
                locations.append((pair[0], pair[1] - 1))
            elif p == 'W':
                locations.append((pair[0] - 1, pair[1]))

        # Getting the @duplicates in @locations
        duplicates = [i for i in set(locations) if locations.count(i) > 1]

        # Return true if duplicate coordinates exist, false if it is not
        if len(duplicates) > 0:
            return True
        else:
            return False
