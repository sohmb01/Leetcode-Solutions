# Problem ID: 776
# Title: N-ary Tree Postorder Traversal
# Runtime: 48 ms

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        l=[]
        self.helper(root,l)
        return l
    def helper(self, node, l):
        if node:
            for child in node.children:
                self.helper(child,l)
            l.append(node.val)