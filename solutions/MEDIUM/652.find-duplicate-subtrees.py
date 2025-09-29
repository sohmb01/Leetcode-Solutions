# Problem ID: 652
# Title: Find Duplicate Subtrees
# Runtime: 5 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = []
        mp = defaultdict(int)
        def serialize(node, path):
            if not node:
                return "#"
            subPath = ",".join([str(node.val), serialize(node.left, path), serialize(node.right, path)])
            mp[subPath]+=1
            if mp[subPath] == 2:
                res.append(node)
            return path + subPath
        
        serialize(root, "")
        return res
        

