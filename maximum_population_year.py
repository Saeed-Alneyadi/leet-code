class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        # Variable Initialization
        minimum = 2000
        maximum = 2000
        counts = []

        # Get the minimum and maximum years
        for log in logs:
            if minimum > log[0]:
                minimum = log[0]

            if maximum < log[1]:
                maximum = log[1]

        # Get the population counts of each year and store it to @counts
        year = minimum
        while year < maximum:
            count = 0
            for log in logs:
                if year >= log[0] and year < log[1]:
                    count += 1

            counts.append(count)
            year += 1

        # Return the year of maximum population count by adding minimum year with it counts and return it
        return minimum + counts.index(max(counts))
