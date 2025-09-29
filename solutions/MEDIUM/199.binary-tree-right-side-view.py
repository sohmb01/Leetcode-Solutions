# Problem ID: 199
# Title: Binary Tree Right Side View
# Runtime: 0 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return []
        q = deque()
        q.append(root)
        while q:
            children = deque()
            while q:
                curr = q.popleft()
                if curr.left:
                    children.append(curr.left)
                if curr.right:
                    children.append(curr.right)
            ans.append(curr.val)
            q = children
        return ans

