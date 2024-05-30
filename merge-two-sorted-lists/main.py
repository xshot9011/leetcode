# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = cursor = ListNode()
        while list1 and list2:
            if list1.val >= list2.val:
                cursor.next = ListNode(list2.val)
                list2 = list2.next
            else:
                cursor.next = ListNode(list1.val)
                list1 = list1.next
            cursor = cursor.next
        
        cursor.next = list2 if list1 is None else list1
        return mergedList.next
