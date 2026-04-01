# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to start the result list
        dummy = ListNode()
        cur = dummy
        
        carry = 0
        # Continue while there's a node in l1, l2, or a remaining carry
        while l1 or l2 or carry:
            # Get values if nodes exist, else use 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0