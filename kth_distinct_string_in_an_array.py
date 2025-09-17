class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        # Variables Initialization
        distinct = []
        removed = []
        idx = k - 1

        # Extract the distinct words from @arr
        for word in arr:
            if word in distinct:
                distinct.remove(word)
                removed.append(word)
            elif word not in removed:
                distinct.append(word)

        # Return the kth distinct string from the distinct array list if it is exist,
        # if it is not, it return empty string
        if idx < len(distinct):
            return distinct[idx]
        else:
            return ""
