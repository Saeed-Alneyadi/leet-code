class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Gets every element in @nums1 that is in @nums2
        ans1 = [num for num in nums1 if num in nums2]

        # Gets every element in @nums2 that is in @nums1
        ans2 = [num for num in nums2 if num in nums1 and not num in ans1]

        # Return the list version of the set of the two @arrays
        return list(set(ans1 + ans2))
