# Problem ID: 893
# Title: All Nodes Distance K in Binary Tree
# Runtime: 45 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def setParent(node, parent):
            if not node:
                return
            parents[node] = parent
            setParent(node.left,node)
            setParent(node.right,node)
        
        def bfs(node, dist):
            if not node or dist>k or node in visit:
                return 
            visit.add(node)
            if dist == k:
                ans.append(node.val)
            bfs(node.left, dist+1)
            bfs(node.right, dist+1)
            bfs(parents[node], dist+1)


        
        parents = {}
        visit = set()
        ans = []
        setParent(root, None)
        bfs(target, 0)
        return ans



        
        
        
            

