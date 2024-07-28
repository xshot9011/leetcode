# https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ansPointer = ListNode(-1, head) # Desciptino node val 0 - 50
        prevPointer = ansPointer
        currentPointer = head
        while currentPointer is not None:
            if currentPointer.val == val:
                prevPointer.next = currentPointer.next
                currentPointer = currentPointer.next
            else:
                prevPointer = currentPointer
                currentPointer = currentPointer.next
        return ansPointer.next
