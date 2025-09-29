# Problem ID: 141
# Title: Linked List Cycle
# Runtime: 48 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head or not head.next:
            return False
        slow, fast = head , head.next
        while fast:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next 
            if fast and fast.next:
                fast = fast.next
        return False
