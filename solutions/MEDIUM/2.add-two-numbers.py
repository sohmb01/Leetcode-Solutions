# Problem ID: 2
# Title: Add Two Numbers
# Runtime: 3 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        elif not l2:
            return l1
        temp = l1
        len1 = 1
        while temp:
            temp = temp.next
            len1+=1
        temp = l2
        len2 = 1
        while temp:
            temp = temp.next
            len2+=1
        if len2>len1:
            l1,l2 = l2,l1
            len1,len2 = len2,len1
        
        curr = l1
        carry = 0
        while curr:
            if l2:
                s = curr.val + l2.val + carry
                l2 = l2.next
            else:
                s = curr.val + carry

            curr.val = s%10
            carry = s//10
            if not curr.next and carry:
                curr.next = ListNode(carry)
                curr = curr.next
            curr = curr.next
        
        return l1