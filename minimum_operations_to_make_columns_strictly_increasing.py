class Solution(object):
    def minimumOperations(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Variable Initialization
        oprCount = 0

        # Loops through each column
        for j in range(len(grid[0])):
            # Refrence the first row in the @grid
            prevRow = grid[0]

            # Loops through each element in column indexed at @j
            for row in grid[1:]:
                # Incrementing current element and @oprCount until its higher than the previous one
                while row[j] <= prevRow[j]:
                    oprCount += 1
                    row[j] += 1
                
                # Setting @prevRow to @row before moving to other element in same column
                prevRow = row
        
        # Return the number incrementing operations executed
        return oprCount
