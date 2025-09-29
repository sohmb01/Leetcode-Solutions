# Problem ID: 114
# Title: Flatten Binary Tree to Linked List
# Runtime: 0 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        st = []
        if not root:
            return root
        st.append(root.right)
        st.append(root.left)
        while st:
            node = st.pop()
            if node:
                root.right = node
                root.left = None
                root = root.right
                st.append(node.right)
                st.append(node.left)
