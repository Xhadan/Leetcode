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
            
            # New digit calculation
            val = v1 + v2 + carry
            carry = val // 10    # e.g., 15 // 10 = 1
            val = val % 10      # e.g., 15 % 10 = 5
            
            # Create new node and move pointer
            cur.next = ListNode(val)
            cur = cur.next
            
            # Advance input pointers if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next