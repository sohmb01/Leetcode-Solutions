# Problem ID: 95
# Title: Unique Binary Search Trees II
# Runtime: 7 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def rec(start,end):
            if start > end:
                return [None]
            trees = []
            for i in range(start, end+1):
                leftTrees = rec(start,i-1)
                rightTrees = rec(i+1, end)

                for l in leftTrees:
                    for r in rightTrees:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        trees.append(currTree)
            return trees
        return rec(1,n) if n else []
            