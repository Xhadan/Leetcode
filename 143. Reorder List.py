# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        # Step 1: Find the middle of the list
        # Fast moves 2x speed, Slow moves 1x. When Fast hits end, Slow is at middle.
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        prev, curr = None, slow.next
        # Important: Break the link between first and second half
        slow.next = None 
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # Step 3: Interleave the two halves
        # first is the start of the 1st half, second is the start of reversed 2nd half
        first, second = head, prev
        while second:
            # Temporarily store the next nodes
            tmp1, tmp2 = first.next, second.next
            
            # Re-link
            first.next = second
            second.next = tmp1
            
            # Move pointers forward
            first = tmp1
            second = tmp2