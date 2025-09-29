# Problem ID: 82
# Title: Remove Duplicates from Sorted List II
# Runtime: 40 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        soham = ListNode(0,head)
        prev=soham
        while head:
            if head.next and head.val==head.next.val:
                while head.next and head.val == head.next.val:
                    head=head.next
                prev.next = head.next
            else:
                prev=prev.next
            head=head.next
        return soham.next