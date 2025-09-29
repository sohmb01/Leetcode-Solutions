# Problem ID: 92
# Title: Reverse Linked List II
# Runtime: 0 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        i = 1
        while i<left:
            prev = prev.next
            i+=1
        
        curr = prev.next
        for _ in range(right-left):
            temp = prev.next
            prev.next = curr.next
            curr.next = curr.next.next
            prev.next.next = temp

        return dummy.next
            
        