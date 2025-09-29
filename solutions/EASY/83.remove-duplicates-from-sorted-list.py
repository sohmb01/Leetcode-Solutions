# Problem ID: 83
# Title: Remove Duplicates from Sorted List
# Runtime: 40 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev=head
        if head==None:
            return head
        curr=head.next
        while (curr!=None):
            if prev.val==curr.val:
                prev.next=curr=curr.next
                
            else:
                temp=curr.next
                prev=curr
                curr=temp
        return head