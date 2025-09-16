class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        # Variables Initialization
        X = 0

        # Looping through @operations list
        for curr in operations:
            # Incrementing @X if the operation is "X++" or "++X"
            if curr == "++X" or curr == "X++":
                X += 1
            # Decrementing @X if the oepration is "X--" or "--X"
            elif curr == "X--" or curr == "--X":
                X -= 1

        # Return @X
        return X
