# Problem ID: 908
# Title: Middle of the Linked List
# Runtime: 32 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next
            if fast:
                fast=fast.next
        return slow