# https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # answer_node = None
        # pointer = None
        # fractor = 0
        # while l1 or l2 or fractor:
        #     l1_value = l1.val if l1 else 0
        #     l2_value = l2.val if l2 else 0
        #     summation = l1_value + l2_value
        #     if answer_node is None:
        #         answer_node = ListNode(summation%10)
        #         pointer = answer_node
        #     else:
        #         pointer.next = ListNode((summation+fractor)%10)
        #         pointer = pointer.next
        #     fractor = (summation+fractor)//10

        #     l1 = l1.next if l1 else None
        #     l2 = l2.next if l2 else None
        # if fractor != 0:
        #     pointer.next = ListNode((fractor)%10)
        # return answer_node

        answer_node = ListNode(0)
        pointer = answer_node
        fractor = 0

        while l1 or l2 or fractor:
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0

            summation = l1_value + l2_value + fractor
            pointer.next = ListNode(summation%10)
            pointer = pointer.next
            fractor = summation // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return answer_node.next



        

        