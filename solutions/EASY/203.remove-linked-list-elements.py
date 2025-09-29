# Problem ID: 203
# Title: Remove Linked List Elements
# Runtime: 72 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        while head.val==val:
            head=head.next
            if not head:
                return head
        last=head
        curr=head.next
        while curr:
            if curr.val==val:
                last.next=curr.next
                curr=curr.next
            else:
                last,curr=curr,curr.next
        return head
        