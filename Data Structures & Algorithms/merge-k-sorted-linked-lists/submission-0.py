# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        node=[]
        for i in lists:
            while i:
                node.append(i.val)
                i=i.next
        node.sort()
        res=ListNode(0)
        current=res
        for j in node:
            current.next=ListNode(j)
            current=current.next  
        return res.next          