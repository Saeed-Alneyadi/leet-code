class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Forming lists of @s and @t strings
        list1, list2 = list(s), list(t)

        # Remove all common elements in both @list1 and @list2
        while len(list1) > 0:
            if list1[0] in list2:
                list2.remove(list1.pop(0))
            else:
                break

        # Return the remaining element in @list2
        return list2[0]
