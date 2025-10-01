class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        # Loops through @fruits list
        for i, fruit in enumerate(fruits):
            # Loops through @basckets list for each fruit in @fruits
            for j, basket in enumerate(baskets):
                # If @basket is greater or equal to @fruit...
                if basket >= fruit:
                    fruits[i] = 0 # Element at index i of @fruits will set to zero
                    baskets[j] = 0 # Element at index j of @baskets will set to zero
                    break # Loop will stop

        # Returns the number of elements in @fruits that are greater than zero,
        # since zero means fruit has been placed
        return len([fruit for fruit in fruits if fruit > 0])
