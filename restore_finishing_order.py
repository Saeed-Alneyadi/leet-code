class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        i = 0
        while i < len(order):
            if not order[i] in friends:
                order.pop(i)
            else:
                i += 1

        return order
