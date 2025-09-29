# Problem ID: 297
# Title: Serialize and Deserialize Binary Tree
# Runtime: 79 ms

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        l = []
        def dfs(node):
            if not node:
                l.append("N")
            else:
                l.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        x = ",".join(l)
        return x

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.i = 0
        data = list(data.split(","))
        def dfs():
            if data[self.i] == "N":
                self.i+=1
                return None
            else:
                node = TreeNode()
                node.val = int(data[self.i])
                self.i+=1
                node.left = dfs()
                node.right = dfs()
            return node
        return dfs()
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))