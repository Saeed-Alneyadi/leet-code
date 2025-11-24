class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        tri = [[1]] # Whole Pascal Triangle Initialization

        for i in range(1, numRows):
            temp = [1,1] # Row Initialization

            for j in range(1,i):
                temp.insert(j, tri[i-1][j-1] + tri[i-1][j]) # Insert the added elements

            tri.append(temp) # Append @temp to @tri

        # Return the answer which is the  Pascal Triangle represented with @tri
        return tri
