# Problem ID: 103
# Title: Binary Tree Zigzag Level Order Traversal
# Runtime: 0 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []
        def levelOrder(nodes):
            if not len(nodes) or not nodes[0]:
                return
            curr, nextLevel = [], []
            for node in nodes:
                curr.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            if len(ans)%2 == 0:
                ans.append(curr)
            else:
                ans.append(curr[::-1])
            levelOrder(nextLevel)
        levelOrder([root])
        return ans
            
