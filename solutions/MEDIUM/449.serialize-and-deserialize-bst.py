# Problem ID: 449
# Title: Serialize and Deserialize BST
# Runtime: 54 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        nodes = []
        def bfs(node):
            if not node:
                return
            nodes.append(node.val)
            bfs(node.left)
            bfs(node.right)
        bfs(root)
        return ",".join(map(str, nodes))
            
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        values = deque([int(val) for val in data.split(",")])

        def bfs(l,r):
            if values and l < values[0] < r:
                root = TreeNode(values.popleft())
                root.left = bfs(l, root.val)
                root.right = bfs(root.val,r)
                return root
        return bfs(float('-inf'),float('inf'))








# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans