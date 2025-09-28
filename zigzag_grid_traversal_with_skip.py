class Solution(object):
    def zigzagTraversal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        # Variables Initialization
        grid_list = []

        # Make the @gird as one list where it starts from the left of the first row and move one to last element on the row
        # then start at the end of the following row and keeps alternating until the end
        for i, row in enumerate(grid):
            if i % 2 == 0:
                for element in row:
                    grid_list.append(element)
            else:
                row.reverse()
                for element in row:
                    grid_list.append(element)
                row.reverse()
            
        # Return the element where their indices are evens
        return [element for idx, element in enumerate(grid_list) if idx % 2 == 0]
