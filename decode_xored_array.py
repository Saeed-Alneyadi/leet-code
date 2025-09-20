class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        # Variables Initialization
        result = [first]

        # Generating @result with inversed XOR
        for idx, enc in enumerate(encoded):
            result.append(enc ^ result[idx])

        # Return @result with XOR results
        return result
