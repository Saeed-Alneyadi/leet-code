# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # If there is no nodes in head, it will be returned as itself
        if head == None:
            return head

        # Varaibles Initialization
        temp = head.val
        prev = head
        curr = head.next

        # Loops until end of list nodes is reached
        while curr != None and prev != None:
            if prev.val == curr.val: # if @prev node value is equal to @curr node value...
                prev.next = curr.next # Duplicate ListNode Removal

                if curr != None: # If @curr is null...
                    curr = curr.next # Set @curr to @curr next

            else:
                prev = curr # Set @prev (previous node) to @curr (current node)
                curr = curr.next # Set @curr to @curr next

        # Return @head after modification
        return head
