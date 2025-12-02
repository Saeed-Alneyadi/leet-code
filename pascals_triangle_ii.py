class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        tri = [[1]] # Whole Pascal Triangle Initialization

        for i in range(1, rowIndex + 1):
            temp = [1,1] # Row Initialization

            for j in range(1,i):
                temp.insert(j, tri[i-1][j-1] + tri[i-1][j]) # Insert the added elements

            tri.append(temp) # Append @temp to @tri

        # Return the answer which is the Pascal Triangle row at @rowIndex in @tri
        return tri[rowIndex]
