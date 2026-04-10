# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        newHead = head

        if head.next:
            newHead = self.reverseList(head.next)
            # Reverses the link between the last node and head
            head.next.next = head
        head.next = None

        return newHead