# Problem ID: 142
# Title: Linked List Cycle II
# Runtime: 47 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        while head:
            visited.add(head)
            head = head.next
            if head in visited:
                return head
        return None