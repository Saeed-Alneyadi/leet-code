class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        # Variables Initialization
        result1 = [x for x in nums1 if x in nums2 or x in nums3]
        result2 = [x for x in nums2 if x in nums3]

        # Return the all the values that are present in at least two sets
        return list(dict.fromkeys(result1 + result2))
