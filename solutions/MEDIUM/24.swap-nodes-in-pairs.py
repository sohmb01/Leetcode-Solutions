# Problem ID: 24
# Title: Swap Nodes in Pairs
# Runtime: 0 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        nxt = curr.next
        prev = ans = ListNode(-1)
        prev.next = curr
        while nxt:
            curr.next,nxt.next,prev.next =  nxt.next, curr, nxt
            prev = curr
            curr = curr.next
            if curr:
                nxt = curr.next
            else:
                nxt = None
        return ans.next