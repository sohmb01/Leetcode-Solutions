# Problem ID: 764
# Title: N-ary Tree Level Order Traversal
# Runtime: 52 ms

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q,l=[root],[]
        while q:
            l.append([node.val for node in q ])
            q=[child for node in q for child in node.children if child]
            
        return l
            
            