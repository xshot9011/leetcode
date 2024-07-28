# https://leetcode.com/problems/linked-list-cycle/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        found = {}
        while head:
            if head.next not in found:
                found[head.next] = True
            elif head.next in found:
                return True
            head = head.next
