# Problem ID: 234
# Title: Palindrome Linked List
# Runtime: 756 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast,slow=head,head
        while fast:
            slow=slow.next
            fast=fast.next
            if fast:
                fast=fast.next        
        
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        slow=node
        temp=head
        while temp and slow:
            if temp.val!=slow.val:
                return False
            temp=temp.next
            slow=slow.next
        return True
 