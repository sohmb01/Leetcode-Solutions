# Problem ID: 337
# Title: House Robber III
# Runtime: 3 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def helper(node):
            if not node:
                return 0,0
            
            leftRob,leftNotRob = helper(node.left)
            rightRob, rightNotRob = helper(node.right)

            robNode = node.val + leftNotRob + rightNotRob
            notRobNode = max(leftRob,leftNotRob) + max(rightRob,rightNotRob)
            return robNode, notRobNode
        return max(helper(root))