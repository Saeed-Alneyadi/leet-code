class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        # Variable Initialization
        count = 0

        # Walks out through every item in @items anc check if one of the conditions is @True
        for item in items:
            if ruleKey == "type" and ruleValue == item[0]:
                count += 1

            if ruleKey == "color" and ruleValue == item[1]:
                count += 1

            if ruleKey == "name" and ruleValue == item[2]:
                count += 1

        # Return @count with the number of items in @items with these conditions
        return count
