# Problem ID: 61
# Title: Rotate List
# Runtime: 36 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        cnt=0
        node=head
        while node:
            last=node
            node=node.next
            cnt+=1
        k=cnt-(k%cnt)
        last.next=head
        for i in range (k-1):
            head=head.next
        ans=head.next
        head.next=None
        
        return ans
        