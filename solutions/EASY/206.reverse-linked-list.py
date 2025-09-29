# Problem ID: 206
# Title: Reverse Linked List
# Runtime: 28 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        temp=head.next
        head.next=None
        while temp:
            k=temp.next
            temp.next=head
            head=temp
            temp=k
        return head