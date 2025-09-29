# Problem ID: 148
# Title: Sort List
# Runtime: 244 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, l1, l2):
        curr = head = ListNode()
        while l1 or l2:
            if not l2 or l1 and l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            elif not l1 or l2 and l1.val>= l2.val:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        return head.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow, fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        temp = slow.next
        slow.next = None
        
        return self.merge(self.sortList(head),self.sortList(temp))