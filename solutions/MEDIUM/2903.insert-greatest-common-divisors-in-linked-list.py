# Problem ID: 2903
# Title: Insert Greatest Common Divisors in Linked List
# Runtime: 368 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def gcd(a,b):
            if a>b:
                return gcd(b,a)
            cnt = a
            while cnt:
                if not a%cnt and not b%cnt:
                    return cnt
                cnt-=1
            return 1
        curr,nxt = head,head.next
        if not nxt:
            return head
        while nxt:
            node = ListNode()
            node.val = gcd(curr.val,nxt.val)
            node.next = nxt
            curr.next = node
            curr = nxt
            nxt = curr.next
        return head