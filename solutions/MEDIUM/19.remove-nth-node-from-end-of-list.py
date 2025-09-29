# Problem ID: 19
# Title: Remove Nth Node From End of List
# Runtime: 36 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ans=ListNode(-1)
        ans.next=head
        temp=ans
        c=0
        while temp:
            temp=temp.next
            c+=1
        temp=ans
        k=c-n-1
        while k:
            k-=1
            temp=temp.next
        
        temp.next=temp.next.next
        return ans.next
        