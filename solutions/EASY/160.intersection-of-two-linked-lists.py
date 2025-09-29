# Problem ID: 160
# Title: Intersection of Two Linked Lists
# Runtime: 152 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        s=set()
        curr=headA
        while curr:
            s.add(curr)
            curr=curr.next
        curr=headB
        while curr:
            if curr in s:
                return curr
            curr=curr.next