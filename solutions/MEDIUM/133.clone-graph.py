# Problem ID: 133
# Title: Clone Graph
# Runtime: 42 ms

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        
        def dfs(node):
            if not node or node.val in visited:
                return
            copy = Node(node.val, None)
            visited[copy.val] = copy
            for neighbor in node.neighbors:
                if neighbor.val in visited:
                    copy.neighbors.append(visited[neighbor.val])
                else:
                    copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node)