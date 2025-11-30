class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Removing the useless elements in @nums1
        for i in range(len(nums1) - m):
            nums1.pop(len(nums1) - 1)

        # Removing the useless elements in @nums2
        for i in range(len(nums2) - n):
            nums2.pop(len(nums2) - 1)

        # Adding all @nums2 elements to @nums1
        for num in nums2:
            nums1.append(num)

        # Making @nums1 in increasing order
        nums1.sort()
