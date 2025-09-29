# Problem ID: 784
# Title: Insert into a Binary Search Tree
# Runtime: 0 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        node = TreeNode(val)
        if not root:
            return node
        while curr:
            if curr.val > val:
                if curr.left:
                    curr = curr.left
                    continue
                curr.left = node
                break
            else:
                if curr.right:
                    curr = curr.right
                    continue
                curr.right = node
                break
        return root