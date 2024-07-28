# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        mapA = {} # {val: [(pointer1, counterA), ...]}
        pointerA = headA
        pointerB = headB
        
        # Create structure of mapA
        while pointerA is not None:
            if pointerA.val in mapA:
                mapA[pointerA.val].append(pointerA)
            else:
                mapA[pointerA.val] = [pointerA]
            pointerA = pointerA.next

        # Running pointerB to A
        while pointerB is not None:
            if pointerB.val in mapA: # Checking value match O(1)
                for pointerA in mapA[pointerB.val]:
                    tempPointerB = pointerB
                    tempPointerA = pointerA
                    while tempPointerB is not None and tempPointerA is not None:
                        if tempPointerB != tempPointerA: # Checking ref
                            break
                        tempPointerB = tempPointerB.next
                        tempPointerA = tempPointerA.next
                    if tempPointerB is None and tempPointerA is None:
                        return pointerA

            pointerB = pointerB.next
        # Time: O(n)*O(m)*O(m+n)
        # Spec: O(m)
        return None
