# Problem ID: 775
# Title: N-ary Tree Preorder Traversal
# Runtime: 40 ms

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        l=[]
        self.helper(root,l)
        return l
    def helper(self, node, l):
        if node:
            l.append(node.val)
            for child in node.children :
                self.helper(child, l)