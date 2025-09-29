# Problem ID: 105
# Title: Construct Binary Tree from Preorder and Inorder Traversal
# Runtime: 169 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder :
            return None
        
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                ind = i
                break
        node = TreeNode()
        node.val = preorder[0]
        node.left = self.buildTree(preorder[1:ind+1],inorder[:ind])
        node.right = self.buildTree(preorder[ind+1:],inorder[ind+1:])
        return node