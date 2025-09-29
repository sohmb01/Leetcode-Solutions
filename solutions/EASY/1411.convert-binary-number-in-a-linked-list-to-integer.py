# Problem ID: 1411
# Title: Convert Binary Number in a Linked List to Integer
# Runtime: 28 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans=0
        while head:
            ans=(ans*2 + head.val)
            head=head.next
        return ans