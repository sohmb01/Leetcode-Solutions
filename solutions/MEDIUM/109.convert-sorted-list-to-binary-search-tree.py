# Problem ID: 109
# Title: Convert Sorted List to Binary Search Tree
# Runtime: 7 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        slow,fast,prev = head,head,None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        node = TreeNode(slow.val)
        if prev:
            prev.next = None
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(slow.next)

        return node