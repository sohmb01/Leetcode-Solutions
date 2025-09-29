# Problem ID: 655
# Title: Print Binary Tree
# Runtime: 0 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        
        def getHeight(node,curr):
            if not node:
                return curr
            return max(getHeight(node.left,curr+1),getHeight(node.right,curr+1))

        def fillTree(node, row, left, right):
            if not node:
                return
            col = (left+right+1)//2
            tree[row][col] = str(node.val)
            fillTree(node.left, row+1, left, col-1)
            fillTree(node.right, row+1, col+1, right)

        height = getHeight(root, 0) - 1
        cols = 2**(height+1) - 1
        tree = [[""]* cols for _ in range(height+1)]
        fillTree(root,0,0,cols-1)
        return tree
