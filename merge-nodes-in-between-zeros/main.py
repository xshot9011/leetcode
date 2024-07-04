# https://leetcode.com/problems/merge-nodes-in-between-zeros/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        basePointer = head
        runnerPointer = head.next
        summation = 0

        while runnerPointer is not None:
            if runnerPointer.val == 0:
                basePointer.val = summation
                if runnerPointer.next is not None:
                    basePointer.next = runnerPointer
                    basePointer = runnerPointer
                else:
                    basePointer.next = None
                summation = 0
            else:
                summation += runnerPointer.val

            runnerPointer = runnerPointer.next

        # Time: O(n)
        # Space: O(1)
        return head
