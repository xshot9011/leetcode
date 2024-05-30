# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # a b c d
        # b -> a
        p = head
        q = None

        while head is not None:
            if q is None:
                q = ListNode(val=head.val)
            else:
                q = ListNode(val=head.val, next=q)
            head = head.next
        return q
