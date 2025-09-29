# Problem ID: 99
# Title: Recover Binary Search Tree
# Runtime: 4 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            arr.append(root)
            inorder(root.right)
        
        inorder(root)
        firstNode,secondNode = arr[0],arr[-1]
        for i in range(len(arr)-1):
            if arr[i].val > arr[i+1].val:
                firstNode = arr[i]
                break
        for i in range(len(arr)-1,-1,-1):
            if arr[i].val < arr[i-1].val:
                secondNode = arr[i]
                break
        
        firstNode.val, secondNode.val = secondNode.val, firstNode.val
        