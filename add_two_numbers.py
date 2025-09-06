# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # New refrences to the linked lists
        first, second = l1, l2

        # Initializations
        idx = 0
        carry = 0
        result = ListNode(0)
        current = result

        # Summing the two linkedlists
        while True:
            # Summing indiviual digits
            current.val += first.val + second.val + carry
            carry = 0

            # Carry the extra one if it exists
            if(current.val > 9):
                carry = 1
                current.val -= 10

            # While loop statement breaker
            if first.next is None and second.next is None and carry == 0:
                break
            elif first.next is None and second.next is None and carry == 1:
                current.next = ListNode(carry)
                break
            else:
                current.next = ListNode(0)
                current = current.next

            # Moving to the next digit in the first number if there is a one
            if first.next is not None:
                first = first.next
            else:
                first =  ListNode(0)

            # Moving to the next digit in the second number if there is a one
            if second.next is not None:
                second = second.next
            else:
                second =  ListNode(0)

            # Incrementing while loop index
            idx += 1

        # Return Statement
        return result
        
