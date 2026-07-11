# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=head
        slow=None
        while fast:
            next=fast.next
            fast.next=slow
            slow=fast
            fast=next
        return slow
            
        