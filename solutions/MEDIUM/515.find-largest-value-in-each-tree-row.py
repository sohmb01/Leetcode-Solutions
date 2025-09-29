# Problem ID: 515
# Title: Find Largest Value in Each Tree Row
# Runtime: 0 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        def bfs(nodes):
            if not nodes:
                return 
            temp = []
            mx = -float("inf")
            for node in nodes:
                mx = max(mx,node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            ans.append(mx)
            bfs(temp)
        bfs([root])
        return ans
        
